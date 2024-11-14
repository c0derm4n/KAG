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


class OpenIEEntitystandardizationdPrompt(PromptOp):

    template_zh = """
{
    "instruction": "input字段包含用户提供的上下文。命名实体字段包含从上下文中提取的命名实体，这些可能是含义不明的缩写、别名或俚语。为了消除歧义，请尝试根据上下文和您自己的知识提供这些实体的官方名称。请注意，具有相同含义的实体只能有一个官方名称。请按照提供的示例中的输出字段格式，以单个JSONArray字符串形式回复，无需任何解释。",
    "example": {
        "input": "metal oxide TFT technology has attracted considerable attention because of its high mobility, low temperature capability, good transparency to visible light, and relatively low fabrication cost. The high fabrication cost of poly-Si TFTs can be alleviated by replacing them with metal oxide TFTs because oxide TFTs can be fabricated without intentional crystallization and doping processes. For this reason, metal oxide TFTs have been studied intensively as an alternative to a-Si TFTs for use in advanced AM displays. Nomura et al. explored a new class of amorphous oxide semiconductors based on InGaZnO (IGZO) and reported that high performance transistors (u ~ 8.3 cm2 /Vs) can be fabricated using IGZO thin films deposited at low temperatures, even at room temperature.",
        "named_entities": [
            {"entity": "metal oxide TFT", "category": "Device"},
            {"entity": "mobility", "category": "Parameter"},
            {"entity": "temperature", "category": "Parameter"},
            {"entity": "transparency", "category": "Parameter"},
            {"entity": "visible light", "category": "Concept"},
            {"entity": "poly-Si TFTs", "category": "Device"},
            {"entity": "crystallization", "category": "Process"}

​            {"entity": "doping ", "category": "Process"}

​            {"entity": "a-Si TFTs ", "category": "Device"}

​            {"entity": "AM displays ", "category": "Device"}

​            {"entity": "Nomura ", "category": "Researcher"}

​            {"entity": "amorphous oxide semiconductors ", "category": "Material"}

​            {"entity": "InGaZnO ", "category": "Material"}

​             {"entity": "IGZO ", "category": "Material"}

​            {"entity": "transistors ", "category": "Device"}

​            {"entity": "cm2 /Vs", "category": "Unit"}

​            {"entity": "IGZO thin films ", "category": "Material"}

​            {"entity": "room temperature ", "category": "Concept"}

​        ],
​        "output": [
​            {"entity": "metal oxide TFT", "category": "Device", "official_name": "metal oxide Thin Film Transistor"},
​            {"entity": "mobility", "category": "Parameter", "official_name": "mobility"},
​            {"entity": "temperature", "category": "Parameter", "official_name": "temperature"},
​            {"entity": "transparency", "category": "Parameter", "official_name": "transparency"},
​            {"entity": "visible light", "category": "Concept", "official_name": "visible light"},
​            {"entity": "poly-Si TFTs", "category": "Device", "official_name": "Poly silicon Thin Film Transistors"},
​            {"entity": "crystallization", "category": "Process", "official_name": "crystallization"}

​			 {"entity": "doping", "category": "Process", "official_name": "doping"}

​             {"entity": "a-Si TFTs", "category": "Device", "official_name": "Amorphous silicon Thin Film Transistor"}

​             {"entity": "AM displays", "category": "Device", "official_name": "Active-Matrix Displays"}

​            {"entity": "Nomura", "category": "Researcher", "official_name": "Nomura"}

​             {"entity": "amorphous oxide semiconductors", "category": "Material", "official_name": "amorphous oxide semiconductors"}

​            {"entity": "InGaZnO", "category": "Material", "official_name": "Indium Zinc Gallium Oxide"}

​           {"entity": "IGZO", "category": "Material", "official_name": "Indium Zinc Gallium Oxide"}

​           {"entity": "transistors", "category": "Device", "official_name": "transistors"}

​           {"entity": "cm2 /Vs", "category": "Unit", "official_name": "Active-Matrix Displays"}

​          {"entity": "IGZO thin films", "category": "Material", "official_name": "Indium Zinc Gallium Oxide thin film"}

​          {"entity": "room temperature", "category": "Concept", "official_name": "room temperature"}

​        ]
​    },
​    "input": $input,
​    "named_entities": $named_entities,
}    
​    """

    template_en = template_zh
    
    def __init__(self, language: Optional[str] = "en"):
        super().__init__(language)
    
    @property
    def template_variables(self) -> List[str]:
        return ["input", "named_entities"]
    
    def parse_response(self, response: str, **kwargs):
    
        rsp = response
        if isinstance(rsp, str):
            rsp = json.loads(rsp)
        if isinstance(rsp, dict) and "output" in rsp:
            rsp = rsp["output"]
        if isinstance(rsp, dict) and "named_entities" in rsp:
            standardized_entity = rsp["named_entities"]
        else:
            standardized_entity = rsp
        entities_with_offical_name = set()
        merged = []
        entities = kwargs.get("named_entities", [])
        for entity in standardized_entity:
            merged.append(entity)
            entities_with_offical_name.add(entity["entity"])
        # in case llm ignores some entities
        for entity in entities:
            if entity["entity"] not in entities_with_offical_name:
                entity["official_name"] = entity["entity"]
                merged.append(entity)
        return merged
