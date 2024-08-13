
import csv
import uuid

import requests
import util.embeddings as embeddings

# BYOD: Bring Your Own Data
# Bunch of datasets online from Kaggle: https://www.kaggle.com/datasets?search=food

file_path = './datasets/coffee_analysis.csv'
COLLECTION_NAME="coffee_reviews"
DIMENSIONS=1536

# 1. Open the CSV file, embed, and upload each row
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)

    # Get the header row
    header = next(csv_reader)

    for row in csv_reader:
        row_embedding = embeddings.generate_embedding(row['desc_1'])

        row_item = {
              "points": [
                  {
                      "id": uuid.uuid4().hex,
                      "vector": row_embedding,
                      "payload": {
                          "name": row['name'],
                          "roaster": row['roaster']
                      }
                  }
              ]
            }
        
        api_endpoint = f"http://localhost:6333/collections/{COLLECTION_NAME}/points"
        response = requests.put(api_endpoint, json=row_item)
        if response.status_code == 200:
            print("Item uploaded successfully:", row)
        else:
            print("Failed to upload item:", row)
            print(response.text)

        # break


