from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams

# Initialize the Qdrant client
client = QdrantClient(host='localhost', port=6333)

COLLECTION_NAME = "COFFEE"
# Create a collection

# MAKE SURE DIMENSIONS ARE CORRECT
client.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(size=1536, distance="Cosine")
)

print("Collection created successfully!")

