from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams
import util.key_params as key_params
# Initialize the Qdrant client
client = QdrantClient(host='localhost', port=6333)


# Create a collection
client.create_collection(
    collection_name=key_params.COLLECTION_NAME,
    vectors_config=VectorParams(size=key_params.DIMENSIONS, distance="Cosine")
)

print("Collection created successfully!")

