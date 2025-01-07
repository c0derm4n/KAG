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

    file_path = '/data/dmy/KAG/kag/examples/微软问题&目标切片-0826-kag测试结果-v7.xlsx'
    data = pd.read_excel(file_path, sheet_name='Query&目标切片')
    new_col_names = 'v11-spo-v4-all'  # 需要指定版本 !!!!!!!!!!
    log_list = []
    for index, row in data.iterrows():
        query = row['Query']
        print(index, query)
        print("===================")
        demo = DisplayDemo()
        answer, trace_log = demo.qa(query)
        print(f"Question: {query}")
        print(f"Answer: {answer}")
        print(f"TraceLog: {trace_log}")
        log_list.append({'问题': query, 'TraceLog': trace_log})
        data.at[index, new_col_names] = answer

    # 保存新的Excel文件
    new_file_path = '小领域-kag主观题测试结果{}-{}.xlsx'.format(new_col_names,date_time_str)  # 新文件的保存路径
    data.to_excel(new_file_path, index=False)  # 保存时不包含行索引
    print(f"文件已保存至：{new_file_path}")
    # 保存log
    with open('TraceLog-{}.json'.format(date_time_str), 'w', encoding='utf-8') as json_file:
        json.dump(log_list, json_file, ensure_ascii=False, indent=4)

    # demo = DisplayDemo()
    # query = "高迁氧化物的稳定性为什么比常规igzo的稳定性差"
    # answer, trace_log = demo.qa(query)
    # print(f"Question: {query}")
    # print(f"Answer: {answer}")
    # print(f"TraceLog: {trace_log}")

