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
from typing import Optional, List

from kag.common.base.prompt_op import PromptOp


class OpenIETriplePrompt(PromptOp):

    template_en = """
{
    "instruction": "You are an expert specializing in carrying out open information extraction (OpenIE). Please extract any possible relations (including subject, predicate, object) from the given text, and list them following the json format {\"triples\": [[\"subject\", \"predicate\",  \"object\"]]}\n. If there are none, do not list them.\n.\n\nPay attention to the following requirements:\n- Each triple should contain at least one, but preferably two, of the named entities in the entity_list.\n- Clearly resolve pronouns to their specific names to maintain clarity.",
    "entity_list": $entity_list,
    "input": "$input",
    "example": {
        "input": "metal oxide TFT technology has attracted considerable attention because of its high mobility, low temperature capability, good transparency to visible light, and relatively low fabrication cost. The high fabrication cost of poly-Si TFTs can be alleviated by replacing them with metal oxide TFTs because oxide TFTs can be fabricated without intentional crystallization and doping processes. For this reason, metal oxide TFTs have been studied intensively as an alternative to a-Si TFTs for use in advanced AM displays. Nomura et al. explored a new class of amorphous oxide semiconductors based on InGaZnO (IGZO) and reported that high performance transistors (u ~ 8.3 cm2 /Vs) can be fabricated using IGZO thin films deposited at low temperatures, even at room temperature.",
        "entity_list": [
            {"entity": "metal oxide TFT", "category": "Device"},
            {"entity": "mobility", "category": "Parameter"},
            {"entity": "temperature", "category": "Parameter"},
            {"entity": "transparency", "category": "Parameter"},
            {"entity": "visible light", "category": "Terminology"},
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
            {"entity": "cm2 /Vs", "category": "Unit"},
            {"entity": "IGZO thin films ", "category": "Material"},
            {"entity": "room temperature ", "category": "Terminology"}
        ],
        "output":[
            ["metal oxide TFT", "has", "high mobility"],
            ["metal oxide TFT", "has", "low temperature capability"],
            ["metal oxide TFT", "has", "good transparency to visible light"],
            ["metal oxide TFT", "has", "relatively low fabrication cost"],
            ["oxide TFTs", "can be fabricated", "without intentional crystallization and doping processes"],
            ["metal oxide TFTs", "an alternative to", "a-Si TFTs"],
            ["metal oxide TFTs", "in", "advanced AM displays"],
            ["Nomura et al", "explored", "InGaZnO"],
            ["InGaZnO  transistors", "fabricated", "IGZO thin films"],
            ["InGaZnO  transistors", "fabricated", "low temperatures"],
            ["InGaZnO  transistors", "fabricated", "room temperature"]
        ]
    }
}    
    """

    template_zh = """
    {
        "instruction": "您是一位专门从事开放信息提取（OpenIE）的专家。同时，你是显示领域的专家，深刻理解显示领域的相关知识和概念。请从input字段的文本中提取任何可能的关系（包括主语、谓语、宾语），并按照JSON格式列出它们，须遵循example字段的示例格式。请注意以下要求：1. 每个三元组应至少包含entity_list实体列表中的一个，但最好是两个命名实体。且三元组数据由主体、谓语、宾语三者组成。2. 明确地将代词解析为特定名称，以保持清晰度。",
        "entity_list": $entity_list,
        "input": "$input",
        "example": {
            "input": "本论文研究了栅极绝缘材料及其制备工艺。由于栅极绝缘层决定着薄膜晶体管的击穿电压、泄漏电流等重要工作参数，因此获得高介电常数、高质量的栅极绝缘层显得极为重要。基于此，我们开发出了阳极氧化 Al2O3 薄膜制备新工艺，在氧化制备过程中使用数控系统对氧化信号进行编程，研制的 Al2O3 薄膜具有高介电常数（~10）、高击穿电场（~6 MV/cm）、低泄漏电流（<10-8 A/cm2）的优点。这种制备方法即避免使用贵重的真空设备，节约了成本，又提高了栅介质薄膜的大面积均一性，十分适合大尺寸AMOLED 显示屏的制作。同时，为了解决栅极 Al 薄膜在高温下容易产生表面小丘的问题，本论文又研制了基于 Al-Nd 和 Al-Ce 合金栅极的阳极氧化 Al2O3，以提高 Al /Al2O3 体系的热稳定性，得到的 Nd:Al2O3 和 Ce:Al2O3 绝缘层在高温下表面平整、膜层致密，完全能够抑制小丘的形成。研究表明，Nd 或 Ce 会扩散进入到半导体内，对 MOTFT 的器件性能产生重要影响。其中，Ce 元素产生电荷陷阱缺陷，严重恶化器件的电学性能；Nd 元素则能抑制氧空位和杂乱的自由电子，改善器件的电学性能。因此，Nd 与金属氧化物半导体具有较好的兼容性，基于阳极氧化 Nd:Al2O3 绝缘层的 MOTFT 在 FPD 产业上有较大的应用潜力。",
            "entity_list": [
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
                {"entity": "cm2 /Vs", "category": "Unit"},
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
            ],
            "output":[
                ["栅极绝缘层", "决定", "决定着薄膜晶体管的击穿电压、泄漏电流等重要工作参数"],
                ["高介电常数、高质量的栅极绝缘层", "显得", "极为重要"],
                ["阳极氧化", "制备", "Al2O3 薄膜"],
                ["数控系统", "编程", "氧化信号"],
                ["Al2O3 薄膜", "具有", "高介电常数（~10）、高击穿电场（~6 MV/cm）、低泄漏电流（<10-8 A/cm2）的优点"],
                ["阳极氧化", "避免使用", "真空设备"],
                ["阳极氧化", "提高", "栅介质薄膜的大面积均一性"],
                ["阳极氧化", "适合", "大尺寸AMOLED 显示屏的制作"],
                ["Al 薄膜", "高温下容易产生", "表面小丘"],
                ["Al-Nd合金栅极制备的阳极氧化 Al2O3", "提高", "Al /Al2O3 体系的热稳定性"],
                ["Al-Ce合金栅极制备的阳极氧化 Al2O3", "提高", "Al /Al2O3 体系的热稳定性"],
                ["Nd:Al2O3绝缘层", "高温下", "表面平整、膜层致密，完全能够抑制小丘的形成"],
                ["Ce:Al2O3 绝缘层", "高温下", "表面平整、膜层致密，完全能够抑制小丘的形成"],
                ["Nd", "扩散到", "半导体"],
                ["Ce", "扩散到", "半导体"],
                ["Ce", "产生", "电荷陷阱缺陷"],
                ["Ce", "恶化", "器件的电学性能"],
                ["Nd", "抑制", "氧空位"],
                ["Nd", "抑制", "自由电子"],
                ["Nd", "改善", "器件的电学性能"],
                ["Nd 与金属氧化物半导体", "具有", "较好的兼容性"]
            ]
        }
    }    
        """

    def __init__(self, language: Optional[str] = "en"):
        super().__init__(language)

    @property
    def template_variables(self) -> List[str]:
        return ["entity_list", "input"]

    def parse_response(self, response: str, **kwargs):
        rsp = response
        if isinstance(rsp, str):
            rsp = json.loads(rsp)
        if isinstance(rsp, dict) and "output" in rsp:
            rsp = rsp["output"]
        if isinstance(rsp, dict) and "triples" in rsp:
            triples = rsp["triples"]
        else:
            triples = rsp

        standardized_triples = []
        for triple in triples:
            if isinstance(triple, list):
                standardized_triples.append(triple)
            elif isinstance(triple, dict):
                s = triple.get("subject")
                p = triple.get("predicate")
                o = triple.get("object")
                if s and p and o:
                    standardized_triples.append([s, p, o])

        return standardized_triples
