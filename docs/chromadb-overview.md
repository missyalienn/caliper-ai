# ChromaDB Overview

## What is ChromaDB?

**ChromaDB** is a vector database designed specifically for AI applications. It's perfect for building RAG (Retrieval-Augmented Generation) systems like Caliper.

## Core Purpose

- **Stores embeddings**: Vector representations of text (like your DIY Q&As)
- **Semantic search**: Finds similar content based on meaning, not just keywords
- **RAG integration**: Perfect for retrieval-augmented generation systems

## How It Works

1. **Text → Embeddings**: Converts your DIY snippets into numerical vectors
2. **Vector Storage**: Stores these vectors in a searchable database
3. **Similarity Search**: When you ask a question, it finds the most similar stored content
4. **Metadata**: Keeps your categories, tools, PPE info alongside the vectors

## Why ChromaDB for Caliper

- **Beginner-friendly**: Much simpler than complex vector databases
- **Local/Cloud**: Can run locally for prototype, scale to cloud later
- **Python-native**: Integrates seamlessly with your Python scripts
- **RAG-ready**: Built specifically for AI applications like yours

## Example Flow

1. User asks: "How do I fix a leaky faucet?"
2. ChromaDB finds similar stored content about plumbing
3. Returns relevant DIY snippets with metadata
4. Your system uses these to generate a helpful answer

## Technical Details

### Collection Structure
- **Collection Name**: `diy_snippets`
- **Storage**: Persistent storage in `./chroma_db` directory
- **Documents**: Each DIY Q&A stored as a document
- **Metadata**: Category, tools_required, ppe_required

### Document Format
```python
{
    'id': '1',
    'text': 'Q: How do I fix a leaky faucet? A: Turn off water supply...',
    'metadata': {
        'category': 'Plumbing',
        'tools_required': 'Screwdriver, Pliers, Wrench',
        'ppe_required': 'Safety Glasses, Work gloves'
    }
}
```

### Setup Process
1. **Initialize Client**: `chromadb.PersistentClient(path="./chroma_db")`
2. **Create Collection**: `client.create_collection(name="diy_snippets")`
3. **Store Documents**: `collection.add(ids, documents, metadatas)`
4. **Verify**: Check document count and sample data

## Usage in Caliper

### Setup Script
```bash
python scripts/setup_chroma.py
```

### What It Does
- Loads DIY data from CSV
- Creates ChromaDB collection
- Stores all documents with metadata
- Verifies successful storage

### Next Steps
- Generate embeddings for semantic search
- Build query system for RAG
- Create demo interface

## Benefits for Prototype

- **Fast setup**: Simple local installation
- **Easy testing**: No cloud dependencies
- **Scalable**: Can move to cloud later
- **Production ready**: Proven technology for AI applications
