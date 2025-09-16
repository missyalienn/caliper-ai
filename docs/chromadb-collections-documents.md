# ChromaDB Collections and Documents

## Overview

This document explains ChromaDB collections and documents, and breaks down the setup script components for the Caliper-AI prototype.

## ChromaDB Collections & Documents

### Collection = Database Table
- **Collection**: Like a database table or folder that holds related documents
- **Purpose**: Organizes documents by topic/type (like "diy_snippets" for all DIY content)
- **Metadata**: Can filter/search within a collection
- **Scalability**: Can have multiple collections (e.g., "diy_snippets", "user_queries", "tool_references")

### Document = Row in Table
- **Document**: A single piece of content (like one DIY Q&A)
- **Structure**: `{id, text, metadata}`
- **Text**: The actual content that gets embedded (your Q&A)
- **Metadata**: Additional info (category, tools, PPE) for filtering

## Setup Script Breakdown

### 1. Load Data (`load_diy_data`)
```python
documents = load_diy_data(csv_path)
```
- **Purpose**: Read CSV and convert to ChromaDB format
- **Output**: List of documents ready for storage
- **Format**: Each document has `id`, `text`, `metadata`

### 2. Setup Collection (`setup_chroma_collection`)
```python
client = chromadb.PersistentClient(path=persist_directory)
collection = client.create_collection(name="diy_snippets")
```
- **Purpose**: Create the "container" for your documents
- **Client**: Connection to ChromaDB (like database connection)
- **Collection**: The "table" where documents will be stored
- **Persistent**: Saves to disk (not just memory)

### 3. Store Documents (`store_documents`)
```python
collection.add(ids=ids, documents=texts, metadatas=metadatas)
```
- **Purpose**: Put your documents into the collection
- **Batch operation**: Stores all documents at once
- **Embeddings**: ChromaDB automatically creates vector embeddings
- **Indexing**: Makes documents searchable

### 4. Verify Collection (`verify_collection`)
```python
count = collection.count()
results = collection.get(limit=5)
```
- **Purpose**: Confirm everything worked correctly
- **Count check**: Verify all documents were stored
- **Sample data**: Show categories to confirm content
- **Health check**: Ensure collection is ready for queries

## Why This Structure?

### Collections Allow:
- **Organization**: Separate different types of content
- **Filtering**: Search within specific categories
- **Scalability**: Add new collections as you grow
- **Performance**: Optimize searches within related content

### Documents Enable:
- **Semantic search**: Find similar content by meaning
- **Metadata filtering**: Filter by category, tools, difficulty
- **RAG queries**: Retrieve relevant context for AI responses

## Real-World Analogy
- **Collection** = Library section (e.g., "DIY Books")
- **Document** = Individual book (e.g., "How to Fix Faucets")
- **Metadata** = Book catalog info (category, tools needed, difficulty)
- **Embeddings** = Book's "fingerprint" for finding similar content

## Technical Details

### Document Structure
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

### Collection Operations
- **Create**: `client.create_collection(name="diy_snippets")`
- **Get**: `client.get_collection(name="diy_snippets")`
- **Add**: `collection.add(ids, documents, metadatas)`
- **Query**: `collection.query(query_texts=["how to fix faucet"])`
- **Count**: `collection.count()`

### Storage Location
- **Local**: `./chroma_db/` directory
- **Persistent**: Survives restarts
- **Scalable**: Can move to cloud later

## Next Steps
- Generate embeddings for semantic search
- Build query system for RAG
- Create demo interface
- Scale to cloud storage
