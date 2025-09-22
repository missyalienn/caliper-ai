# Caliper: AI-Powered DIY Assistant

## 🎯 Vision

**Caliper turns DIY overwhelm into confident action.**

Your AI assistant for DIY that cuts through information overload with practical steps — so you can build with confidence.

## ⚙️ What It Does

Caliper answers your DIY questions with step-by-step instructions, essential tools, and safety tips.

### Current Functionality
- **Data Ingestion**: Loads DIY project snippets with categories, tools, and safety tips
- **Semantic Search**: Uses sentence-transformers embeddings to find relevant guidance
- **RAG Pipeline**: Retrieves relevant snippets and composes step-by-step, context-aware answers
- **Categories**: Home Decor, Painting, Refinishing, Woodworking, Lighting, Tools, Plumbing
  
## 🛠️ Tech Stack

- **ChromaDB**: In-memory vector storage and similarity search
- **Python**: Core development language with modular scripts
- **Sentence Transformers**: Semantic embeddings (powered by PyTorch)
- **CSV**: Structured storage of DIY project snippets
- **Safety-Focused**: Each snippet includes recommended safety tips and required tools

## 📁 Project Structure

```
caliper-ai/
├── data/           # Local data files containing DIY project snippets
├── chroma_db/      # ChromaDB persistent storage (when using PersistentClient)
├── scripts/        # Python scripts for core functionality
├── docs/           # Technical documentation
├── venv/          # Python virtual environment
└── README.md      # This file
```

---

## 📚 Technical Documentation

For detailed technical information, see [`docs/README.md`](docs/README.md) which includes:
- Script descriptions and data structures
- Embedding configuration and pipeline workflow
- Demo instructions and development notes