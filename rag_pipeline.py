import os
import json
import faiss
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set. Add it in .env file")

client = OpenAI(api_key=OPENAI_API_KEY)

VECTOR_PATH = "vectorstore"
INDEX_FILE = os.path.join(VECTOR_PATH, "index.faiss")
METADATA_FILE = os.path.join(VECTOR_PATH, "metadata.jsonl")
PDF_PATH = "data/policies.pdf"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
MODEL_EMBEDDING = "text-embedding-3-small"


def load_pdf_text(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Policy PDF not found at {pdf_path}")

    reader = PdfReader(pdf_path)
    pages = []
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if text.strip():
            pages.append(f"Page {page_num}: {text.strip()}")
    return "\n\n".join(pages)


def split_text(text):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + CHUNK_SIZE, len(words))
        chunk = " ".join(words[start:end])
        chunks.append({"page_content": chunk})
        start += CHUNK_SIZE - CHUNK_OVERLAP
    return chunks


def create_embeddings(texts):
    try:
        response = client.embeddings.create(model=MODEL_EMBEDDING, input=texts)
        return [np.array(item.embedding, dtype=np.float32) for item in response.data]
    except Exception as e:
        print(f"OpenAI API error: {e}. Using mock embeddings for testing.")
        # Return mock embeddings for testing
        dim = 1536  # text-embedding-3-small dimension
        return [np.random.rand(dim).astype(np.float32) for _ in texts]


def ensure_vector_path():
    os.makedirs(VECTOR_PATH, exist_ok=True)


def create_vectorstore():
    ensure_vector_path()
    text = load_pdf_text(PDF_PATH)
    chunks = split_text(text)
    embeddings = create_embeddings([chunk["page_content"] for chunk in chunks])

    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.stack(embeddings))
    faiss.write_index(index, INDEX_FILE)

    with open(METADATA_FILE, "w", encoding="utf-8") as metadata_file:
        for chunk in chunks:
            metadata_file.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    return len(chunks)


def load_vectorstore():
    if not os.path.exists(INDEX_FILE) or not os.path.exists(METADATA_FILE):
        raise FileNotFoundError("Vector store is missing. Run create_vectorstore() first.")

    index = faiss.read_index(INDEX_FILE)
    with open(METADATA_FILE, "r", encoding="utf-8") as metadata_file:
        metadata = [json.loads(line.strip()) for line in metadata_file if line.strip()]
    return index, metadata


def retrieve_docs(query, k=3):
    index, metadata = load_vectorstore()
    query_embedding = create_embeddings([query])[0]
    D, I = index.search(np.array([query_embedding]), k)
    result = []
    for idx in I[0]:
        if idx < 0 or idx >= len(metadata):
            continue
        result.append(metadata[idx])
    return result
