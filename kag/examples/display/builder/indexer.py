import json
import logging
import os
from typing import Type, List


from kag.builder.component.vectorizer.batch_vectorizer import BatchVectorizer
from kag.builder.component import KGWriter
from kag.builder.component.reader.csv_reader import CSVReader
from kag.builder.component.extractor import SPGExtractor, KAGExtractor
from kag.builder.component.mapping.spo_mapping import SPOMapping
from kag.builder.component.splitter import LengthSplitter
from kag.builder.default_chain import DefaultStructuredBuilderChain, DefaultUnstructuredBuilderChain
from kag.common.env import init_kag_config
from knext.builder.builder_chain_abc import BuilderChainABC
from kag.interface.builder.reader_abc import SourceReaderABC
from knext.common.base.runnable import Input, Output
from kag.builder.model.chunk import Chunk
from kag.builder.component.reader import DocxReader, TXTReader


logger = logging.getLogger(__name__)


class DisplayCorpusReader(SourceReaderABC):
    @property
    def input_types(self) -> Type[Input]:
        """The type of input this Runnable object accepts specified as a type annotation."""
        return str

    @property
    def output_types(self) -> Type[Output]:
        """The type of output this Runnable object produces specified as a type annotation."""
        return Chunk



    def get_basename(self, file_name: str):
        base, ext = os.path.splitext(os.path.basename(file_name))
        return base

    def invoke(self, input: str, **kwargs) -> List[Output]:
        id_column = kwargs.get("id_column", "title")
        name_column = kwargs.get("name_column", "title")
        content_column = kwargs.get("content_column", "text")

        if os.path.exists(str(input)):
            with open(input, "r") as f:
                corpusList = json.load(f)
        else:
            corpusList = input
        chunks = []

        for item in corpusList:
            basename, _ = os.path.splitext(os.path.basename(item[id_column]))
            chunk = Chunk(
                id=Chunk.generate_hash_id(item[id_column]),
                name=basename,
                content=item[content_column],
            )
            chunks.append(chunk)
        return chunks


class DisplayBuilderChain(BuilderChainABC):
    def build(self, **kwargs):
        source = DisplayCorpusReader()
        splitter = LengthSplitter(split_length=2000)
        extractor = KAGExtractor()
        vectorizer = BatchVectorizer()
        sink = KGWriter()

        return source >> splitter >> extractor >> vectorizer >> sink


def buildKB(corpusFilePath):
    DisplayBuilderChain().invoke(file_path=corpusFilePath, max_workers=20)

    logger.info(f"\n\nbuildKB successfully for {corpusFilePath}\n\n")



if __name__ == '__main__':
    filePath = "./data/display_corpus_only_zh.json"  # _half1   _only_zh  _zh_clean
    corpusFilePath = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), filePath
    )
    buildKB(corpusFilePath)
