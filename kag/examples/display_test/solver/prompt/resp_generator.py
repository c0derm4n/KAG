import re
from string import Template
from typing import List
import logging

from kag.common.base.prompt_op import PromptOp

logger = logging.getLogger(__name__)


class RespGenerator(PromptOp):
    template_zh = "基于给定的引用信息完整回答问题。" \
                  "\n给定的引用信息：'$memory'\n问题：'$instruction'"
    template_en = "Answer the question completely based on the given reference." \
                 "\nThe following are given reference:'$memory'\nQuestion: '$instruction'"
    template_zh_plus = '''[角色]
你是一名半导体显示技术专家，充分掌握半导体显示技术的复杂概念和细节，擅长对专业知识进行解答。


[知识]
""""""
'$memory'
""""""


[问题]
'$instruction'


[要求]
0. 用中文回答
1. [知识]存在对解答[问题]无关的内容，你需要对解答[问题]有效的内容进行提取和理解。
2. 如果[知识]中未提供足够信息解答[问题]，则要回答需要相关背景知识。
3. [知识]的内容庞杂，你需要把他们逻辑梳理准确，不得出现错误。
4. 根据已有的[知识]，对问题进行详尽的回答，推荐分点回答格式。
5. 对[问题]的解答要准确、无误。缺乏所需信息可以提出疑问。


[回答]
'''

    template_en_plus = '''[Role]
    You are an expert in semiconductor display technology, fully grasping the complex concepts and details of semiconductor display technology, and skilled at answering professional knowledge questions.

    [Knowledge]
    """"""
    '$memory'
    """"""

    [Question]
    '$instruction'

    [Requirements]
    0. Answer in Chinese

    [Knowledge] contains irrelevant content for answering [Question]; you need to extract and understand the content that is effective for answering [Question].
    If [Knowledge] does not provide enough information to answer [Question], then respond that you need relevant background knowledge.
    The content in [Knowledge] is complex; you need to logically organize it accurately without errors.
    Based on the existing [Knowledge], provide a detailed answer to the question, recommending a bullet-point response format.
    The answer to [Question] must be accurate and error-free. If lacking the required information, you may ask questions.
    [Answer]
    '''


    def __init__(self, language: str):
        super().__init__(language)

    @property
    def template_variables(self) -> List[str]:
        return ["memory", "instruction"]

    def parse_response(self, response: str, **kwargs):
        logger.debug('推理器判别:{}'.format(response))
        return response
