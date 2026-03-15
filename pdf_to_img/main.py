from constants.main import RESUMES_FILES

from .helper import pdf_to_base64_img


def main():
    pdf_to_base64_img(RESUMES_FILES[0])


if __name__ == "__main__":
    main()
