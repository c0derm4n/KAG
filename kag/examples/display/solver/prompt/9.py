# -*- coding: utf-8 -*-
# @Time : 2024/12/20 9:54 
# @Author : dumingyu
# @File : 7.py 
# @Software: PyCharm
#deepseek
case_en = """"cases": [
         {
            "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
            "answer": "Step1: What is the parasitic capacitance of IGZO with a top-gate structure?\nAction1: get_spo(s=s1:Structure[Top-Gate Structure], p=p1:ParasiticCapacitance, o=o1:Value)\nStep2: What is the parasitic capacitance of IGZO with a bottom-gate structure?\nAction2: get_spo(s=s2:Structure[Bottom-Gate Structure], p=p2:ParasiticCapacitance, o=o2:Value)\nStep3: Compare the parasitic capacitance of the two structures.\nAction3: compare(set=[o1, o2], op=min)"
         },
         {
            "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
            "answer": "Step1: What is the amorphous mobility of silicon?\nAction1: get_spo(s=s1:Material[Silicon], p=p1:AmorphousMobility, o=o1:Value)\nStep2: What is the amorphous mobility of oxides?\nAction2: get_spo(s=s2:Material[Oxides], p=p2:AmorphousMobility, o=o2:Value)\nStep3: Compare the amorphous mobility of silicon and oxides.\nAction3: compare(set=[o1, o2], op=max)"
         },
         {
            "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
            "answer": "Step1: What is the relationship between the threshold voltage and channel length L in a top-gate IGZO TFT?\nAction1: get_spo(s=s1:Structure[Top-Gate IGZO TFT], p=p1:ChannelLength, o=o1:Value)\nAction2: get_spo(s=s1, p=p2:ThresholdVoltage, o=o2:Value)\nStep3: Analyze the effect of decreasing channel length L on the threshold voltage.\nAction3: compare(set=[o1, o2], op=min)"
         },
         {
            "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
            "answer": "Step1: What is the response speed of devices with a bottom-gate structure?\nAction1: get_spo(s=s1:Structure[Bottom-Gate Structure], p=p1:ResponseSpeed, o=o1:Value)\nStep2: What is the response speed of devices with other structures?\nAction2: get_spo(s=s2:Structure[Other Structure], p=p2:ResponseSpeed, o=o2:Value)\nStep3: Compare the response speed of bottom-gate structure and other structures.\nAction3: compare(set=[o1, o2], op=min)"
         }
    ],"""
