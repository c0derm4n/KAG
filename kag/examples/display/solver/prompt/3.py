# -*- coding: utf-8 -*-
# @Time : 2024/12/20 13:53 
# @Author : dumingyu
# @File : 3.py 
# @Software: PyCharm

# 人工+kimi
default_case_en_v2 = """"cases": [
    {
        "query": "氧化物薄膜晶体管TFT相比于非晶硅TFT和LTPS TFT的优势是什么？",
        "answer": "Step1: Identify the properties of metal oxide thin film Transistor.\nAction1: get_spo(s=s1:Device[MetalOxideTFT], p=p1:Properties, o=o1:Info)\nStep2: Identify the properties of amorphous silicon thin film Transistor.\nAction2: get_spo(s=s2:Device[AmorphousSiliconTFT], p=p2:Properties, o=o2:Info)\nStep3: Identify the properties of LTPS thin film Transistor.\nAction3: get_spo(s=s3:Device[LTPSTFT], p=p3:Properties, o=o3:Info)\nStep4: What are the advantages of the properties of metal oxide thin film Transistor over the properties of amorphous silicon thin film Transistor and the properties of LTPS thin film Transistor.\nAction4: compare(set=[o1, o2, o3], op=max)\nStep5: Output the analysis results.\nAction5: get(o1)"
    },
    {
        "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
        "answer": "Step1: What are the factors that cause circuit slow response speed.\nAction1: get_spo(s=s1:Material[AmorphousSi], p=p1:Mobility, o=o1:Value)\nStep2: What are the properties of bottom-gate structure device.\nAction2: get_spo(s=s2:Device[BottomGate], p=p2:Properties, o=o2:Info)\nStep3: Determine the specific reasons for the bottom-gate structure affecting response speed.\nAction3: compare(set=[o1], op=min)\nStep4: Output the analysis results.\nAction4: get(o2)"
    },
    {
        "query": "除了短沟道效应影响外，为什么在顶栅IGZO TFT中，随着沟道长度L的变小，TFT的阈值电压会变负？",
        "answer": "Step1: What causes the parasitic capacitance of top-gate IGZO?\nAction1: get_spo(s=s1:Device[IGZOTFT], p=p1:ParasiteCapacitance, o=o1:Value)\nStep2: What makes the parasitic capacitance of top-gate IGZO low?\nAction2: get_spo(s=s1, p=p2:ChannelLength, o=o2:Value)\nStep3: What causes the parasitic capacitance of bottom-gate IGZO?\nAction3: get_spo(s=s2:Device[BottomGateIGZO], p=p3:ParasiteCapacitance, o=o3:Value)\nStep4: What makes the parasitic capacitance of bottom-gate IGZO high?\nAction4: get_spo(s=s2, p=p4:ChannelLength, o=o4:Value)\nStep5: Output the analysis results.\nAction5: get(o1)"
    },
    {
        "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
        "answer": "Step1: Identify the properties of amorphous Si.\nAction1: get_spo(s=s1:Material[AmorphousSi], p=p1:Properties, o=o1:Info)\nStep2: What property makes Amorphous Si low.\nAction2: get_spo(s=s1, p=p2:Mobility, o=o2:Value)\nStep3: Identify the properties of amorphous metal oxide.\nAction3: get_spo(s=s2:Material[AmorphousMetalOxide], p=p3:Properties, o=o3:Info)\nStep4: What property makes Amorphous metal oxide high.\nAction4: get_spo(s=s2, p=p4:Mobility, o=o4:Value)\nStep5: Output the analysis results.\nAction5: compare(set=[o2, o4], op=max)"
    }
],"""