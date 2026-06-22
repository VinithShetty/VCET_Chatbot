# Portable image for the VCET Chatbot Flask backend.
# Runs on Hugging Face Spaces (Docker SDK), Google Cloud Run, Fly.io, Railway, Koyeb, etc.
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    # Model caches must live in a writable dir (HF Spaces containers are read-only except /tmp)
    HF_HOME=/tmp/hf_cache \
    SENTENCE_TRANSFORMERS_HOME=/tmp/st_cache

WORKDIR /app

# Install CPU-only torch first (~190 MB vs ~2 GB for the default CUDA build).
RUN pip install torch==2.2.0 --index-url https://download.pytorch.org/whl/cpu

# Then the rest of the deps (torch is already satisfied, so it's skipped).
COPY Server/requirements.txt ./Server/requirements.txt
RUN pip install -r Server/requirements.txt

# Copy the whole project (backend in Server/, frontend in chatbot/).
COPY . .

# rag_chain.py serves the frontend from ../chatbot, so run from inside Server/.
WORKDIR /app/Server

# HF Spaces routes to 7860; other hosts inject $PORT.
EXPOSE 7860
CMD gunicorn -w 1 -b 0.0.0.0:${PORT:-7860} rag_chain:app --timeout 120
