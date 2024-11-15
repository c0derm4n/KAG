import os

from kag.builder.component.reader import DocxReader, TXTReader
from kag.builder.component.splitter import LengthSplitter, OutlineSplitter
from knext.builder.builder_chain_abc import BuilderChainABC
from kag.builder.component.extractor import KAGExtractor
from kag.builder.component.vectorizer.batch_vectorizer import BatchVectorizer
from kag.builder.component.writer import KGWriter
from kag.solver.logic.solver_pipeline import SolverPipeline
import logging
from kag.common.env import init_kag_config

file_path = os.path.dirname(__file__)

suffix_mapping = {
    "docx": DocxReader,
    "txt": TXTReader
}


class KagDemoBuildChain(BuilderChainABC):

    def build(self, **kwargs):
        file_path = kwargs.get("file_path", "a.docx")
        suffix = file_path.split(".")[-1]
        reader = suffix_mapping[suffix]()
        if reader is None:
            raise NotImplementedError
        project_id = int(os.getenv("KAG_PROJECT_ID"))
        vectorizer = BatchVectorizer()
        splitter = LengthSplitter(split_length=2000)
        extractor = KAGExtractor(project_id=project_id)
        writer = KGWriter()

        chain = reader >> splitter>> extractor >> vectorizer >> writer
        return chain


def buildKG(test_file, **kwargs):
    chain = KagDemoBuildChain(file_path=test_file)
    chain.invoke(test_file, max_workers=10)


if __name__ == "__main__":
    test_pdf = os.path.join(file_path, "./data/test.txt")
    buildKG(test_pdf)
