from typing import Iterable

from unstructured.documents.elements import Element
from unstructured.partition.pdf import partition_pdf
from unstructured.partition.utils.constants import PartitionStrategy
from unstructured.staging.base import convert_to_text, elements_to_json


def pdf_file(pdf: str) -> list[Element]:
    data = partition_pdf(pdf, languages=["en"], strategy=PartitionStrategy.FAST)

    return data


def unstructured_element_to_json(el: Iterable[Element]) -> str:
    return elements_to_json(el)


def unstructured_element_to_text(el: Iterable[Element]) -> str:
    return convert_to_text(el)
