import os
import json
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer

# Load environment variables from .env file
load_dotenv()

# Load API keys from environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV", "us-east-1")  # Default to us-east-1 if not set

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "vcet-chatbot"

# Check if index exists; if not, create it with the correct dimension
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  # Match the dimension of all-MiniLM-L6-v2
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region=PINECONE_ENV)
    )
else:
    # If the index exists, verify its dimension
    index_description = pc.describe_index(index_name)
    existing_dimension = index_description.dimension
    if existing_dimension != 384:
        print(f"Existing index dimension ({existing_dimension}) does not match model dimension (384).")
        print("Deleting and recreating the index...")
        pc.delete_index(index_name)
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region=PINECONE_ENV)
        )

# Connect to the index
index = pc.Index(index_name)

# Load Sentence Transformer Model
model = SentenceTransformer("all-MiniLM-L6-v2")  # Outputs 384-dim embeddings

# Read the combined text
with open("data/extracted.txt", "r", encoding="utf-8") as f:
    text_data = f.read()

# Split text into smaller chunks
chunk_size = 2000  # Adjust based on Pinecone's limits
text_chunks = [text_data[i:i + chunk_size] for i in range(0, len(text_data), chunk_size)]

# Process and upload each chunk
for i, chunk in enumerate(text_chunks):
    try:
        # Generate embeddings
        embedding = model.encode(chunk).tolist()

        # Upload to Pinecone
        index.upsert(vectors=[(f"chunk_{i}", embedding, {"text": chunk})])

        print(f"Uploaded chunk {i+1}/{len(text_chunks)} ✅")
    except Exception as e:
        print(f"Error uploading chunk {i+1}: {e}")

print("Data uploaded to Pinecone successfully! 🎉")