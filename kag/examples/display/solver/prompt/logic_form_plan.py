import logging
import re
from string import Template
from typing import List
logger = logging.getLogger(__name__)

from kag.common.base.prompt_op import PromptOp


class LogicFormPlanPrompt(PromptOp):
    instruct_zh = """"instruction": "",
    "function_description": "functionName为算子名;基本格式为 functionName(arg_name1=arg_value1,[args_name2=arg_value2, args_name3=arg_value3]),括号中为参数，被[]包含的参数为可选参数，未被[]包含的为必选参数",
    "function": [
      {
          "functionName": "get_spo",
          "function_declaration": "get_spo(s=s_alias:entity_type[entity_name], p=p_alias:edge_type, o=o_alias:entity_type[entity_name], p.edge_type=value)",
          "description": "查找spo信息，s代表主体，o代表客体，表示为变量名:实体类型[实体名称]，实体名称作为可选参数，当有明确的查询实体时需要给出；p代表谓词，即关系或属性，表示为变量名:边类型或属性类型；这里为每个变量都分配一个变量名，作为后续提及时的指代；注意，s、p、o不能在同一表达式中反复多次出现；当变量为前文指代的变量名是，变量名必须和指代的变量名一致，且只需给出变量名，实体类型仅在首次引入时给定"
      },
      {
          "functionName": "count",
          "function_declaration": "count_alias=count(alias)",
          "description": "统计节点个数，参数为指定待统计的节点集合，只能是get_spo中出现的变量名；count_alias作为变量名表示计算结果，只能是int类型，变量名可作为下文的指代"
      },
      {
          "functionName": "sum",
          "function_declaration": "sum(alias, num1, num2, ...)->sum_alias",
          "description": "数据求和，参数为指定待求和的集合，可以是数字也可以是前文中出现的变量名，其内容只能是数值类型；sum_alias作为变量名表示计算结果，只能是数值类型，变量名可作为下文的指代"
      },
      {
          "functionName": "sort",
          "function_declaration": "sort(set=alias, orderby=o_alias or count_alias or sum_alias, direction=min or max, limit=N)",
          "description": "对节点集合排序，set指定待排序的节点集合，只能是get_spo中出现的变量名；orderby指定排序的依据，为节点的关系或属性名称，若是前文提及过的，则用别名指代；direction指定排序的方向，只能是min(正序)或max(倒序)排列；limit为输出个数限制，为int类型；可作为最后的输出结果"
      },
      {
          "functionName": "get",
          "function_declaration": "get(alias)",
          "description": "返回指定的别名代表的信息，可以是实体、关系路径或get_spo中获取到的属性值；可作为最后的输出结果"
      }
    ],
    """

    default_case_zh = """"cases": [
            {
                "Action": "吴京是谁",
                "answer": "Step1:查询吴京\nAction1:get_spo(s=s1:公众人物[吴京], p=p1, o=o1)\nOutput:输出s1\nAction2:get(s1)"
            },
            {
                "query": "30+6加上华为创始人在2024年的年龄是多少",
                "answer": "Step1:30+6 等于多少？\nAction1:sum(30,6)->sum1\nStep2:华为创始人是谁？\nAction2:get_spo(s=s2:企业[华为],p=p2:创始人,o=o2)\nStep3:华为创始人出生在什么年份？\nAction3:get_spo(s=o2,p=p3:出生年份,o=o3)\nStep4:华为创始人在2024年的年龄是多少？\nAction4:sum(2024,-o3)->sum4\nStep5:30+6的结果与华为创始人在2024年的年龄相加是多少？\nAction5:sum(sum1,sum4)->sum5\nStep6:输出sum5\nAction6:get(sum5)"
            },
            {
                "query": "中华人民共和国铁路法第二十八条的内容是什么",
                "answer": "Step1:中华人民共和国铁路法第二十八条的内容是什么 ?\nAction1:get_spo(s=s1:Chunk[中华人民共和国铁路法第二十八条], p=p1:content, o=o1:Text)\n Action2: get(o1)"
            },
            {
                "Action": "张*三是一个赌博App的开发者吗?",
                "answer": "Step1:查询是否张*三的分类\nAction1:get_spo(s=s1:自然人[张*三], p=p1:属于, o=o1:风险用户)\nOutput:输出o1\nAction2:get(o1)"
            },
            {
                "Action": "A溃坝事件对那些公司产生了影响",
                "answer": "Step1:查询A溃坝事件引起的公司事件\nAction1:get_spo(s=s1:产业链事件[A溃坝事件], p=p1:导致, o=o1:公司事件)\nOutput:输出o1\nAction2:get(o1)"
                }
        ],"""
    dmy_case_zh_v1 = """"cases": [
            {
                "query": "除了短沟道效应影响外，为什么在顶栅IGZO TFT中，随着沟道长度L的变小，TFT的阈值电压会变负？",
                "answer": "Step1: 查询顶栅IGZO TFT的阈值电压与沟道长度L的关系\nAction1: get_spo(s=s1:半导体器件[顶栅IGZO TFT], p=p1:阈值电压, o=o1:电压值)\nStep2: 查询沟道长度L对阈值电压的影响\nAction2: get_spo(s=s1, p=p2:沟道长度, o=o2:L值)\nStep3: 分析除了短沟道效应外的其他因素\nAction3: get_spo(s=s1, p=p3:其他影响因素, o=o3)\nStep4: 输出分析结果\nAction4: Output(o1, o2, o3)"
            }
    ],"""
    hy_case_zh_v1 = """"cases": [
                    {
                        "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
                        "answer": "Step1: 识别底栅结构器件类型及其特点\nAction1: get_spo(s=s1:Device, p=p1:HasCharacteristic, o=o1:Property)\nStep2: 查找底栅结构与响应速度的关系\nAction2: get_spo(s=o1, p=p2:RelatedTo, o=o2:ResponseSpeed)\nStep3: 解释为何底栅结构影响响应速度\nAction3: get_spo(s=o2, p=p3:InfluencedBy, o=o3:Factor)"
                    }
            ],"""
    template_zh = f"""
{{
    {instruct_zh}
    {hy_case_zh_v1}
    "output_format": "only output `Step`, `Action` and `Output` content",
    "query": "$question"
}}   
    """
    # The parameters in parentheses are optional parameters that are included in [], and mandatory parameters that are not included in []
    instruct_en = """    "instruction": "Please convert the query to the required output format based on the function_description and example cases.",
    "function_description": "functionName is operator name;the function format is functionName(arg_name1=arg_value1,[args_name2=arg_value2, args_name3=arg_value3]),括号中为参数，被[]包含的参数为可选参数，未被[]包含的为必选参数",
    "function": [
      {
          "functionName": "get_spo",
          "function_declaration": "get_spo(s=s_alias:entity_type[entity_name], p=p_alias:edge_type, o=o_alias:entity_type[entity_name])",
          "description": "Find SPO information. 's' represents the subject, 'o' represents the object, and they are denoted as variable_name:entity_type[entity_name]. The entity name is an optional parameter and should be provided when there is a specific entity to query. 'p' represents the predicate, which can be a relationship or attribute, denoted as variable_name:edge_type_or_attribute_type. Each variable is assigned a unique variable name, which is used for reference in subsequent mentions. Note that 's', 'p', and 'o' should not appear repeatedly within the same expression; only one set of SPO should be queried at a time. When a variable is a reference to a previously mentioned variable name, the variable name must match the previously mentioned variable name, and only the variable name needs to be provided; the entity type is only given when it is first introduced."
      },
      {
          "functionName": "count",
          "function_declaration": "count(alias)->count_alias",
          "description": "Count the number of nodes. The parameter should be a specified set of nodes to count, and it can only be variable names that appear in the get_spo query. The variable name 'count_alias' represents the counting result, which must be of int type, and this variable name can be used for reference in subsequent mentions."
      },
      {
          "functionName": "sum",
          "function_declaration": "sum(alias, num1, num2, ...)->sum_alias",
          "description": "Calculate the sum of data. The parameter should be a specified set to sum, which can be either numbers or variable names mentioned earlier, and its content must be of numeric type. The variable name 'sum_alias' represents the result of the calculation, which must be of numeric type, and this variable name can be used for reference in subsequent mentions."      },
      {
          "functionName": "sort",
          "function_declaration": "sort(set=alias, orderby=o_alias or count_alias or sum_alias, direction=min or max, limit=N)",
          "description": "Sort a set of nodes. The 'set' parameter specifies the set of nodes to be sorted and can only be variable names that appear in the get_spo query. The 'orderby' parameter specifies the basis for sorting, which can be the relationship or attribute name of the nodes. If it has been mentioned earlier, an alias should be used. The 'direction' parameter specifies the sorting order, which can only be 'min' (ascending) or 'max' (descending). The 'limit' parameter specifies the limit on the number of output results and must be of int type. The sorted result can be used as the final output."      },
      {
          "functionName": "compare",
          "function_declaration": "compare(set=[alias1, alias2, ...], op=min|max)",
          "description": "Compare nodes or numeric values. The 'set' parameter specifies the set of nodes or values to be compared, which can be variable names that appear in the get_spo query or constants. The 'op' parameter specifies the comparison operation: 'min' to find the smallest and 'max' to find the largest."
      },
      {
          "functionName": "get",
          "function_declaration": "get(alias)",
          "description": "Return the information represented by a specified alias. This can be an entity, a relationship path, or an attribute value obtained in the get_spo query. It can be used as the final output result."
      }
    ],"""
    default_case_en = """"cases": [
        {
            "query": "Which sports team for which Cristiano Ronaldo played in 2011 was founded last ?",
            "answer": "Step1:Which Sports Teams Cristiano Ronaldo Played for in 2011 ?\nAction1:get_spo(s=s1:Player[Cristiano Ronaldo],p=p1:PlayedForIn2011Year,o=o1:SportsTeam)\nStep2:In which year were these teams established ?\nAction2:get_spo(s=o1,p=p2:FoundationYear,o=o2:Year)\nStep3:Which team was founded last ?\nAction3:sort(set=o1, orderby=o2, direction=max, limit=1)"
        },
        {
            "query": "Who was the first president of the association which published Journal of Psychotherapy Integration?",
            "answer": "Step1:Which association that publishes the Journal of Psychotherapy Integration ?\nAction1:Journal(s=s1:Player[Psychotherapy Integration],p=p1:Publish,o=o1:Association)\nStep2:Who was the first president of that specific association?\nAction2:get_spo(s=o1,p=p2:FirstPresident,o=o2:Person)"
        },
        {
            "query": "When did the state where Pocahontas Mounds is located become part of the United States?",
            "answer": "Step1:Which State Where Pocahontas Mounds is Located ?\nAction1:get_spo(s=s1:HistoricalSite[Pocahontas Mounds], p=p1:LocatedIn, o=o1:State)\nStep2:When did this state become a part of the United States ？\nAction2:get_spo(s=o1, p=p2:YearOfBecamingPartofTheUnitedStates, o=o2:Date)"
        },
        {
            "query": "Which of the two tornado outbreaks killed the most people?",
            "answer": "Step1:Which is the first tornado outbreaks ?\nAction1:get_spo(s=s1:Event[Tornado Outbreak], p=p1:TheFirst, o=o1:Event)\nStep2:Which is the second tornado outbreaks ?\nAction2:get_spo(s=s2:Event[Tornado Outbreak], p=p2:TheSecond, o=o2:Event)\nStep3:How many people died in the first tornado outbreak ?\nAction3:get_spo(s=s1, p=p3:KilledPeopleNumber, o=o3:Number)\nStep4:How many people died in the second tornado outbreak ?\nAction4:get_spo(s=s2, p=p4:KilledPeopleNumber, o=o4:Number)\nStep5:To compare the death toll between two tornado outbreaks to determine which one had more fatalities.\nAction5:compare(set=[o3,o4], op=max)"
        }
    ],"""
    # v1 客观题93% 主观题9/17
    hy_case_en_v1 = """"cases": [
                            {
                                "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
                                "answer": "Step1:What is the parasitic capacitance of top-gate structure IGZO?\nAction1:get_spo(s=s1:IGZO, p=p1:ParasiticCapacitance, o=o1:Value, p2:TopGateStructure)\nStep2:What is the parasitic capacitance of bottom-gate structure IGZO?\nAction2:get_spo(s=s2:IGZO, p=p2:ParasiticCapacitance, o=o2:Value, p3:BottomGateStructure)\nStep3:Why is the parasitic capacitance lower for top-gate structure compared to bottom-gate structure?\nAction3:get_spo(s=s1, p=p3:Reason, o=o3:Explanation)"
                            },
                            {
                                "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
                                "answer": "Step1: Define the properties of amorphous Si and its mobility\nAction1: get_spo(s=s1:Material[Amorphous Si], p=p1:Mobility, o=o1:Value)\nStep2: Define the properties of amorphous oxides and their mobility\nAction2: get_spo(s=s2:Material[Amorphous Oxides], p=p2:Mobility, o=o2:Value)\nStep3: Compare the mobility values of amorphous Si and oxides\nAction3: compare(set=[o1, o2], op=min)"
                            }
                    ],"""
    dmy_case_en_v3 = """"cases": [
        {
            "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
            "answer": "Step1:What is the parasitic capacitance of top-gate structure IGZO?\nAction1:get_spo(s=s1:IGZO, p=p1:ParasiticCapacitance, o=o1:Value, p2:TopGateStructure)\nStep2:What is the parasitic capacitance of bottom-gate structure IGZO?\nAction2:get_spo(s=s2:IGZO, p=p2:ParasiticCapacitance, o=o2:Value, p3:BottomGateStructure)\nStep3:Why is the parasitic capacitance lower for top-gate structure compared to bottom-gate structure?\nAction3:get_spo(s=s1, p=p3:Reason, o=o3:Explanation)"
        },
        {
            "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
            "answer": "Step1: Define the properties of amorphous Si and its mobility\nAction1: get_spo(s=s1:Material[Amorphous Si], p=p1:Mobility, o=o1:Value)\nStep2: Define the properties of amorphous oxides and their mobility\nAction2: get_spo(s=s2:Material[Amorphous Oxides], p=p2:Mobility, o=o2:Value)\nStep3: Compare the mobility values of amorphous Si and oxides\nAction3: compare(set=[o1, o2], op=min)"
        },
        {
            "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
            "answer": "Step1: Identify the properties of amorphous Si.\nAction1: get_spo(s=s1:Material[Amorphous Si], p=p1:Property, o=o1:Info)\nStep2: What property makes Amorphous Si low.\nAction2: get_spo(s=s1, p=p2:Mobility, o=o2:Value)\nStep3: Identify the properties of amorphous metal oxide.\nAction3: get_spo(s=s2:Material[AmorphousMetalOxide], p=p3:Property, o=o3:Info)\nStep4: What property makes Amorphous metal oxide high.\nAction4: get_spo(s=s2, p=p4:Mobility, o=o4:Value)\nStep5: Output the analysis results.\nAction5: compare(set=[o2, o4], op=max)"
        },
        {
            "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
            "answer": "Step1: What are the factors that cause circuit slow response speed?\nAction1:get_spo(s=s1:Equipment[Circuit], p=p1:SlowResponseFactors, o=o1)\nStep2: What are the properties of bottom-gate structure device?\nAction2:get_spo(s=s2:Device[Bottom-Gate Device], p=p2:Property, o=o2)\nStep3: What is the specific reasons for the bottom-gate structure device affecting circuit response speed?\nAction3:get_spo(s=o2, p=p2:AffectingResponseSpeed, o=o2:Reason)"
         }
    ],"""
    dmy_case_en_v4 = """"cases": [
        {
            "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
            "answer": "Step1:What is the parasitic capacitance of top-gate structure IGZO?\nAction1:get_spo(s=s1:IGZO, p=p1:ParasiticCapacitance, o=o1:Value, p2:TopGateStructure)\nStep2:What is the parasitic capacitance of bottom-gate structure IGZO?\nAction2:get_spo(s=s2:IGZO, p=p2:ParasiticCapacitance, o=o2:Value, p3:BottomGateStructure)\nStep3:Why is the parasitic capacitance lower for top-gate structure compared to bottom-gate structure?\nAction3:get_spo(s=s1, p=p3:Reason, o=o3:Explanation)"
        },
        {
            "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",  
            "answer": "Step1: Define the properties of amorphous Si and its mobility\nAction1: get_spo(s=s1:Material[Amorphous Si], p=p1:Mobility, o=o1:Value)\nStep2: Define the properties of amorphous oxides and their mobility\nAction2: get_spo(s=s2:Material[Amorphous Oxides], p=p2:Mobility, o=o2:Value)\nStep3: Compare the mobility values of amorphous Si and oxides\nAction3: compare(set=[o1, o2], op=min)"
        },
        {
            "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
            "answer": "Step1: What are the factors that cause circuit slow response speed?\nAction1:get_spo(s=s1:Equipment[Circuit], p=p1:SlowResponseFactors, o=o1)\nStep2: What are the properties of bottom-gate structure device?\nAction2:get_spo(s=s2:Device[Bottom-Gate Device], p=p2:Property, o=o2)\nStep3: What is the specific reasons for the bottom-gate structure device affecting circuit response speed?\nAction3:get_spo(s=o2, p=p2:AffectingResponseSpeed, o=o2:Reason)"
         },
         {
            "query": "氧化物薄膜晶体管TFT 相比于非晶硅TFT和LTPS TFT的优势是什么？",
            "answer": "Step1: Identify the properties of metal oxide thin film Transistor\nAction1:get_spo(s=s1:Device[Metal Oxide TFT], p=p1:Property, o=o1)\nStep2: Identify the properties of amorphous silicon thin film Transistor\nAction2:get_spo(s=s2:Device[Amorphous Silicon TFT], p=p2:Property, o=o2)\nStep3: Identify the properties of LTPS thin film Transistor\nAction3:get_spo(s=s3:Device[LTPS TFT], p=p3:Property, o=o3)\nStep4: What are the advantage of the properties of metal oxide thin film Transistor over the properties of amorphous silicon thin film Transistor and the properties of LTPS thin film Transistor\nAction4:compare(set=[o1, o2, o3], op=max)"
         }
    ],"""
    dmy_case_en_v5 = """"cases": [
            {
                "query": "Which sports team for which Cristiano Ronaldo played in 2011 was founded last ?",
                "answer": "Step1:Which Sports Teams Cristiano Ronaldo Played for in 2011 ?\nAction1:get_spo(s=s1:Player[Cristiano Ronaldo],p=p1:PlayedForIn2011Year,o=o1:SportsTeam)\nStep2:In which year were these teams established ?\nAction2:get_spo(s=o1,p=p2:FoundationYear,o=o2:Year)\nStep3:Which team was founded last ?\nAction3:sort(set=o1, orderby=o2, direction=max, limit=1)"
            },
            {
                "query": "Who was the first president of the association which published Journal of Psychotherapy Integration?",
                "answer": "Step1:Which association that publishes the Journal of Psychotherapy Integration ?\nAction1:Journal(s=s1:Player[Psychotherapy Integration],p=p1:Publish,o=o1:Association)\nStep2:Who was the first president of that specific association?\nAction2:get_spo(s=o1,p=p2:FirstPresident,o=o2:Person)"
            },
            {
                "query": "When did the state where Pocahontas Mounds is located become part of the United States?",
                "answer": "Step1:Which State Where Pocahontas Mounds is Located ?\nAction1:get_spo(s=s1:HistoricalSite[Pocahontas Mounds], p=p1:LocatedIn, o=o1:State)\nStep2:When did this state become a part of the United States ？\nAction2:get_spo(s=o1, p=p2:YearOfBecamingPartofTheUnitedStates, o=o2:Date)"
            },
            {
                "query": "Which of the two tornado outbreaks killed the most people?",
                "answer": "Step1:Which is the first tornado outbreaks ?\nAction1:get_spo(s=s1:Event[Tornado Outbreak], p=p1:TheFirst, o=o1:Event)\nStep2:Which is the second tornado outbreaks ?\nAction2:get_spo(s=s2:Event[Tornado Outbreak], p=p2:TheSecond, o=o2:Event)\nStep3:How many people died in the first tornado outbreak ?\nAction3:get_spo(s=s1, p=p3:KilledPeopleNumber, o=o3:Number)\nStep4:How many people died in the second tornado outbreak ?\nAction4:get_spo(s=s2, p=p4:KilledPeopleNumber, o=o4:Number)\nStep5:To compare the death toll between two tornado outbreaks to determine which one had more fatalities.\nAction5:compare(set=[o3,o4], op=max)"
            },
            {
                "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
                "answer": "Step1:What is the parasitic capacitance of top-gate structure IGZO?\nAction1:get_spo(s=s1:IGZO, p=p1:ParasiticCapacitance, o=o1:Value, p2:TopGateStructure)\nStep2:What is the parasitic capacitance of bottom-gate structure IGZO?\nAction2:get_spo(s=s2:IGZO, p=p2:ParasiticCapacitance, o=o2:Value, p3:BottomGateStructure)\nStep3:Why is the parasitic capacitance lower for top-gate structure compared to bottom-gate structure?\nAction3:get_spo(s=s1, p=p3:Reason, o=o3:Explanation)"
            },
            {
                "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",  
                "answer": "Step1: Define the properties of amorphous Si and its mobility\nAction1: get_spo(s=s1:Material[Amorphous Si], p=p1:Mobility, o=o1:Value)\nStep2: Define the properties of amorphous oxides and their mobility\nAction2: get_spo(s=s2:Material[Amorphous Oxides], p=p2:Mobility, o=o2:Value)\nStep3: Compare the mobility values of amorphous Si and oxides\nAction3: compare(set=[o1, o2], op=min)"
            },
            {
                "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
                "answer": "Step1: What are the factors that cause circuit slow response speed?\nAction1:get_spo(s=s1:Equipment[Circuit], p=p1:SlowResponseFactors, o=o1)\nStep2: What are the properties of bottom-gate structure device?\nAction2:get_spo(s=s2:Device[Bottom-Gate Device], p=p2:Property, o=o2)\nStep3: What is the specific reasons for the bottom-gate structure device affecting circuit response speed?\nAction3:get_spo(s=o2, p=p2:AffectingResponseSpeed, o=o2:Reason)"
             },
             {
                "query": "氧化物薄膜晶体管TFT 相比于非晶硅TFT和LTPS TFT的优势是什么？",
                "answer": "Step1: Identify the properties of metal oxide thin film Transistor\nAction1:get_spo(s=s1:Device[Metal Oxide TFT], p=p1:Property, o=o1)\nStep2: Identify the properties of amorphous silicon thin film Transistor\nAction2:get_spo(s=s2:Device[Amorphous Silicon TFT], p=p2:Property, o=o2)\nStep3: Identify the properties of LTPS thin film Transistor\nAction3:get_spo(s=s3:Device[LTPS TFT], p=p3:Property, o=o3)\nStep4: What are the advantage of the properties of metal oxide thin film Transistor over the properties of amorphous silicon thin film Transistor and the properties of LTPS thin film Transistor\nAction4:compare(set=[o1, o2, o3], op=max)"
             }
        ],"""
    template_en = f"""
{{
    {instruct_en}
    {dmy_case_en_v4}    
    "output_format": "Only output words in answer, for examples: `Step`, `Action` content",
    "query": "$question"
}}   
    """

    def __init__(self, language: str):
        super().__init__(language)

    @property
    def template_variables(self) -> List[str]:
        return ["question"]


    def parse_response(self, response: str, **kwargs):
        try:
            logger.debug(f"logic form:{response}")
            _output_string = response.replace("：", ":")
            _output_string = response.strip()
            sub_querys = []
            logic_forms = []
            current_sub_query = ''
            for line in _output_string.split('\n'):
                if line.startswith('Step'):
                    sub_querys_regex = re.search('Step\d+:(.*)', line)
                    if sub_querys_regex is not None:
                        sub_querys.append(sub_querys_regex.group(1))
                        current_sub_query = sub_querys_regex.group(1)
                elif line.startswith('Output'):
                    sub_querys.append("output")
                elif line.startswith('Action'):
                    logic_forms_regex = re.search('Action\d+:(.*)', line)
                    if logic_forms_regex:
                        logic_forms.append(logic_forms_regex.group(1))
                        if len(logic_forms) - len(sub_querys) == 1:
                            sub_querys.append(current_sub_query)
            print('---------------------------------')
            print("拆解出来的sub_querys：",sub_querys)
            print("对应的logic_forms：", logic_forms)
            print('---------------------------------')
            return sub_querys, logic_forms
        except Exception as e:
            logger.warning(f"{response} parse logic form faied {e}", exc_info=True)
            return [], []
