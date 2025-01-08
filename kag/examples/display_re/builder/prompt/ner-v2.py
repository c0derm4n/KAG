# -*- coding: utf-8 -*-
# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.

import json
from string import Template
from typing import List, Optional

from kag.common.base.prompt_op import PromptOp
from knext.schema.client import SchemaClient


class OpenIENERPrompt(PromptOp):

    template_en = """
    {
        "instruction": "You're a very effective entity extraction system. Please extract all the entities that are important for knowledge build and question, along with type, category and a brief description of the entity. The description of the entity is based on your OWN KNOWLEDGE AND UNDERSTANDING and does not need to be limited to the context. the entity's category belongs taxonomically to one of the items defined by schema, please also output the category. Note: Type refers to a specific, well-defined classification, such as Professor, Actor, while category is a broader group or class that may contain more than one type, such as Person, Works. Return an empty list if the entity type does not exist. Please respond in the format of a JSON string.You can refer to the example for extraction.",
        "schema": $schema,
        "example": [
            {
                "input": "metal oxide TFT technology has attracted considerable attention because of its high mobility, low temperature capability, good transparency to visible light, and relatively low fabrication cost. The high fabrication cost of poly-Si TFTs can be alleviated by replacing them with metal oxide TFTs because oxide TFTs can be fabricated without intentional crystallization and doping processes. For this reason, metal oxide TFTs have been studied intensively as an alternative to a-Si TFTs for use in advanced AM displays. Nomura et al. explored a new class of amorphous oxide semiconductors based on InGaZnO (IGZO) and reported that high performance transistors (u ~ 8.3 cm2 /Vs) can be fabricated using IGZO thin films deposited at low temperatures, even at room temperature.",
                "output": [
                        {"entity": "metal oxide TFT", "category": "Device"},
                        {"entity": "mobility", "category": "Parameter"},
                        {"entity": "temperature", "category": "Parameter"},
                        {"entity": "transparency", "category": "Parameter"},
                        {"entity": "visible light", "category": "Terminology"},
                        {"entity": "fabrication cost", "category": "Others"},
                        {"entity": "poly-Si TFTs", "category": "Device"},
                        {"entity": "crystallization", "category": "Process"},
                        {"entity": "doping ", "category": "Process"},
                        {"entity": "a-Si TFTs ", "category": "Device"},
                        {"entity": "AM displays ", "category": "Device"},
                        {"entity": "Nomura ", "category": "Researcher"},
                        {"entity": "amorphous oxide semiconductors ", "category": "Material"},
                        {"entity": "InGaZnO ", "category": "Material"},
                        {"entity": "IGZO ", "category": "Material"},
                        {"entity": "transistors ", "category": "Device"},
                        {"entity": "8.3 cm2 /Vs ", "category": "Parameter"},
                        {"entity": "cm2 /Vs", "category": "Unit"},
                        {"entity": "IGZO thin films ", "category": "Material"},
                        {"entity": "room temperature ", "category": "Terminology"}
                    ]
            },
            {
                "input": "This letter examines the effect of the gate dielectric material on the light-induced bias-temperature instability of an In–Ga–Zn–O (IGZO) thin-film transistor (TFT). After applying positive and negative bias stresses, the SiNx-gated TFT exhibited inferior stability to the SiO2-gated TFT, which was explained by the charge trapping mechanism. However, light illumination under a negative bias stress accelerated the negative displacement of the threshold voltage (Vth) of the SiNx-gated IGZO TFT compared to that of the SiO2-gated TFT. This was attributed to the injection of photocreated hole carriers into the underlying gate dielectric bulk region as well as the hole trapping at the gate/channel interface.\n An IGZO TFT with a PECVD-derived SiO2 gate dielectric exhibited greater bias stability and light-induced bias stability than the device with the SiNx gate dielectric. This phenomenon has been discussed based on a charge trapping mechanism.Therefore, the SiO2-gated IGZO TFTs can be implemented as backplane electronics in the next-generation AM flat panel displays.",
                "output": [
                        {"entity": "gate dielectric material", "category": "Material"},
                        {"entity": "light-induced bias-temperature instability", "category": "Issue"},
                        {"entity": "applying positive and negative bias stresses", "category": "Test"},
                        {"entity": "SiNx-gated TFT", "category": "Device"},
                        {"entity": "SiO2-gated TFT", "category": "Device"},
                        {"entity": "charge trapping mechanism", "category": "Mechanism"},
                        {"entity": "light illumination under a negative bias stress", "category": "Process"},
                        {"entity": "negative displacement of the threshold voltage (Vth)", "category": "Issue"}
                        {"entity": "injection of photocreated hole carriers into the underlying gate dielectric bulk region", "category": "Mechanism"},
                        {"entity": " hole trapping at the gate/channel interface", "category": "Mechanism"},
                        {"entity": "bias stability", "category": "Parameter"},
                        {"entity": "light-induced bias stability", "category": "Parameter"},
                        {"entity": "SiO2-gated IGZO TFTs can be implemented as backplane electronics ", "category": "Countermeasure"}
                    ]
            },
            {
                "input": "The TFT fabrication process as follows. First, a 100 nm thick layer molybdenum (Mo) as bottom gate electrode was grown by direct current (DC) sputtering with Inline Sputtering System room temperature produced by Ulvac Inc. and patterned by wet etching on the glass. Next, a 120 nm thick layer SiO2 as gate insulator (GI) was grown by plasma enhanced chemical vapor deposition (PECVD) at 300°C . The ratio of SiH4 and N2O during SiO2 growth is 20:80 sccm. Afterwards, a 40 nm thick layer a-IZO (In:Zn=1:1) as the active channel was grown by direct current (DC) sputtering at room temperature and patterned by wet etching in a diluted HCl solution. The DC power and gas pressure on sputtering a-IZO were 100 W and 0.4 Pa.",
                "output": [
                        {"entity": "TFT fabrication process", "category": "Process"},
                        {"entity": "100 nm thick layer molybdenum (Mo)", "category": "Material"},
                        {"entity": "bottom gate electrode", "category": "Terminology"},
                        {"entity": "direct current (DC) sputtering", "category": "Process"},
                        {"entity": "Inline Sputtering System", "category": "Equipment"},
                        {"entity": "Ulvac Inc.", "category": "Company"},
                        {"entity": "wet etching", "category": "Process"},
                        {"entity": "glass", "category": "Material"},
                        {"entity": "120 nm thick layer SiO2", "category": "Material"},
                        {"entity": "gate insulator (GI) ", "category": "Terminology"}
                        {"entity": "plasma enhanced chemical vapor deposition (PECVD)", "category": "Process"},
                        {"entity": "300°C", "category": "Parameter"},
                        {"entity": "ratio of SiH4 and N2O during SiO2 growth", "category": "Parameter"},
                        {"entity": "20:80 sccm", "category": "Parameter"},
                        {"entity": "40 nm thick layer a-IZO (In:Zn=1:1) ", "category": "Material"},
                        {"entity": "active channel", "category": "Terminology"},
                        {"entity": "diluted HCl solution", "category": "Material"},
                        {"entity": "DC power", "category": "Parameter"},
                        {"entity": "gas pressure", "category": "Parameter"},
                        {"entity": "a-IZO", "category": "Material"},
                        {"entity": "0.4 Pa", "category": "Parameter"},
                        {"entity": "100 W", "category": "Parameter"},
                        {"entity": "Pa", "category": "Unit"},
                        {"entity": "W", "category": "Unit"}
                    ]
            }
        ],
        "input": "$input"
    }    
        """
    template_zh = """
        {
            "instruction": "你是命名实体识别的专家，同时，你是显示领域的专家，深刻理解显示领域的相关知识和概念。请从输入中提取与模式定义匹配的实体，需要把与模式定义匹配的实体全部提取出来。如果不存在该类型的实体，请返回一个空列表。请以JSON字符串格式回应。你可以参照example进行抽取。",
            "schema": $schema,
            "example": [
                {
                    "input": "本论文研究了栅极绝缘材料及其制备工艺。由于栅极绝缘层决定着薄膜晶体管的击穿电压、泄漏电流等重要工作参数，因此获得高介电常数、高质量的栅极绝缘层显得极为重要。基于此，我们开发出了阳极氧化 Al2O3 薄膜制备新工艺，在氧化制备过程中使用数控系统对氧化信号进行编程，研制的 Al2O3 薄膜具有高介电常数（~10）、高击穿电场（~6 MV/cm）、低泄漏电流（<10-8 A/cm2）的优点。这种制备方法即避免使用贵重的真空设备，节约了成本，又提高了栅介质薄膜的大面积均一性，十分适合大尺寸AMOLED 显示屏的制作。同时，为了解决栅极 Al 薄膜在高温下容易产生表面小丘的问题，本论文又研制了基于 Al-Nd 和 Al-Ce 合金栅极的阳极氧化 Al2O3，以提高 Al /Al2O3 体系的热稳定性，得到的 Nd:Al2O3 和 Ce:Al2O3 绝缘层在高温下表面平整、膜层致密，完全能够抑制小丘的形成。研究表明，Nd 或 Ce 会扩散进入到半导体内，对 MOTFT 的器件性能产生重要影响。其中，Ce 元素产生电荷陷阱缺陷，严重恶化器件的电学性能；Nd 元素则能抑制氧空位和杂乱的自由电子，改善器件的电学性能。因此，Nd 与金属氧化物半导体具有较好的兼容性，基于阳极氧化 Nd:Al2O3 绝缘层的 MOTFT 在 FPD 产业上有较大的应用潜力。",
                    "output": [
                            {"entity": "栅极绝缘材料", "category": "Material"},
                            {"entity": "栅极绝缘层", "category": "Terminology"},
                            {"entity": "薄膜晶体管", "category": "Device"},
                            {"entity": "击穿电压", "category": "Parameter"},
                            {"entity": "介电常数", "category": "Parameter"},
                            {"entity": "阳极氧化 ", "category": "Process"},
                            {"entity": "Al2O3 薄膜", "category": "Material"},
                            {"entity": "数控系统 ", "category": "Equipment"},
                            {"entity": "氧化信号 ", "category": "Parameter"},
                            {"entity": "MV/cm ", "category": "Unit"},
                            {"entity": "A/cm2", "category": "Unit"},
                            {"entity": "真空设备", "category": "Equipment"},
                            {"entity": "均一性 ", "category": "Parameter"},
                            {"entity": "AMOLED 显示屏 ", "category": "Device"},
                            {"entity": "栅极", "category": "Terminology"},
                            {"entity": "Al 薄膜", "category": "Material"},
                            {"entity": "cm2 /Vs", "category": "Unit"}
                            {"entity": "小丘", "category": "Terminology"},
                            {"entity": "Al-Nd", "category": "Material"},
                            {"entity": "Al-Ce 合金", "category": "Material"},
                            {"entity": "Al2O3", "category": "Material"},
                            {"entity": "Al /Al2O3 体系", "category": "Material"},
                            {"entity": "Nd:Al2O3", "category": "Material"},
                            {"entity": "Ce:Al2O3", "category": "Material"},
                            {"entity": "Nd", "category": "Material"},
                            {"entity": "半导体", "category": "Material"},
                            {"entity": "MOTFT", "category": "Device"},
                            {"entity": "电荷陷阱缺陷", "category": "Terminology"},
                            {"entity": "电学性能", "category": "Parameter"},
                            {"entity": "氧空位", "category": "Terminology"},
                            {"entity": "自由电子", "category": "Terminology"},
                            {"entity": "金属氧化物半导体", "category": "Material"},
                            {"entity": "FPD", "category": "Device"}
                        ]
                }
            ],
            "input": "$input"
        }
            """

    def __init__(
            self, language: Optional[str] = "en", **kwargs
    ):
        super().__init__(language, **kwargs)
        self.schema = SchemaClient(project_id=self.project_id).extract_types()
        self.template = Template(self.template).safe_substitute(schema=self.schema)

    @property
    def template_variables(self) -> List[str]:
        return ["input"]

    def parse_response(self, response: str, **kwargs):
        rsp = response
        if isinstance(rsp, str):
            rsp = json.loads(rsp)
        if isinstance(rsp, dict) and "output" in rsp:
            rsp = rsp["output"]
        if isinstance(rsp, dict) and "named_entities" in rsp:
            entities = rsp["named_entities"]
        else:
            entities = rsp

        return entities
