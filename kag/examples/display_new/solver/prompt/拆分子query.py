# -*- coding: utf-8 -*-
# @Time : 2024/12/19 15:52 
# @Author : dumingyu
# @File : 拆分子query.py
# @Software: PyCharm

lll = """
阅读文档https://openspg.yuque.com/ndx6g9/0.5/nzsxb8p2nf7kztlz及如下代码：
class LogicFormPlanPrompt(PromptOp):
    instruct_zh = " "instruction": "",
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
    " 

    default_case_zh = " "cases": [
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
        ], "

    template_zh = f "
{{
    {instruct_zh}
    {hy_case_zh_v1}
    "output_format": "only output `Step`, `Action` and `Output` content",
    "query": "$question"
}}   
     "

    instruct_en = "     "instruction": "",
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
    ]," 
    default_case_en = " "cases": [
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
    ]," 
    template_en = f "
{{
    {instruct_en}
    {default_case_en_v2}
    "output_format": "Only output words in answer, for examples: `Step`, `Action` content",
    "query": "$question"
}}   
    " 

理解上述代码中自定义的多个"function"，根据示例default_case_zh和default_case_en，补全如下代码中“此处需要补全”部分内容：

case_en = " "cases": [
         {
            "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
            "answer": "{此处需要补全}"
         },
         {
            "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
            "answer": "{此处需要补全}"
         },
         {
            "query": "为什么在顶栅IGZO TFT中，随着沟道长度L的变小，TFT的阈值电压会变负？",
            "answer": "{此处需要补全}"
         },
         {
            "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
            "answer": "{此处需要补全}"
         }
    ],"""
# ==========kimi============

l =  [
    {
        "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
        "answer": "Step1: Find the parasitic capacitance of top-gate structure IGZO."
                  "Action1: get_spo(s=s1:Material[IGZO], p=p1:ParasiteCapacitance, o=o1:Value, p1:Structure[top-gate])"
                  "Step2: Find the parasitic capacitance of bottom-gate structure IGZO."
                  "Action2: get_spo(s=s2:Material[IGZO], p=p2:ParasiteCapacitance, o=o2:Value, p2:Structure[bottom-gate])"
                  "Step3: Compare the parasitic capacitance values to determine why the top-gate structure has lower capacitance."
                  "Action3: compare(set=[o1, o2], op=min)"
    },
    {
        "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
        "answer": "Step1: Find the mobility of amorphous Si.\nAction1: get_spo(s=s1:Material[Amorphous Si], p=p1:Mobility, o=o1:Value)\n"
                  "Step2: Find the mobility of amorphous oxides.\nAction2: get_spo(s=s2:Material[Amorphous Oxides], p=p2:Mobility, o=o2:Value)\n"
                  "Step3: Compare the mobility values to determine why amorphous Si has lower mobility.\nAction3: compare(set=[o1, o2], op=max)"
    },
    {
        "query": "为什么在顶栅IGZO TFT中，随着沟道长度L的变小，TFT的阈值电压会变负？",
        "answer": "Step1: Find the relationship between threshold voltage and channel length L in top-gate IGZO TFTs.\nAction1: get_spo(s=s1:Device[IGZO TFT], p=p1:ThresholdVoltage, o=o1:Value, p1:ChannelLength[L])\n"
                  "Step2: Identify other factors that affect the threshold voltage besides the short-channel effect.\nAction2: get_spo(s=s1, p=p2:OtherFactors, o=o2:Info)\n"
                  "Step3: Analyze the reasons for the negative threshold voltage shift as the channel length decreases.\nAction3: Output(o2)"
    },
    {
        "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
        "answer": "Step1: Find the properties of bottom-gate structure devices that affect response speed.\nAction1: get_spo(s=s1:Device[Bottom-gate], p=p1:Properties, o=o1:Info)\n"
                  "Step2: Find the relationship between bottom-gate structure and response speed.\nAction2: get_spo(s=s1, p=p2:ResponseSpeed, o=o2:Value)\n"
                  "Step3: Explain why the bottom-gate structure results in slower response speed.\nAction3: get(o1)"
    }
]

