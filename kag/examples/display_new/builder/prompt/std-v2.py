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
    template_en = """
{
    "instruction": "The `input` field contains a user provided context. The `named_entities` field contains extracted named entities from the context, which may be unclear abbreviations, aliases, or slang. To eliminate ambiguity, please attempt to provide the official names of these entities based on the context and your own knowledge. Note that entities with the same meaning can only have ONE official name. Please respond in the format of a single JSONArray string without any explanation, as shown in the `output` field of the provided example.",
    "example": [
    {
        "input": "metal oxide TFT technology has attracted considerable attention because of its high mobility, low temperature capability, good transparency to visible light, and relatively low fabrication cost. The high fabrication cost of poly-Si TFTs can be alleviated by replacing them with metal oxide TFTs because oxide TFTs can be fabricated without intentional crystallization and doping processes. For this reason, metal oxide TFTs have been studied intensively as an alternative to a-Si TFTs for use in advanced AM displays. Nomura et al. explored a new class of amorphous oxide semiconductors based on InGaZnO (IGZO) and reported that high performance transistors (u ~ 8.3 cm2 /Vs) can be fabricated using IGZO thin films deposited at low temperatures, even at room temperature.",
        "named_entities": [
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
            {"entity": "transistors", "category": "Device"},
            {"entity": "8.3 cm2 /Vs", "category": "Parameter"},
            {"entity": "cm2 /Vs", "category": "Unit"},
            {"entity": "IGZO thin films ", "category": "Material"},
            {"entity": "room temperature ", "category": "Terminology"}
            ],
        "output": [
            {"entity": "metal oxide TFT", "category": "Device", "official_name": "Metal-Oxide Thin Film Transistor"},
            {"entity": "mobility", "category": "Parameter", "official_name": "mobility"},
            {"entity": "temperature", "category": "Parameter", "official_name": "temperature"},
            {"entity": "transparency", "category": "Parameter", "official_name": "transparency"},
            {"entity": "visible light", "category": "Terminology", "official_name": "visible light"},
            {"entity": "fabrication cost", "category": "Others", "official_name": "fabrication cost"},
            {"entity": "poly-Si TFTs", "category": "Device", "official_name": "Poly silicon Thin Film Transistors"},
            {"entity": "crystallization", "category": "Process", "official_name": "crystallization"},
            {"entity": "doping", "category": "Process", "official_name": "doping"},
            {"entity": "a-Si TFTs", "category": "Device", "official_name": "Amorphous silicon Thin Film Transistor"},
            {"entity": "AM displays", "category": "Device", "official_name": "Active Matrix Displays"},
            {"entity": "Nomura", "category": "Researcher", "official_name": "Nomura"},
            {"entity": "amorphous oxide semiconductors", "category": "Material", "official_name": "amorphous oxide semiconductors"},
            {"entity": "InGaZnO", "category": "Material", "official_name": "Indium Zinc Gallium Oxide"},
            {"entity": "IGZO", "category": "Material", "official_name": "Indium Zinc Gallium Oxide"},
            {"entity": "transistors", "category": "Device", "official_name": "transistors"},
            {"entity": "8.3 cm2 /Vs", "category": "Parameter", "official_name": "8.3 cm2 /Vs"},
            {"entity": "cm2 /Vs", "category": "Unit", "official_name": "cm2 /Vs"},
            {"entity": "IGZO thin films", "category": "Material", "official_name": "Indium Zinc Gallium Oxide thin film"},
            {"entity": "room temperature", "official_name": "room temperature", "category": "Terminology"}
    ]
    },
    {
        "input": "This letter examines the effect of the gate dielectric material on the light-induced bias-temperature instability of an In–Ga–Zn–O (IGZO) thin-film transistor (TFT). After applying positive and negative bias stresses, the SiNx-gated TFT exhibited inferior stability to the SiO2-gated TFT, which was explained by the charge trapping mechanism. However, light illumination under a negative bias stress accelerated the negative displacement of the threshold voltage (Vth) of the SiNx-gated IGZO TFT compared to that of the SiO2-gated TFT. This was attributed to the injection of photocreated hole carriers into the underlying gate dielectric bulk region as well as the hole trapping at the gate/channel interface.\n An IGZO TFT with a PECVD-derived SiO2 gate dielectric exhibited greater bias stability and light-induced bias stability than the device with the SiNx gate dielectric. This phenomenon has been discussed based on a charge trapping mechanism.Therefore, the SiO2-gated IGZO TFTs can be implemented as backplane electronics in the next-generation AM flat panel displays.",
        "named_entities": [
            {"entity": "gate dielectric material", "category": "Material"},
            {"entity": "light-induced bias-temperature instability", "category": "Issue"},
            {"entity": "applying positive and negative bias stresses", "category": "Test"},
            {"entity": "SiNx-gated TFT", "category": "Device"},
            {"entity": "SiO2-gated TFT", "category": "Device"},
            {"entity": "charge trapping mechanism", "category": "Mechanism"},
            {"entity": "light illumination under a negative bias stress", "category": "Process"},
            {"entity": "negative displacement of the threshold voltage (Vth)", "category": "Issue"},
            {"entity": "injection of photocreated hole carriers into the underlying gate dielectric bulk region", "category": "Mechanism"},
            {"entity": "hole trapping at the gate/channel interface", "category": "Mechanism"},
            {"entity": "bias stability", "category": "Parameter"},
            {"entity": "light-induced bias stability", "category": "Parameter"},
            {"entity": "SiO2-gated IGZO TFTs can be implemented as backplane electronics ", "category": "Countermeasure"}
            ],
    "output": [
            {"entity": "gate dielectric material", "category": "Material", "official_name": "gate dielectric material"},
            {"entity": "light-induced bias-temperature instability", "category": "Issue", "official_name": "light-induced bias-temperature instability"},
            {"entity": "applying positive and negative bias stresses", "category": "Test", "official_name": "applying positive and negative bias stresses"},
            {"entity": "SiNx-gated TFT", "category": "Device", "official_name": "Silicon Nitride-gated Thin Film Transistor"}, 
            {"entity": "SiO2-gated TFT", "category": "Device", "official_name": "Silicon Dioxide-gated Thin Film Transistor"}, 
            {"entity": "charge trapping mechanism", "category": "Mechanism", "official_name": "charge trapping mechanism"}, 
            {"entity": "light illumination under a negative bias stress", "category": "Process", "official_name": "light illumination under negative bias stress"}, 
            {"entity": "negative displacement of the threshold voltage (Vth)", "category": "Issue", "official_name": "negative shift of the threshold voltage"}, 
            {"entity": "injection of photocreated hole carriers into the underlying gate dielectric bulk region", "category": "Mechanism", "official_name": "injection of photocreated hole carriers into the underlying gate dielectric bulk region"}, 
            {"entity": "hole trapping at the gate/channel interface", "category": "Mechanism", "official_name": "hole trapping at the gate/channel interface"}, 
            {"entity": "bias stability", "category": "Parameter", "official_name": "bias stability"}, 
            {"entity": "light-induced bias stability", "category": "Parameter", "official_name": "light-induced bias stability"}, 
            {"entity": "SiO2-gated IGZO TFTs can be implemented as backplane electronics", "category": "Countermeasure", "official_name": "Silicon Dioxide-gated IGZO TFTs can be implemented as backplane electronics"}]
    },
    {
    "input": "The TFT fabrication process as follows. First, a 100 nm thick layer molybdenum (Mo) as bottom gate electrode was grown by direct current (DC) sputtering with Inline Sputtering System room temperature produced by Ulvac Inc. and patterned by wet etching on the glass. Next, a 120 nm thick layer SiO2 as gate insulator (GI) was grown by plasma enhanced chemical vapor deposition (PECVD) at 300°C . The ratio of SiH4 and N2O during SiO2 growth is 20:80 sccm. Afterwards, a 40 nm thick layer a-IZO (In:Zn=1:1) as the active channel was grown by direct current (DC) sputtering at room temperature and patterned by wet etching in a diluted HCl solution. The DC power and gas pressure on sputtering a-IZO were 100 W and 0.4 Pa.",
    "named_entities": [
                {"entity": "TFT fabrication process", "category": "Process"},
                {"entity": "100 nm thick layer molybdenum (Mo)", "category": "Material"},
                {"entity": "bottom gate electrode", "category": "Terminology"},
                {"entity": "direct current (DC) sputtering", "category": "Process"},
                {"entity": "Inline Sputtering System", "category": "Equipment"},
                {"entity": "Ulvac Inc.", "category": "Company"},
                {"entity": "wet etching", "category": "Process"},
                {"entity": "glass", "category": "Material"},
                {"entity": "120 nm thick layer SiO2", "category": "Material"},
                {"entity": "gate insulator (GI)", "category": "Terminology"},
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
                ], 
    "output": [
        {"entity": "TFT fabrication process", "category": "Process", "official_name": "TFT fabrication process"},
        {"entity": "100 nm thick layer molybdenum (Mo)", "category": "Material", "official_name": "100 nm thick layer molybdenum"},
        {"entity": "bottom gate electrode", "category": "Terminology", "official_name": "bottom gate electrode"},
        {"entity": "direct current (DC) sputtering", "category": "Process", "official_name": "direct current sputtering"},
        {"entity": "Inline Sputtering System", "category": "Equipment", "official_name": "Inline Sputtering System"},
        {"entity": "Ulvac Inc.", "category": "Company", "official_name": "Ulvac Inc."},
        {"entity": "wet etching", "category": "Process", "official_name": "wet etching"},
        {"entity": "glass", "category": "Material", "official_name": "glass"},
        {"entity": "120 nm thick layer SiO2", "category": "Material", "official_name": "120 nm thick layer silicon dioxide"},
        {"entity": "gate insulator (GI)", "category": "Terminology", "official_name": "gate insulator"},
        {"entity": "plasma enhanced chemical vapor deposition (PECVD)", "category": "Process", "official_name": "plasma enhanced chemical vapor deposition"},
        {"entity": "300°C", "category": "Parameter", "official_name": "300°C"},
        {"entity": "ratio of SiH4 and N2O during SiO2 growth", "category": "Parameter", "official_name": "ratio of SiH4 and N2O during silicon dioxide growth"},
        {"entity": "20:80 sccm", "category": "Parameter", "official_name": "20:80 sccm"},
        {"entity": "40 nm thick layer a-IZO (In:Zn=1:1)", "category": "Material", "official_name": "40 nm thick layer amorphous indium zinc oxide"},
        {"entity": "active channel", "category": "Terminology", "official_name": "active channel"},
        {"entity": "diluted HCl solution", "category": "Material", "official_name": "diluted hydrochloric acid solution"},
        {"entity": "DC power", "category": "Parameter", "official_name": "Direct Current power"},
        {"entity": "gas pressure", "category": "Parameter", "official_name": "gas pressure"},
        {"entity": "a-IZO", "category": "Material", "official_name": "amorphous indium zinc oxide"},
        {"entity": "0.4 Pa", "category": "Parameter", "official_name": "0.4 Pa"},
        {"entity": "100 W", "category": "Parameter", "official_name": "100 W"},
        {"entity": "Pa", "category": "Unit", "official_name": "Pa"},
        {"entity": "W", "category": "Unit", "official_name": "W"}
        ]
    }
    ],
    "input": $input,
    "named_entities": $named_entities,
}"""

    template_zh = """
    {
        "instruction": "你是实体名称官方标识的专家，同时，你是显示领域的专家，深刻理解显示领域的相关知识和概念。input字段包含用户提供的上下文。命名实体字段包含从上下文中提取的命名实体，这些可能是含义不明的缩写、别名或俚语。为了消除歧义，请尝试根据上下文和您自己的知识提供这些实体的官方名称。Official_name中的语种需要和entity中的语种一致，即entity中用中文表示，则Official_name也用中文表示，若entity中用英文表示，则Official_name也用英文表示，且Official_name中不能包含解释词语，即不能出现类似“阈值电压（Vth）”这种形式“中文（英文）”实体名称。请注意，具有相同含义的实体只能有一个官方名称。请按照提供的示例中的输出字段格式，以单个JSONArray字符串形式回复，无需任何解释。",
        "example": {
            "input": "本论文研究了栅极绝缘材料及其制备工艺。由于栅极绝缘层决定着薄膜晶体管的击穿电压、泄漏电流等重要工作参数，因此获得高介电常数、高质量的栅极绝缘层显得极为重要。基于此，我们开发出了阳极氧化 Al2O3 薄膜制备新工艺，在氧化制备过程中使用数控系统对氧化信号进行编程，研制的 Al2O3 薄膜具有高介电常数（~10）、高击穿电场（~6 MV/cm）、低泄漏电流（<10-8 A/cm2）的优点。这种制备方法即避免使用贵重的真空设备，节约了成本，又提高了栅介质薄膜的大面积均一性，十分适合大尺寸AMOLED 显示屏的制作。同时，为了解决栅极 Al 薄膜在高温下容易产生表面小丘的问题，本论文又研制了基于 Al-Nd 和 Al-Ce 合金栅极的阳极氧化 Al2O3，以提高 Al /Al2O3 体系的热稳定性，得到的 Nd:Al2O3 和 Ce:Al2O3 绝缘层在高温下表面平整、膜层致密，完全能够抑制小丘的形成。研究表明，Nd 或 Ce 会扩散进入到半导体内，对 MOTFT 的器件性能产生重要影响。其中，Ce 元素产生电荷陷阱缺陷，严重恶化器件的电学性能；Nd 元素则能抑制氧空位和杂乱的自由电子，改善器件的电学性能。因此，Nd 与金属氧化物半导体具有较好的兼容性，基于阳极氧化 Nd:Al2O3 绝缘层的 MOTFT 在 FPD 产业上有较大的应用潜力。",
            "named_entities": [
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
            "output": [
                {"entity": "栅极绝缘材料", "category": "Material", "official_name": "栅极绝缘材料"},
                {"entity": "栅极绝缘层", "category": "Terminology", "official_name": "栅极绝缘层"},
                {"entity": "薄膜晶体管", "category": "Device", "official_name": "薄膜晶体管"},
                {"entity": "击穿电压", "category": "Parameter", "official_name": "击穿电压"},
                {"entity": "介电常数", "category": "Parameter", "official_name": "介电常数"},
                {"entity": "阳极氧化", "category": "Process", "official_name": "阳极氧化"},
                {"entity": "Al2O3 薄膜", "category": "Material", "official_name": "Al2O3 薄膜"},
                {"entity": "数控系统", "category": "Equipment", "official_name": "数控系统"},
                {"entity": "氧化信号", "category": "Parameter", "official_name": "氧化信号"},
                {"entity": "MV/cm", "category": "Unit", "official_name": "MV/cm"},
                {"entity": "A/cm2", "category": "Unit", "official_name": "A/cm2"},
                {"entity": "真空设备", "category": "Equipment", "official_name": "真空设备"},
                {"entity": "均一性", "category": "Parameter", "official_name": "均一性"},
                {"entity": "AMOLED 显示屏", "category": "Device", "official_name": "AMOLED 显示屏"},
                {"entity": "栅极", "category": "Terminology", "official_name": "栅极"},
                {"entity": "Al 薄膜", "category": "Material", "official_name": "Al 薄膜"},
                {"entity": "cm2 /Vs", "category": "Unit", "official_name": "cm2 /Vs"},
                {"entity": "小丘", "category": "Terminology", "official_name": "小丘"}
                {"entity": "Al-Nd", "category": "Material", "official_name": "Al-Nd"},
                {"entity": "Al-Ce 合金", "category": "Material", "official_name": "Al-Ce 合金"},
                {"entity": "Al2O3", "category": "Material", "official_name": "Al2O3"},
                {"entity": "Al /Al2O3 体系", "category": "Material", "official_name": "Al /Al2O3 体系"},
                {"entity": "Nd:Al2O3", "category": "Material", "official_name": "Nd:Al2O3"},
                {"entity": "Ce:Al2O3", "category": "Material", "official_name": "Ce:Al2O3"},
                {"entity": "Nd", "category": "Material", "official_name": "Nd"},
                {"entity": "半导体", "category": "Material", "official_name": "半导体"},
                {"entity": "MOTFT", "category": "Device", "official_name": "Metal-Oxide Thin Film Transistor"},
                {"entity": "电荷陷阱缺陷", "category": "Terminology", "official_name": "电荷陷阱缺陷"},
                {"entity": "电学性能", "category": "Parameter", "official_name": "电学性能"},
                {"entity": "氧空位", "category": "Terminology", "official_name": "氧空位"},
                {"entity": "自由电子", "category": "Terminology", "official_name": "自由电子"},
                {"entity": "金属氧化物半导体", "category": "Material", "official_name": "金属氧化物半导体"},
                {"entity": "FPD", "category": "Device", "official_name": "Flat Panel Display"}
            ]
        },
        "input": $input,
        "named_entities": $named_entities,
    }    
    ​    """

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
