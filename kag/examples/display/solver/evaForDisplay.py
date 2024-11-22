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

#     query_list = """除了短沟道效应影响外，为什么在顶栅IGZO TFT中，随着沟道长度L的变小，TFT的阈值电压会变负？
# 顶栅结构的IGZO的寄生电容为什么相对于底栅结构的寄生电容要低？
# JDI（Japan Display Inc）企业开发的IGO材料的迁移率、PBTS、NBTIS分别是多少？它的制备工艺是怎样的？
# 顶栅IGZO TFT的难点之一是将SD区域的IGZO进行金属化/导体化，请问下有什么导体化的方式吗？以及它们的机理是什么？
# 氧化物半导体TFT可以在制备过程中通过控制氧含量或通过材料元素成分调控氧空位，请问下如果氧化物半导体中氧空位增加，其迁移率一般是如何变化的？为什么会出现这样的结果呢？
# 顶栅IGZO TFT在驱动显示屏时可能会经历长时间的偏压stress，请问如何改善顶栅IGZO的PBTS/PBS，它们的机理是什么?
# IGZO TFT的迁移率一般在10cm2/vs左右，难以应对高刷新率或窄边框等需求，请问有什么可以提升氧化物迁移率的方法吗？
# 怎么实现短沟道的顶栅氧化物TFT器件且同时避免器件失效？
# 基于金属氧化物驱动的OLED显示器件中的柔性封装膜层为什么在高温时会导致金属氧化物阈值电压往负向漂移，有什么改善对策吗？
# 金属氧化物背板在短时间内驱动OLED显示时会出现残影，请问如何在TFT方面改善残影问题？
# 氧化物半导体层中的H、O含量对电子浓度有什么影响?
# 为什么IGZO TFT的Ioff漏电流比a-Si TFT的漏电流低
# 在LCD中，DEMUX（De-multiplex）技术是什么？它有什么优点？
# 在LCD的DEMUX（De-multiplex）技术中，为什么多采用LTPS TFT，而不是IGZO TFT？
# 在IGZO TFT中，环境气氛中的氧气是如何影响TFT的阈值电压的？
# 在IGZO TFT中，进行正栅压应力测试时，为什么以SiOx为钝化层的TFT，其Vth变化量要小于未钝化的TFT？
# 高迁氧化物的稳定性为什么比常规igzo的稳定性差？""".split('\n')
#     answer_list = []
#     for query in query_list:
#         demo = DisplayDemo()
#         try:
#             answer,trace_log = demo.qa(query)
#         except:
#             answer = ''
#             trace_log = ''
#         print(f"Question: {query}")
#         print(f"Answer: {answer}")
#         print(f"TraceLog: {trace_log}")
#         answer_list.append(answer)
#     for line in answer_list:
#         print(line)
#         print('=================')

    demo = DisplayDemo()
    query = "高迁氧化物的稳定性为什么比常规igzo的稳定性差？"
    answer, trace_log = demo.qa(query)
    print(f"Question: {query}")
    print(f"Answer: {answer}")
    print(f"TraceLog: {trace_log}")
