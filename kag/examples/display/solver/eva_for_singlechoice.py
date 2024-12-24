import logging
import os
import json
import pandas as pd
from kag.solver.logic.solver_pipeline import SolverPipeline

from datetime import datetime

now = datetime.now()
date_time_str = now.strftime("%Y-%m-%d-%H-%M")

logger = logging.getLogger(__name__)


class DisplayDemo:

    """
    init for kag client
    """

    def __init__(self):
        pass

    def qa(self, query):
        # CA
        resp = SolverPipeline()
        answer, trace_log = resp.run(query)

        return answer,trace_log

    """
        parallel qa from knowledge base
        and getBenchmarks(em, f1, answer_similarity)
    """



if __name__ == "__main__":
    import time
    t0 = time.time()
    file_path = '/data/dmy/KAG/kag/examples/GPT4_生成的子领域客观题(1).xlsx'
    data = pd.read_excel(file_path,sheet_name='V3V4预测正确并集')   # 筛选后  错误集合
    new_col_names = '调试spo-V5'  # 需要指定
    log_list = []
    for index, row in data.iterrows():
        # if index>=50:
        #     continue
        query = row['query']
        line_list = query.split('\n')
        for i,line in enumerate(line_list):
            if '正确答案' in line:
                start_index = i
                break
        question = '\n'.join(line_list[:start_index])
        question = question+'\n'+'上面是一道单选题，请给出正确选项。'
        print(index, question)
        print("===================")
        try:
            demo = DisplayDemo()
            answer, trace_log = demo.qa(question)
            print(f"Question: {question}")
            print(f"Answer: {answer}")
            print(f"TraceLog: {trace_log}")
            log_list.append({'问题': query, 'TraceLog': trace_log})
            data.at[index, new_col_names] = answer
        except:
            print(f"Question: {question}")
            print(f"Answer: ")
            print(f"TraceLog: ")
            log_list.append({'问题': query, 'TraceLog': []})
            data.at[index, new_col_names] = '报错'

    # 保存新的Excel文件
    new_file_path = '小领域-kag客观题测试结果-{}-{}.xlsx'.format(new_col_names,date_time_str)  # 新文件的保存路径
    data.to_excel(new_file_path, index=False)  # 保存时不包含行索引
    print(f"文件已保存至：{new_file_path}")
    # 保存log
    with open('TraceLog-{}.json'.format(date_time_str), 'w', encoding='utf-8') as json_file:
        json.dump(log_list, json_file, ensure_ascii=False, indent=4)
    print("耗时：",time.time()-t0)
    demo = DisplayDemo()
    query = """**问题：  
在金属氧化物薄膜晶体管（TFT）的研究中，引入镓（Ga）到铟锡锌氧化物（ITZO）通道层的目的是为了实现什么？

选项：  
A) 提高场效应迁移率  
B) 扩大能带宽度并减少缺陷  
C) 增加背景载流子浓度  
D) 提高器件的制造成本"""
    answer, trace_log = demo.qa(query)
    print(f"Question: {query}")
    print(f"Answer: {answer}")
    # print(f"TraceLog: {trace_log}")
