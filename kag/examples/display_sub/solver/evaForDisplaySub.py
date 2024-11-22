import logging
import os

from kag.common.env import init_kag_config
from kag.solver.logic.solver_pipeline import SolverPipeline

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
 #    demo = DisplayDemo()
 #    query_list = ['氧化物半导体层中的H、O含量对电子浓度有什么影响?',
 # '顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？',
 # '在IGZO TFT中，环境气氛中的氧气是如何影响TFT的阈值电压的？',
 # '在IGZO TFT中，进行正栅压应力测试时，为什么以SiOx为钝化层的TFT，其Vth变化量要小于未钝化的TFT？',
 # '顶栅IGZO TFT的难点之一是将SD区域的IGZO进行金属化/导体化，请问下有什么导体化的方式吗？以及它们的机理是什么？',
 # '氧化物半导体TFT可以在制备过程中通过控制氧含量或通过材料元素成分调控氧空位，请问下如果氧化物半导体中氧空位增加，其迁移率一般是如何变化的？为什么会出现这样的结果呢？',
 # '怎么实现短沟道的顶栅氧化物TFT器件且同时避免器件失效？']
 #    answer_list = []
 #    for query in query_list:
 #        answer,trace_log = demo.qa(query)
 #        print(f"Question: {query}")
 #        print(f"Answer: {answer}")
 #        # print(f"TraceLog: {trace_log}")
 #        answer_list.append(answer)
 #    print(answer_list)

    demo = DisplayDemo()
    query = "氧化物半导体TFT可以在制备过程中通过控制氧含量或通过材料元素成分调控氧空位，请问下如果氧化物半导体中氧空位增加，其迁移率一般是如何变化的？为什么会出现这样的结果呢？"
    answer, trace_log = demo.qa(query)
    print(f"Question: {query}")
    print(f"Answer: {answer}")
    print(f"TraceLog: {trace_log}")
