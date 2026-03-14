import pymupdf


def extract_text(path: str) -> str:
    doc = pymupdf.open(path)
    texts: list[str] = []
    for page in doc:
        texts.append(page.get_text())

    doc.close()
    return "".join(texts)
