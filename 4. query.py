# We can also use the Qdrant client to extract information about our data

# The Dashboard is a good GUI.

from qdrant_client import QdrantClient

# client = QdrantClient(path="path/to/db")  # Persists changes to disk
# or
client = QdrantClient(":memory:")

search_result = client.query(
    collection_name="demo_collection",
    query_text="This is a query document",
    limit=1
)
print(search_result)