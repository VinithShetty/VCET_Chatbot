import os
from dotenv import load_dotenv
import pinecone
import time
from sentence_transformers import SentenceTransformer

# Load environment variables from .env file
load_dotenv()

# Load API key and environment from environment variables
PINCONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINCONE_ENV = os.getenv("PINECONE_ENV", "us-east-1-aws")
INDEX_NAME = "vcet-chatbot"

# Initialize Pinecone
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
index = pc.Index(INDEX_NAME)

# Initialize the embedding model (384-dim output)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Example chunks – REPLACE these with your actual chunks
chunks = [
    "This is the first chunk of text.",
    "Another example chunk that will be embedded.",
    "This is the third chunk of data for the chatbot.",
]

# Create vector tuples: (id, vector, metadata)
vectors_to_upsert = []
for i, chunk in enumerate(chunks):
    vector = model.encode(chunk).tolist()  # Convert numpy array to list
    vectors_to_upsert.append((f"vec{i}", vector, {"text": chunk}))

# Upsert into Pinecone
print("Upserting vectors to Pinecone...")
response = index.upsert(vectors=vectors_to_upsert)
print("Upsert response:", response)

# Allow time for index update
time.sleep(2)

# Fetch and display index stats
stats = index.describe_index_stats()
print("\nIndex stats:", stats)

# Display the total number of vectors
index_metadata = pc.describe_index(INDEX_NAME)
print(f"\nNumber of chunks (vectors) in Pinecone: {index_metadata['vector_count']}")
