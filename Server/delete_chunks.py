import pinecone

# Load API key and environment
PINECONE_API_KEY = "pcsk_7GMvEr_Pe8fT731qrQTiyVYoobsgRwmGU1PLs5Uz6NjLYaZjGBSuoH3BMDkau9KY1RjFtK"
PINECONE_ENV = "us-east-1-aws"  # v3 format includes provider (e.g., aws)

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
