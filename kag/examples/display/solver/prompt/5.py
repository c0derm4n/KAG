# -*- coding: utf-8 -*-
# @Time : 2024/12/19 16:58 
# @Author : dumingyu
# @File : 5.py 
# @Software: PyCharm

# GPT4
default_case_en_v2 = """"cases": [
         {
            "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
            "answer": "Step1:Identify the parasitic capacitance in top-gate IGZO structure.
Action1:get_spo(s=s1:Structure[TopGateIGZO], p=p1:ParasiticCapacitance, o=o1:Capacitance)
Step2:Identify the parasitic capacitance in bottom-gate IGZO structure.
Action2:get_spo(s=s2:Structure[BottomGateIGZO], p=p2:ParasiticCapacitance, o=o2:Capacitance)
Step3:Compare the parasitic capacitance between top-gate and bottom-gate structures.
Action3:compare(set=[o1, o2], op=min)"
         },
         {
            "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
            "answer": "Step1:Identify the mobility of amorphous silicon.
Action1:get_spo(s=s1:Material[AmorphousSilicon], p=p1:Mobility, o=o1:MobilityValue)
Step2:Identify the mobility of amorphous oxide.
Action2:get_spo(s=s2:Material[AmorphousOxide], p=p2:Mobility, o=o2:MobilityValue)
Step3:Compare the mobility between amorphous silicon and amorphous oxide.
Action3:compare(set=[o1, o2], op=max)"
         },
         {
            "query": "除了短沟道效应影响外，为什么在顶栅IGZO TFT中，随着沟道长度L的变小，TFT的阈值电压会变负？",
            "answer": "Step1:Identify the threshold voltage in top-gate IGZO TFT with varying channel length.
Action1:get_spo(s=s1:Device[TopGateIGZOTFT], p=p1:ThresholdVoltage, o=o1:Voltage)
Step2:Identify the effect of channel length on threshold voltage.
Action2:get_spo(s=s1, p=p2:ChannelLengthEffect, o=o2:Effect)
Step3:Determine the reason for negative shift in threshold voltage.
Action3:get(s=o2)"
         },
         {
            "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
            "answer": "Step1:Identify the response speed of circuits using bottom-gate structure devices.
Action1:get_spo(s=s1:Device[BottomGateStructure], p=p1:ResponseSpeed, o=o1:Speed)
Step2:Identify factors affecting response speed in bottom-gate structure.
Action2:get_spo(s=s1, p=p2:SpeedFactors, o=o2:Factors)
Step3:Determine the reason for slower response speed.
Action3:get(s=o2)"
         }
    ],"""
