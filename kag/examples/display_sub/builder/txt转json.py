# -*- coding: utf-8 -*-
# @Time : 2024/12/2 10:39 
# @Author : dumingyu
# @File : txt转json.py
# @Software: PyCharm


import os
import json

# dir_path = r"E:\tft子领域_sid2024_待入库_0619\tft_0619（子领域英文）"
dir_path = r"E:\tft子领域_sid2024_待入库_0619\tft_0619（子领域英文）清洗后"
dir_path = r"E:\tft子领域_sid2024_待入库_0619\microsoft_data_derepetition_combine3中可以接受的学位论文清洗后"
# 获取当前目录下所有的txt文件
txt_files = [f for f in os.listdir(dir_path) if f.endswith('.txt')]

# 初始化一个列表来存储每个文件形成的dict
data_list = []

# 遍历每个txt文件
for file_name in txt_files:
    # 读取文件内容
    with open(os.path.join(dir_path,file_name), 'r', encoding='utf-8') as file:
        content = file.read()

    # 创建一个dict，文件名作为title，文件内容作为text
    file_dict = {
        'title': file_name,
        'text': content
    }

    # 将dict添加到列表中
    data_list.append(file_dict)

# 将列表保存为json文件
with open('display_corpus_en_clean.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=4)

print("所有txt文件已读取并保存为JSON文件。")