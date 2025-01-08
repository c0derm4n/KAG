# -*- coding: utf-8 -*-
# @Time : 2024/12/19 13:57 
# @Author : dumingyu
# @File : 2.py 
# @Software: PyCharm

"""
复杂版 主要是有p2
"""
default_case_en_v2 = """"cases": [
    {
        "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
        "answer": "Step1: What is the parasitic capacitance of top-gate structure IGZO?\nAction1: get_spo(s=s1:Material[IGZO], p=p1:ParasiticCapacitance, o=o1:Value, p1:Structure[Top-gate])\nStep2: What is the parasitic capacitance of bottom-gate structure IGZO?\nAction2: get_spo(s=s2:Material[IGZO], p=p2:ParasiticCapacitance, o=o2:Value, p2:Structure[Bottom-gate])\nStep3: Why is the parasitic capacitance lower for top-gate structure compared to bottom-gate structure?\nAction3: compare(set=[o1, o2], op=min)\nAction4: get(o1)"
    },
    {
        "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
        "answer": "Step1: Define the properties of amorphous Si and its mobility\nAction1: get_spo(s=s1:Material[Amorphous Si], p=p1:Mobility, o=o1:Value)\nStep2: Define the properties of amorphous oxides and their mobility\nAction2: get_spo(s=s2:Material[Amorphous Oxides], p=p2:Mobility, o=o2:Value)\nStep3: Compare the mobility values of amorphous Si and oxides\nAction3: compare(set=[o1, o2], op=max)\nAction4: get(o2)"
    },
    {
        "query": "除了短沟道效应影响外，为什么在顶栅IGZO TFT中，随着沟道长度L的变小，TFT的阈值电压会变负？",
        "answer": "Step1: Search for the relationship between the threshold voltage and the channel length L of top-gate IGZO TFTs\nAction1: get_spo(s=s1:Device[IGZO TFT], p=p1:ThresholdVoltage, o=o1:Value, p1:ChannelLength[L])\nStep2: Search for the relationship between negative threshold voltage shift and the shorten channel length L\nAction2: get_spo(s=s1, p=p2:NegativeVoltageShift, o=o2:Value, p2:ChannelLength[L])\nStep3: Analyze factors other than short-channel effect\nAction3: get_spo(s=s1, p=p3:OtherFactors, o=o3:Info)\nStep4: Output the analysis results\nAction4: Output(o3)"
    },
    {
        "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
        "answer": "Step1: What are the properties of bottom gate structure device ?\nAction1: get_spo(s=s1:Device[Bottom-gate Structure], p=p1:Properties, o=o1:Info)\nStep2: Search for the relationship between bottom-gate structure and response speed\nAction2: get_spo(s=s1, p=p2:ResponseSpeed, o=o2:Value)\nStep3: Explain why the bottom-gate structure affects response speed.\nAction3: get(o1)"
    }
],"""