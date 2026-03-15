import os

from dotenv import load_dotenv
from ollama import ChatResponse, Client

load_dotenv()

c: Client = Client(
    host="https://ollama.com",
    headers={"Authorization": "Bearer " + os.environ.get("OLLAMA_KEY", "")},
)


def get_info(base64_image: str) -> None:
    print(f"got this {base64_image}")
    res: ChatResponse = c.chat(
        model="qwen3.5:cloud",
        # model="gemma3:27b-cloud",
        messages=[
            {
                "role": "user",
                "content": "Extract name, education, skills, certifications as JSON.",
                "images": [base64_image],
            }
        ],
    )
    print(res.message)
