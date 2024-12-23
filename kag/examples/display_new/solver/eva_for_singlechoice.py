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
    # file_path = '/data/dmy/KAG/kag/examples/GPT4_生成的子领域客观题(1).xlsx'
    # data = pd.read_excel(file_path,sheet_name='筛选后')   # 筛选后  错误集合
    # new_col_names = 'ans'  # 需要指定
    # log_list = []
    # for index, row in data.iterrows():
    #     # if index>=50:
    #     #     continue
    #     query = row['query']
    #     line_list = query.split('\n')
    #     for i,line in enumerate(line_list):
    #         if '正确答案' in line:
    #             start_index = i
    #             break
    #     question = '\n'.join(line_list[:start_index])
    #     question = question+'\n'+'上面是一道单选题，请给出正确选项。'
    #     print(index, question)
    #     print("===================")
    #     try:
    #         demo = DisplayDemo()
    #         answer, trace_log = demo.qa(question)
    #         print(f"Question: {question}")
    #         print(f"Answer: {answer}")
    #         print(f"TraceLog: {trace_log}")
    #         log_list.append({'问题': query, 'TraceLog': trace_log})
    #         data.at[index, 'new_col_names'] = answer
    #     except:
    #         print(f"Question: {question}")
    #         print(f"Answer: ")
    #         print(f"TraceLog: ")
    #         log_list.append({'问题': query, 'TraceLog': []})
    #         data.at[index, 'new_col_names'] = '报错'
    #
    # # 保存新的Excel文件
    # new_file_path = '小领域-kag客观题测试结果-{}.xlsx'.format(date_time_str)  # 新文件的保存路径
    # data.to_excel(new_file_path, index=False)  # 保存时不包含行索引
    # print(f"文件已保存至：{new_file_path}")
    # # 保存log
    # with open('TraceLog-{}.json'.format(date_time_str), 'w', encoding='utf-8') as json_file:
    #     json.dump(log_list, json_file, ensure_ascii=False, indent=4)

    demo = DisplayDemo()
    query = """问题：在研究IGZO薄膜晶体管（TFTs）中漏电流下降（DCD）现象的过程中，哪种措施有助于减少DCD并改善显示面板的性能？

A) 减少导电通道的长度以增加电场强度  
B) 降低电场强度  
C) 降低退火温度以增加缺陷数量  
D) 增加SiOx钝化层中的氧原子扩散以增加氧缺陷 """
    answer, trace_log = demo.qa(query)
    print(f"Question: {query}")
    print(f"Answer: {answer}")
    print(f"TraceLog: {trace_log}")
