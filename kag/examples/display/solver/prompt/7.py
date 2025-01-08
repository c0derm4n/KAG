# -*- coding: utf-8 -*-
# @Time : 2024/12/20 9:54 
# @Author : dumingyu
# @File : 7.py 
# @Software: PyCharm
#gpt4
case_en = """"cases": [
         {
            "query": "顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？",
            "answer": "Step1:Identify the parasitic capacitance in top-gate IGZO structure.\nAction1:get_spo(s=s1:Device[Top-Gate IGZO], p=p1:ParasiticCapacitance, o=o1:Value)\nStep2:Identify the parasitic capacitance in bottom-gate structure.\nAction2:get_spo(s=s2:Device[Bottom-Gate IGZO], p=p2:ParasiticCapacitance, o=o2:Value)\nStep3:Compare the parasitic capacitance values to determine which is lower.\nAction3:compare(set=[o1, o2], op=min)"
         },
         {
            "query": "为什么si的非晶态迁移率较低，而氧化物的非晶态迁移率较高？",
            "answer": "Step1:Identify the mobility of amorphous silicon.\nAction1:get_spo(s=s1:Material[Amorphous Silicon], p=p1:Mobility, o=o1:Value)\nStep2:Identify the mobility of amorphous oxide.\nAction2:get_spo(s=s2:Material[Amorphous Oxide], p=p2:Mobility, o=o2:Value)\nStep3:Compare the mobility values to understand the difference.\nAction3:compare(set=[o1, o2], op=max)"
         },
         {
            "query": "为什么在顶栅IGZO TFT中，随着沟道长度L的变小，TFT的阈值电压会变负？",
            "answer": "Step1:Identify the threshold voltage in top-gate IGZO TFT with varying channel length L.\nAction1:get_spo(s=s1:Device[TFT], p=p1:ThresholdVoltage, o=o1:Value, p2:ChannelLength, o2:Length)\nStep2:Analyze how the threshold voltage changes as the channel length decreases.\nAction2:sort(set=o1, orderby=o2, direction=min, limit=1)"
         },
         {
            "query": "为什么以底栅结构的器件为元件的电路响应速度较慢？",
            "answer": "Step1:Identify the response speed of circuits using bottom-gate devices.\nAction1:get_spo(s=s1:Circuit[Bottom-Gate Device], p=p1:ResponseSpeed, o=o1:Value)\nStep2:Identify the response speed of circuits using other device structures.\nAction2:get_spo(s=s2:Circuit[Other Device], p=p2:ResponseSpeed, o=o2:Value)\nStep3:Compare the response speeds to determine which is slower.\nAction3:compare(set=[o1, o2], op=min)"
         }
    ],"""
