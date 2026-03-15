import base64

import pymupdf


def pdf_to_base64_img(pdf_path: str) -> str:
    doc = pymupdf.open(pdf_path)
    pix = doc.get_page_pixmap(0)

    return base64.b64encode(pix.tobytes("png")).decode("utf-8")
