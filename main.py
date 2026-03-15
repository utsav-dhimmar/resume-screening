from constants import RESUMES_FILES
from langextract_helper import extract_data
from ollama_models import get_info
from pdf_to_img import pdf_to_base64_img
from pymupdf_helper import extract_text
from unstructured_helper import pdf_file, unstructured_element_to_text


def using_unstructured():
    el = pdf_file(RESUMES_FILES[0])
    txt = unstructured_element_to_text(el)
    print(txt)


def using_pymypdf():
    res = extract_text(RESUMES_FILES[0])
    print(res)
    data = extract_data(res)
    print(data.extractions)


def main():
    res = pdf_to_base64_img(RESUMES_FILES[0])
    # print(res)
    get_info(res)


if __name__ == "__main__":
    main()
