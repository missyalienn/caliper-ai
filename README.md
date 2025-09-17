# Caliper: AI-Powered DIY Assistant

## 🎯 Vision

**Caliper: Your AI assistant for DIY — build with confidence.**

Caliper helps beginner DIYers cut through information overload with clear, practical steps — so they can start and finish projects confidently.

**In short: Caliper turns overwhelm into action.**

## ⚙️ What It Does

Caliper-AI is a prototype that helps beginners with DIY projects by providing practical, safe guidance and reducing decision fatigue.

### Current Functionality
- **Data Ingestion**: Loads DIY project snippets with categories, tools, and safety equipment
- **Semantic Search**: Uses 384-dimension mock embeddings to find relevant guidance
- **RAG Pipeline**: Retrieves relevant snippets and provides tools/PPE metadata
- **Categories**: Home Decor, Painting, Refinishing, Woodworking, Lighting, Tools, Plumbing

## 🛠️ Tech Stack

- **ChromaDB**: In-memory vector storage and similarity search
- **Python**: Core development language with modular scripts
- **Mock Embeddings**: 384-dimension vectors for demonstration
- **CSV**: Structured storage of DIY project snippets
- **Safety-Focused**: Each snippet includes required PPE and tools

## 📁 Project Structure

```
caliper-ai/
├── data/           # CSV files containing DIY project snippets
├── scripts/        # Python scripts for core functionality
├── notebooks/      # Interactive testing and exploration
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