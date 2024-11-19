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

    template_zh = """
{
    "instruction": "您是一位专门从事开放信息提取（OpenIE）的专家。请从input字段的文本中提取任何可能的关系（包括主语、谓语、宾语），并按照JSON格式列出它们，须遵循example字段的示例格式。请注意以下要求：1. 每个三元组应至少包含entity_list实体列表中的一个，但最好是两个命名实体。2. 明确地将代词解析为特定名称，以保持清晰度。",
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
​        ],
​        "output":[
​            ["metal oxide TFT", "has", "high mobility"],
​            ["metal oxide TFT", "has", "low temperature capability"],
​            ["metal oxide TFT", "has", "good transparency to visible light"],
​            ["metal oxide TFT", "has", "relatively low fabrication cost"],
​            ["oxide TFTs", "can be fabricated", "without intentional crystallization and doping processes"],
​            ["metal oxide TFTs", "an alternative to", "a-Si TFTs"],
​            ["metal oxide TFTs", "in", "advanced AM displays"],
​            ["Nomura et al", "explored", "InGaZnO"],
             ["InGaZnO  transistors", "fabricated", "IGZO thin films"],
             ["InGaZnO  transistors", "fabricated", "low temperatures"],
             ["InGaZnO  transistors", "fabricated", "room temperature"]
​        ]
​    }
}    
    """

    template_en = template_zh

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
