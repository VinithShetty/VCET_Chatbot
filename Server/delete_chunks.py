import os
from dotenv import load_dotenv
import pinecone

# Load environment variables from .env file
load_dotenv()

# Load API key and environment from environment variables
PINCONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINCONE_ENV = os.getenv("PINECONE_ENV", "us-east-1-aws")  # Default if not set

# Initialize Pinecone using the new class method
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

# Connect to the index
index_name = "vcet-chatbot"
index = pc.Index(index_name)

# Delete chunks in batches
total_chunks = 9040
batch_size = 1000

for i in range(0, total_chunks, batch_size):
    ids = [f"chunk_{j}" for j in range(i, min(i + batch_size, total_chunks))]
    index.delete(ids=ids)
    print(f"✅ Deleted chunks {i} to {i + len(ids) - 1}")

print("🎉 All chunks deleted successfully from Pinecone!")
