# -*- coding: utf-8 -*-
# @Time : 2024/12/20 9:54 
# @Author : dumingyu
# @File : 7.py 
# @Software: PyCharm
# kimi
case_en = """"cases": [
    {
        "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
        "answer": "Step1: Find the parasitic capacitance of top-gate structure IGZO.\nAction1: get_spo(s=s1:Material[IGZO], p=p1:ParasiteCapacitance, o=o1:Value, p1:Structure[top-gate])\nStep2: Find the parasitic capacitance of bottom-gate structure IGZO.\nAction2: get_spo(s=s2:Material[IGZO], p=p2:ParasiteCapacitance, o=o2:Value, p2:Structure[bottom-gate])\nStep3: Compare the parasitic capacitance values to determine why the top-gate structure has lower capacitance.\nAction3: compare(set=[o1, o2], op=min)"
    },
    {
        "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
        "answer": "Step1: Find the mobility of amorphous Si.\nAction1: get_spo(s=s1:Material[Amorphous Si], p=p1:Mobility, o=o1:Value)\nStep2: Find the mobility of amorphous oxides.\nAction2: get_spo(s=s2:Material[Amorphous Oxides], p=p2:Mobility, o=o2:Value)\nStep3: Compare the mobility values to determine why amorphous Si has lower mobility.\nAction3: compare(set=[o1, o2], op=max)"
    },
    {
        "query": "为什么在顶栅IGZO TFT中，随着沟道长度L的变小，TFT的阈值电压会变负？",
        "answer": "Step1: Find the relationship between threshold voltage and channel length L in top-gate IGZO TFTs.\nAction1: get_spo(s=s1:Device[IGZO TFT], p=p1:ThresholdVoltage, o=o1:Value, p1:ChannelLength[L])\nStep2: Identify other factors that affect the threshold voltage besides the short-channel effect.\nAction2: get_spo(s=s1, p=p2:OtherFactors, o=o2:Info)\nStep3: Analyze the reasons for the negative threshold voltage shift as the channel length decreases.\nAction3: Output(o2)"
    },
    {
        "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
        "answer": "Step1: Find the properties of bottom-gate structure devices that affect response speed.\nAction1: get_spo(s=s1:Device[Bottom-gate], p=p1:Properties, o=o1:Info)\nStep2: Find the relationship between bottom-gate structure and response speed.\nAction2: get_spo(s=s1, p=p2:ResponseSpeed, o=o2:Value)\nStep3: Explain why the bottom-gate structure results in slower response speed.\nAction3: get(o1)"
    }
],"""