# ==========deepseek============
default_case_en_v2 = """"cases": [
         {
            "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
            "answer": "
                Step1:What is the parasitic capacitance of top-gate structure IGZO?
                Action1:get_spo(s=s1:Material[IGZO], p=p1:ParasiticCapacitance, o=o1:Value)
                Step2:What is the parasitic capacitance of bottom-gate structure IGZO?
                Action2:get_spo(s=s2:Material[IGZO], p=p2:ParasiticCapacitance, o=o2:Value)
                Step3:Why is the parasitic capacitance lower for top-gate structure compared to bottom-gate structure?
                Action3:compare(set=[o1, o2], op=min)"
         },
         {
            "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
            "answer": "
                Step1:Define the properties of amorphous Si and its mobility
                Action1:get_spo(s=s1:Material[AmorphousSi], p=p1:Mobility, o=o1:Value)
                Step2:Define the properties of amorphous oxides and their mobility
                Action2:get_spo(s=s2:Material[AmorphousOxides], p=p2:Mobility, o=o2:Value)
                Step3:Compare the mobility values of amorphous Si and oxides
                Action3:compare(set=[o1, o2], op=max)"
         },
         {
            "query": "为什么在顶栅IGZO TFT中，随着沟道长度L的变小，TFT的阈值电压会变负？",
            "answer": "
                Step1:Search for the relationship between the threshold voltage and the channel length L of top-gate IGZO TFTs
                Action1:get_spo(s=s1:Device[IGZOTFT], p=p1:ThresholdVoltage, o=o1:Value)
                Step2:Search for the relationship between negative threshold voltage shift and the shorten channel length L
                Action2:get_spo(s=s1, p=p2:ChannelLength, o=o2:Value)
                Step3:Analyze factors other than short-channel effect
                Action3:get_spo(s=s1, p=p3:OtherFactors, o=o3:Analysis)
                Step4:Output the analysis results
                Action4:get(o3)"
         },
         {
            "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
            "answer": "
                Step1:What are the properties of bottom-gate structure device?
                Action1:get_spo(s=s1:Device[BottomGateStructure], p=p1:Properties, o=o1:Value)
                Step2:Search for the relationship between bottom-gate structure and response speed
                Action2:get_spo(s=s1, p=p2:ResponseSpeed, o=o2:Value)
                Step3:Explain why the bottom-gate structure affects response speed
                Action3:get(o2)"
         }
    ],"""

#===========gpt4
default_case_en_v2 = """"cases": [
         {
            "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
            "answer": "
            Step1: Identify the factors contributing to parasitic capacitance in top-gate IGZO structures.
            Step2: Identify the factors contributing to parasitic capacitance in bottom-gate IGZO structures.
            Step3: Compare the parasitic capacitance between top-gate and bottom-gate structures to determine why the top-gate has lower capacitance."
         },
         {
            "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
            "answer": "
            Step1: Determine the factors affecting the mobility of amorphous silicon.
            Step2: Determine the factors affecting the mobility of amorphous oxides.
            Step3: Compare the mobility characteristics of amorphous silicon and oxides to understand the differences."
         },
         {
            "query": "除了短沟道效应影响外，为什么在顶栅IGZO TFT中，随着沟道长度L的变小，TFT的阈值电压会变负？",
            "answer": "
            Step1: Identify the factors influencing threshold voltage in top-gate IGZO TFTs.
            Step2: Analyze how channel length reduction affects these factors.
            Step3: Explain why these changes lead to a negative shift in threshold voltage."
         },
         {
            "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
            "answer": "
            Step1: Identify the factors affecting circuit response speed in bottom-gate structured devices.
            Step2: Compare these factors with those in other structures.
            Step3: Explain why these factors result in slower response speed for bottom-gate structured devices."
         }
    ],"""


# ==========qwen============
default_case_en_v2 = """"cases": [
         {
            "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
            "answer": "
                Step1:Find the entity of IGZO TFT with top-gate structure.
                Step2:Identify the parasitic capacitance characteristics of the top-gate IGZO TFT.
                Step3:Find the entity of IGZO TFT with bottom-gate structure.
                Step4:Identify the parasitic capacitance characteristics of the bottom-gate IGZO TFT.
                Step5:Compare the parasitic capacitance between top-gate and bottom-gate structures to explain why the former is lower."
             },
         {
            "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
            "answer": "
                Step1:Identify the mobility characteristics of amorphous silicon (a-Si).
                Step2:Identify the mobility characteristics of amorphous oxide semiconductors.
                Step3:Compare the mobility of a-Si with that of amorphous oxides.
                Step4:Explain the reasons for the differences in mobility based on material properties."
             },
         {
            "query": "除了短沟道效应影响外，为什么在顶栅IGZO TFT中，随着沟道长度L的变小，TFT的阈值电压会变负？",
            "answer": "
                Step1:Identify the threshold voltage behavior of top-gate IGZO TFTs as channel length L decreases.
                Step2:Exclude the effects of short-channel phenomena on threshold voltage.
                Step3:Analyze other factors affecting the threshold voltage when L decreases.
                Step4:Explain why the threshold voltage becomes more negative with decreasing L, apart from short-channel effects."
             },
         {
            "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
            "answer": "
                Step1:Identify the response speed characteristics of circuits using bottom-gate structured devices.
                Step2:Analyze the factors that influence the response speed of these circuits.
                Step3:Compare the response speed of bottom-gate circuits with other types of circuits.
                Step4:Conclude why bottom-gate circuits have a slower response speed."
             }
    ],"""
