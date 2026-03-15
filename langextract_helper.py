import os
import textwrap

from dotenv import load_dotenv
from langextract.data import AnnotatedDocument, ExampleData, Extraction
from langextract.extraction import extract
from langextract.providers.gemini import GeminiLanguageModel
from langextract.providers.ollama import OllamaLanguageModel

load_dotenv()
# 1. Define the prompt and extraction rules
prompt = textwrap.dedent("""\
    Extract name, skills, links,Education,Certifications and projects from the resume.
    Use exact text for extractions.""")

# 2. Provide a high-quality example to guide the model

examples = [
    ExampleData(
        text="Jane Smith Skills: Python GitHub: https://github.com/jane Project: ML chatbot",
        extractions=[
            Extraction(
                extraction_class="name",
                extraction_text="Jane Smith",
                attributes={},
            ),
            Extraction(
                extraction_class="skill",
                extraction_text="Python",
                attributes={},
            ),
            Extraction(
                extraction_class="link",
                extraction_text="https://github.com/jane",
                attributes={"type": "github"},
            ),
            Extraction(
                extraction_class="project",
                extraction_text="ML chatbot",
                attributes={},
            ),
        ],
    )
]


ollama_model = OllamaLanguageModel(
    model_id="glm-5:cloud",
    model_url="https://ollama.com",
    api_key=os.environ["OLLAMA_KEY"],
    fence_output=False,
    use_schema_constraints=False,
    timeout=30,
)
gemini_model = GeminiLanguageModel(
    api_key=os.environ["LANGEXTRACT_API_KEY"],
    timeout=30,
)


def extract_data(data: str) -> list[AnnotatedDocument] | AnnotatedDocument:
    print(f"got this data {data}")
    return extract(
        text_or_documents=data, model=gemini_model, examples=examples
    )
