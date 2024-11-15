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


# def buildKB(corpusFilePath):
#     chunk = Chunk(
#                 id="xxx",
#                 name="xxx",
#                 content="""Among TCOs, a promising material is indium zinc tin oxide (IZTO) because of their possibility for use as TCO films with excellent chemical and thermal stability, as well as high electrical conductivity and optical transparency [6,7].\n\nOn the other hands, in general, the wet chemical etching process is simpler than the dry method, and provides a high throughput and low cost. Therefore, wet etching is used to pattern TCO films in display manufacturing [8]. For the application of IZTO semiconductor to flexible TTFT devices, the wet etching behavior must be investigated to evaluate its chemical stability and to explore etchants for use in wet etching, which is an essential subject for the device fabrication using this material. This work is motivated from the fact that wet chemical etching characteristics of IZTO thin films in the aqueous etching solutions conventionally used in TFT industry is yet to be reported. In wet etching process, hydrochloric acid\n(HCl) has been widely used as one of the conventional etchants for patterning of TCO films [9–11].\n\nHence, in this study, we have prepared transparent semiconducting IZTO thin film on polyethylene naphthalate (PEN) substrate by RF-magnetron sputtering method, and investigated their wet chemical etching characteristics in HCl solutions.\n\n## Experimental\n\nThe IZTO thin films were deposited on the PEN (Teijin Dupont Films) substrate covered with hard coating layer, using a RF-magnetron sputtering method, at room temperature with varying O2 fraction in the mixture of Ar and O2. Prior to deposition, the substrates were cleaned with acetone, methanol and de-ionized water for 10 min in an ultrasonic bath. The base pressure in the chamber was adjusted to 1.0  106Torr and the pressure during the deposition was maintained at 3 mTorr regardless of O2 fraction in Ar and O2 gas mixture. The composition of 3 inch sputtering target used in the experiment was In2O3: ZnO: SnO2 ¼ 90: 7: 3 in weight ratio with purity of 99.99%.\n\nThe semiconducting IZTO films were patterned using a conventional photolithographic method. The etching was carried out in hydrochloric acid solutions as a function of etchant concentration and etching temperature. After etching process, the samples were rinsed in deionized water, the photoresist was stripped using acetone and then the films were dried in N2 flow.\n\nThe thickness and etching rates of the films were determined by a surface profiler (KLA Tencor, Alpha-Step IQ). In order to examine the crystallinity of IZTO thin films, x-ray diffraction (XRD, Rigaku, D=MAX-2500) measurement was performed. The XRD diffraction patterns of the films did not contain any peaks attributable to crystal, indicating amorphous state. The electrical properties of IZTO thin films were obtained from the Hall Effect measurement (Ecopia, HMS-3000) by the Van der Pauw technique. Optical transmittance characteristics of the films were measured by means of an ultraviolet-visible spectrophotometer (Otsuka, MCPD-7000) in the visible region. Optical microscope (Olympus, BX51 M) and field emission scanning electron microscope (FE-SEM, JEOL,\nJSM-7000 F) were used to observe the pattern images and etching profiles, respectively.\n\n## Results And Discussion\n\nFigure 1 shows the influence of O2 flow rate in the sputtering deposition on the deposition rate of the IZTO thin films. It is observed that when oxygen flow rate increases, deposition rate of the films decreases gradually. The decrease in the deposition rate with O2 flow rate is caused by the relative reduction of Ar fraction under constant pressure, resulting in lower sputtering yield of the target material.\n\nAlthough the deposition rate is varied with O2 flow rate, by the control of sputtering time, the thickness of the deposited IZTO films is fixed at about 100 nm, which is confirmed by the cross section images of a FE-SEM.\n\nFigure 2 indicates the dependence of electrical properties of IZTO thin films on the oxygen flow rate""",
#             )
#     extractor = KAGExtractor()
#     print(extractor.invoke(chunk))



if __name__ == '__main__':
    filePath = "./data/display_corpus.json"  # en
    filePath = "./data/display_sub_corpus.json" # test
    corpusFilePath = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), filePath
    )
    buildKB(corpusFilePath)
