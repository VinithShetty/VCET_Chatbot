import os
from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
from groq import Groq
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

class RAGChatBot:
    def __init__(self):
        self.groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
        self.index = self.pc.Index("vcet-chatbot")  # Replace with your index name
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.conversation_history = []

    def retrieve_contexts(self, query, top_k=3):
        query_vector = self.embedder.encode(query).tolist()
        results = self.index.query(
            vector=query_vector,
            top_k=top_k,
            include_metadata=True
        )
        contexts = [match['metadata']['text'] for match in results['matches']]
        return contexts

    def generate_response(self, query, contexts):
        context_str = "\n\n".join(contexts)
        history_str = "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.conversation_history[-5:]])
        
        prompt = f"""Conversation History:
{history_str}

Context from knowledge base:
{context_str}

Current Question: {query}
Answer:"""
        
        response = self.groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant with access to a knowledge base."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content

chatbot = RAGChatBot()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_query = data.get("message", "")
    
    if not user_query:
        return jsonify({"error": "Empty message"}), 400
    
    chatbot.conversation_history.append({"role": "user", "content": user_query})
    contexts = chatbot.retrieve_contexts(user_query)
    response = chatbot.generate_response(user_query, contexts)
    chatbot.conversation_history.append({"role": "bot", "content": response})
    
    return jsonify({"response": response})

@app.route('/')
def serve_index():
    return send_from_directory('../chatbot', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../chatbot', path)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

if __name__ == "__main__":
    app.run(debug=True)