import logging
import os
import json
import pandas as pd
from kag.solver.logic.solver_pipeline import SolverPipeline

from datetime import datetime

import time

t0 = time.time()
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

        return answer, trace_log

    """
        parallel qa from knowledge base
        and getBenchmarks(em, f1, answer_similarity)
    """


if __name__ == "__main__":
    # 默认是0：单例测试  改成1：整体测试
    flag = 1
    if flag:
        file_path = '/data/dmy/KAG/kag/examples/GPT4_生成的子领域客观题(1).xlsx'
        data = pd.read_excel(file_path, sheet_name='筛选后')  # 筛选后  错误集合
        new_col_names = 'spo-v5'  # 需要指定
        log_list = []
        for index, row in data.iterrows():
            # if index>=50:
            #     continue
            query = row['query']
            line_list = query.split('\n')
            for i, line in enumerate(line_list):
                if '正确答案' in line:
                    start_index = i
                    break
            question = '\n'.join(line_list[:start_index])
            question = question + '\n' + '上面是一道单选题，请给出正确选项。'
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
        new_file_path = '小领域-kag客观题测试结果-{}-{}.xlsx'.format(new_col_names, date_time_str)  # 新文件的保存路径
        data.to_excel(new_file_path, index=False)  # 保存时不包含行索引
        print(f"文件已保存至：{new_file_path}")
        # 保存log
        with open('TraceLog-{}.json'.format(date_time_str), 'w', encoding='utf-8') as json_file:
            json.dump(log_list, json_file, ensure_ascii=False, indent=4)
        print("耗时：", time.time() - t0)

    else:
        demo = DisplayDemo()
        query = """**问题:** 在半导体显示领域中，氢化多晶In–Ga–O (IGO:H)薄膜晶体管（TFT）的最大场效应迁移率（µFE）是多少？

    **选项:**
    A) 10 cm²/Vs  
    B) 50.6 cm²/Vs  
    C) 100 cm²/Vs  
    D) 160 cm²/Vs"""
        answer, trace_log = demo.qa(query+'\n' + '上面是一道单选题，请给出正确选项。')
        print(f"Question: {query}")
        print(f"Answer: {answer}")

