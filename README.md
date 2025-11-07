# VCET Chatbot 🤖

An intelligent RAG (Retrieval-Augmented Generation) chatbot built with Flask, Pinecone, and Groq AI, featuring a modern web interface with voice interaction capabilities.

## 🌟 Features

- **RAG Architecture**: Combines vector database retrieval with LLM generation for accurate, context-aware responses
- **Voice Interaction**: Built-in speech recognition and text-to-speech capabilities
- **Real-time Chat**: Interactive web interface with smooth animations and modern UI
- **Conversation Memory**: Maintains conversation history for contextual responses
- **Vector Search**: Efficient semantic search using Pinecone vector database
- **Fast LLM Inference**: Powered by Groq's high-performance LLM API

## 🏗️ Architecture

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   Frontend  │─────▶│ Flask Server │─────▶│   Groq AI   │
│  (HTML/JS)  │◀─────│  (RAG Chain) │◀─────│    (LLM)    │
└─────────────┘      └──────┬───────┘      └─────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │   Pinecone   │
                     │ Vector Store │
                     └──────────────┘
```

## 📁 Project Structure

```
VCET_Chatbot/
├── chatbot/                    # Frontend files
│   ├── index.html             # Main chatbot interface
│   ├── style.css              # Styling (integrated in HTML)
│   ├── main.js                # JavaScript logic (integrated in HTML)
│   └── chatbot.png            # Chatbot avatar image
├── Server/                     # Backend files
│   ├── rag_chain.py           # Flask server with RAG implementation
│   ├── vector_embedding.py    # Script to create and upload embeddings
│   ├── check_chunks.py        # Utility to verify stored chunks
│   ├── delete_chunks.py       # Utility to manage vector database
│   ├── to activate venv.txt   # Virtual environment activation guide
│   └── data/
│       ├── cleaned_text.txt   # Cleaned text data
│       └── extracted.txt      # Raw extracted text data
├── .gitignore                 # Git ignore rules
└── README.md                  # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js (optional, for development server)
- Groq API key
- Pinecone API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/VinithShetty/VCET_Chatbot.git
   cd VCET_Chatbot
   ```

2. **Set up Python virtual environment**
   ```bash
   cd Server
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install flask flask-cors python-dotenv groq pinecone-client sentence-transformers
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the `Server/` directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   PINECONE_API_KEY=your_pinecone_api_key_here
   ```

5. **Initialize Pinecone vector database**
   ```bash
   python vector_embedding.py
   ```
   This will create the Pinecone index and upload your knowledge base.

6. **Start the Flask server**
   ```bash
   python rag_chain.py
   ```
   The server will run on `http://127.0.0.1:5000`

7. **Open the chatbot interface**
   
   Open `chatbot/index.html` in your web browser or serve it using a local server:
   ```bash
   # Using Python's built-in server
   cd ../chatbot
   python -m http.server 8000
   ```
   Then navigate to `http://localhost:8000`

## 🔧 Configuration

### Customizing the Knowledge Base

1. Add your text data to `Server/data/extracted.txt`
2. Run the embedding script to update the vector database:
   ```bash
   python vector_embedding.py
   ```

### Adjusting Model Parameters

In `rag_chain.py`, you can modify:
- `top_k`: Number of retrieved contexts (default: 3)
- `temperature`: LLM creativity level (default: 0.7)
- `max_tokens`: Maximum response length (default: 500)
- `model`: Groq model selection (default: "llama-3.3-70b-versatile")

## 🎯 How It Works

1. **User Query**: User types or speaks a question
2. **Embedding**: Query is converted to a vector using SentenceTransformer
3. **Retrieval**: Similar context chunks are retrieved from Pinecone
4. **Generation**: Retrieved contexts + query are sent to Groq LLM
5. **Response**: AI-generated response is displayed and spoken back

## 🛠️ Technologies Used

### Backend
- **Flask**: Web framework for the API server
- **Groq**: High-performance LLM inference
- **Pinecone**: Vector database for semantic search
- **SentenceTransformers**: Text embedding model (all-MiniLM-L6-v2)
- **Python-dotenv**: Environment variable management

### Frontend
- **HTML5/CSS3**: Modern, responsive UI
- **Vanilla JavaScript**: No framework dependencies
- **Web Speech API**: Voice recognition and synthesis
- **Boxicons**: Beautiful icon library

## 📊 API Endpoints

### POST /chat
Send a message to the chatbot

**Request:**
```json
{
  "message": "What is VCET?"
}
```

**Response:**
```json
{
  "response": "VCET (Vivekanand College of Engineering & Technology) is..."
}
```

## 🎨 Features Breakdown

### Voice Interaction
- Click the microphone icon to speak your query
- Automatic speech-to-text conversion
- Text-to-speech for bot responses
- Visual feedback during voice input

### Chat Interface
- Modern, clean design with smooth animations
- Typing indicators for better UX
- Conversation history display
- Mobile-responsive layout
- Toggle button for showing/hiding chat

### RAG System
- Semantic search for relevant information
- Context-aware responses
- Conversation memory (last 5 exchanges)
- Efficient vector similarity matching

## 🔒 Security Notes

- Never commit `.env` files to version control
- Keep your API keys secure
- The `.gitignore` file is configured to exclude sensitive files
- Use environment variables for all credentials

## 🐛 Troubleshooting

### Common Issues

**Issue**: "CORS error when calling Flask API"
- **Solution**: Ensure Flask-CORS is installed and configured properly

**Issue**: "Voice recognition not working"
- **Solution**: Use Chrome, Edge, or Safari. Voice features require HTTPS in production.

**Issue**: "Pinecone dimension mismatch"
- **Solution**: The script automatically handles this by recreating the index

**Issue**: "ModuleNotFoundError"
- **Solution**: Ensure all dependencies are installed in your virtual environment

## 📈 Future Enhancements

- [ ] Add user authentication
- [ ] Implement chat history persistence
- [ ] Add multi-language support
- [ ] Deploy to cloud platform (AWS/Azure/GCP)
- [ ] Add file upload for dynamic knowledge base updates
- [ ] Implement advanced conversation analytics
- [ ] Add support for image/document queries

## 👨‍💻 Author

**Vinith Shetty**
- GitHub: [@VinithShetty](https://github.com/VinithShetty)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/VinithShetty/VCET_Chatbot/issues).

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

**Note**: Remember to replace the API keys in `vector_embedding.py` with environment variables before deploying to production.
