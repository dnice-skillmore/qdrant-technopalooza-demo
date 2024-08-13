from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams

# Initialize the Qdrant client
client = QdrantClient(host='localhost', port=6333)



COLLECTION_NAME="coffee_reviews"
DIMENSIONS=1536

# Create a collection
client.create_collection(
    collection_name=COLLECTION_NAME,
    # MAKE SURE DIMENSIONS ARE CORRECT
    vectors_config=VectorParams(size=DIMENSIONS, distance="Cosine")
)

print("Collection created successfully!")

