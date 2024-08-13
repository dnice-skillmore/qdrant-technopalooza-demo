# We can also use the Qdrant client to extract information about our data

from qdrant_client import QdrantClient
import util.embeddings as embeddings
import util.key_params as key_params

client = QdrantClient(host='localhost', port=6333)

query = "Floral and fruity"

# Embed the query
query_embedding = embeddings.generate_embedding(query)

search_result = client.search(
    collection_name=key_params.COLLECTION_NAME,
    query_vector=query_embedding,
    limit=1
)

for result in search_result:
    print(f"ID: {result.id}, Score: {result.score}, Payload: {result.payload}")