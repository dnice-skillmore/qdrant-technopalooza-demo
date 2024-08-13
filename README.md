# Creating a Collection, Embedding Data, and Querying with OpenAI and Qdrant

## Step 1: Install Required Packages
```bash
pip install -r requirements.txt
```
## Step 2: Run the Qdrant Docker image
 ```bash
 # This is with default settings. To run with a custom config file, you must build the Dockerfile.
 docker run -d --name qdrant -p 6333:6333 qdrant/qdrant
```

## Step 3: Find a dataset you want to query
  By default, I have it set to coffee_analysis, and provided a few for choices.
  
  You can also find datasets online like from Kaggle https://www.kaggle.com/datasets?search=food

## Step 4: Set the parameters in `utils/key_params.py`

## Step 5: Setup the collection
 ```bash
python 1.setup_qdrant_collection.py 
```

## Step 6: Embed data and upload
Add the env variables in `.env`
 ```bash
OPENAI_API_KEY="<YOUR_OPENAI_API_KEY>"
OPENAI_ORG='<YOUR_OPENAI_ORG_KEY>'
```

Run 
```bash
python 2.embed_and_upload.py 
```

## Step 7: Start running queries!