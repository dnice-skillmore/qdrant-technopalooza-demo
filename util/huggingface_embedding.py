#TODO
import os 
import dotenv

dotenv.load_dotenv()
hf_token = os.getenv("HF_TOKEN")
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"


def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        embedding_url,
        headers={
            "Authorization": f"Bearer {hf_token}"
        },
        json={
            "inputs": text
        }
    )

    if response.status_code != 200:
        raise ValueError(f"API request was unsuccessful {response.text}")

    return response.json()