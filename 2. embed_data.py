# Your data is publicly available: OpenAI, Hugging Face

# Your data is private and should remain that way: Azure OpenAI, BedRock (?), Hugging Face

# But you're a menace anyway: OpenAI 

# Supported Embedding Providers and Models
# https://qdrant.tech/documentation/embeddings/#supported-embedding-providers--models

from langchain_openai import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from openai import OpenAI
import os

OpenAIClient = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    organization=os.getenv('OPENAI_ORG')
  )
# loader = DirectoryLoader("./sample_files", glob="./*.txt", show_progress=True)
# data = loader.load()

embeddings = OpenAIEmbeddings(
    openai_api_key=key_param.openai_api_key, organization=key_param.openai_org_id)

def generate_embedding(text: str) -> list[float]:
  response = OpenAIClient.embeddings.create(model="text-embedding-ada-002", input=text)
  return response.data[0].embedding

print(generate_embedding("atherosclerosis"))

# for doc in collection.find({'example_embedding': {"$exists": False}}):
#     print(doc)
#     doc['example_embedding'] = generate_embedding(doc['example'])
#     collection.replace_one({'_id': doc['_id']}, doc)

