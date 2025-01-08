# -*- coding: utf-8 -*-
# @Time : 2024/12/19 13:57 
# @Author : dumingyu
# @File : 1.py 
# @Software: PyCharm
default_case_en_v2 = """"cases": [
         {
            "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
            "answer": "Step1:What is the parasitic capacitance of top-gate structure IGZO?\nAction1:get_spo(s=s1:IGZO, p=p1:ParasiticCapacitance, o=o1:Value, p2:TopGateStructure)\nStep2:What is the parasitic capacitance of bottom-gate structure IGZO?\nAction2:get_spo(s=s2:IGZO, p=p2:ParasiticCapacitance, o=o2:Value, p3:BottomGateStructure)\nStep3:Why is the parasitic capacitance lower for top-gate structure compared to bottom-gate structure?\nAction3:get_spo(s=s1, p=p3:Reason, o=o3:Explanation)"
         },
         {
            "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
            "answer": "Step1: Define the properties of amorphous Si and its mobility\nAction1: get_spo(s=s1:Material[Amorphous Si], p=p1:Mobility, o=o1:Value)\nStep2: Define the properties of amorphous oxides and their mobility\nAction2: get_spo(s=s2:Material[Amorphous Oxides], p=p2:Mobility, o=o2:Value)\nStep3: Compare the mobility values of amorphous Si and oxides\nAction3: compare(set=[o1, o2], op=min)"
         },
         {
            "query": "除了短沟道效应影响外，为什么在顶栅IGZO TFT中，随着沟道长度L的变小，TFT的阈值电压会变负？",
            "answer": "Step1: Search for the relationship between the threshold voltage and the channel length L of top-gate IGZO TFTs\nAction1: get_spo(s=s1:Semiconductor Device [Top-Gate IGZO TFT], p=p1:threshold voltage, o=o1:Voltage value)\nStep2:  Search for the relationship between negative threshold voltage shift and the shorten channel length L \nAction2: get_spo(s=s1, p=p2:channel length, o=o2:negative threshold voltage shift)\nStep3: Analyze factors other than short-channel effect.\nAction3: get_spo(s=s1, p=p3:other factor, o=o3)\nStep4: Output the analysis results.\nAction4: Output(o1, o2, o3)"
         },
         {
            "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
            "answer": "Step1: What are the properties of bottom-gate structure device \nAction1: get_spo(s=s1:Device, p=p1:HasCharacteristic, o=o1:Property)\nStep2: Search for the relationship between bottom-gate structure and response speed.\nAction2: get_spo(s=o1, p=p2:RelatedTo, o=o2:ResponseSpeed)\nStep3: Explain why the bottom-gate structure affects response speed.\nAction3: get_spo(s=o2, p=p3:InfluencedBy, o=o3:Factor)"
         }
    ],"""