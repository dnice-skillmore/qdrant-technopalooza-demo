# Using the Qdrant client, we are going to add these collections

# Install that shit
# !pip install 'qdrant-client[fastembed]' --quiet

# Make sure you have your docker container running

import csv
import requests
import json

def upload_items_from_csv(csv_file, api_endpoint):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        x = 2
        for row in reader:
            row_item = {
              "points": [
                  {
                      "id": x,
                      "vector": row['example_embedding'],
                      "payload": {
                          "skill_name": row['skill_name'],
                          "example": row['example']
                      }
                  }
              ]
            }
            # Assuming each row represents an item to be uploaded
            response = requests.put(api_endpoint, json=row_item)
            if response.status_code == 200:
                print("Item uploaded successfully:", row)
            else:
                print("Failed to upload item:", row)
                print(response.text)
            x += 1

# Example usage
csv_file = './embedding_healthcare_skill_examples.csv'
api_endpoint = 'http://localhost:6333/collections/health_skill_examples/points'
upload_items_from_csv(csv_file, api_endpoint)
