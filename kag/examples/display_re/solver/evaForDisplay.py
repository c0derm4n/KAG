import logging
import json
from kag.interface.solver.lf_planner_abc import LFPlannerABC
from kag.solver.implementation.default_lf_planner import DefaultLFPlanner
from kag.solver.implementation.default_kg_retrieval import KGRetrieverByLlm
from kag.solver.implementation.default_reasoner import DefaultReasoner
from kag.solver.implementation.lf_chunk_retriever import LFChunkRetriever
from kag.solver.logic.core_modules.lf_solver import LFSolver
from kag.solver.logic.solver_pipeline import SolverPipeline
logger = logging.getLogger(__name__)
from datetime import datetime

now = datetime.now()
date_time_str = now.strftime("%Y-%m-%d-%H-%M")

import pandas as pd

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



    def qaWithoutLogicForm(self, query):
        # CA
        lf_solver = LFSolver(chunk_retriever=LFChunkRetriever(),
                             kg_retriever=None)
        reasoner = DefaultReasoner(lf_planner=DefaultLFPlanner(), lf_solver=lf_solver)
        resp = SolverPipeline(reasoner=reasoner)
        answer, trace_log = resp.run(query)
        logger.info(f"\n\nso the answer for '{query}' is: {answer}\n\n")
        return answer, trace_log



if __name__ == "__main__":
    # demo = DisplayDemo()
    # query = "高迁氧化物的稳定性为什么比常规igzo的稳定性差"
    # answer, trace_log = demo.qa(query)
    # print(f"Question: {query}")
    # print(f"Answer: {answer}")
    # print(f"TraceLog: {trace_log}")

    file_path = '/data/dmy/KAG/kag/examples/微软问题&目标切片-0826-kag测试结果-v7.xlsx'
    data = pd.read_excel(file_path, sheet_name='Query&目标切片')
    new_col_names = 'V8-3'  # 需要指定版本 !!!!!!!!!!
    log_list = []
    for index, row in data.iterrows():
        if index >= 17:
            continue
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