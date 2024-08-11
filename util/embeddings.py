
from langchain_openai import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

OpenAIClient = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    organization=os.getenv('OPENAI_ORG')
  )

def generate_embedding(text: str) -> list[float]:
  response = OpenAIClient.embeddings.create(model="text-embedding-ada-002", input=text)

  return response.data[0].embedding
