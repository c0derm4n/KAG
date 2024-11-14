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

    template_zh = """
    {
        "instruction": "你是命名实体识别的专家。请从输入中提取与模式定义匹配的实体。如果不存在该类型的实体，请返回一个空列表。请以JSON字符串格式回应。你可以参照example进行抽取。",
        "schema": $schema,
        "example": [
            {
                "input": "metal oxide TFT technology has attracted considerable attention because of its high mobility, low temperature capability, good transparency to visible light, and relatively low fabrication cost. The high fabrication cost of poly-Si TFTs can be alleviated by replacing them with metal oxide TFTs because oxide TFTs can be fabricated without intentional crystallization and doping processes. For this reason, metal oxide TFTs have been studied intensively as an alternative to a-Si TFTs for use in advanced AM displays. Nomura et al. explored a new class of amorphous oxide semiconductors based on InGaZnO (IGZO) and reported that high performance transistors (u ~ 8.3 cm2 /Vs) can be fabricated using IGZO thin films deposited at low temperatures, even at room temperature.",
                "output": [
                        {"entity": "metal oxide TFT", "category": "Device"},
                        {"entity": "mobility", "category": "Parameter"},
                        {"entity": "temperature", "category": "Parameter"},
                        {"entity": "transparency", "category": "Parameter"},
                        {"entity": "visible light", "category": "Concept"},
                        {"entity": "fabrication cost", "category": "Finance"},
                        {"entity": "poly-Si TFTs", "category": "Device"},
                        {"entity": "crystallization", "category": "Process"}
            ​           {"entity": "doping ", "category": "Process"}
            ​           {"entity": "a-Si TFTs ", "category": "Device"}
            ​           {"entity": "AM displays ", "category": "Device"}
            ​           {"entity": "Nomura ", "category": "Researcher"}
            ​           {"entity": "amorphous oxide semiconductors ", "category": "Material"}
            ​           {"entity": "InGaZnO ", "category": "Material"}
            ​           {"entity": "IGZO ", "category": "Material"}
            ​           {"entity": "transistors ", "category": "Device"}
            ​           {"entity": "cm2 /Vs", "category": "Unit"}
            ​           {"entity": "IGZO thin films ", "category": "Material"}
            ​           {"entity": "room temperature ", "category": "Concept"}
                    ]
            }
        ],
        "input": "$input"
    }    
        """

    template_en = template_zh

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
