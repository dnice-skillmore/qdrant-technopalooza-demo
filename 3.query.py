# We can also use the Qdrant client to extract information about our data

# The Dashboard is a good GUI.

from qdrant_client import QdrantClient
import util.embeddings as embeddings

# client = QdrantClient(path="path/to/db")  # Persists changes to disk
# or
client = QdrantClient(host='localhost', port=6333)

COLLECTION_NAME = "COFFEE"

query = "Floral and fruity"

# Embed the query
query_embedding = embeddings.generate_embedding(query)


search_result = client.search(
    collection_name=COLLECTION_NAME,
    query_vector=query_embedding,
    limit=1
)

# Print the search results
for result in search_result:
    print(f"ID: {result.id}, Score: {result.score}, Payload: {result.payload}")
# print(search_result)