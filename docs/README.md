# Caliper-AI Technical Documentation

## System Overview

Caliper-AI is an AI companion for beginner DIY projects. The system ingests DIY project data from local data sources, generates embeddings using sentence transformers, stores them in ChromaDB, and uses retrieval-augmented generation (RAG) to provide relevant project instructions along with metadata such as category, required tools, and safety equipment.


## Architecture

### Core Components
- **Data Pipeline**: Data ingestion and validation
- **Vector Database**: ChromaDB for semantic search
- **Embedding System**: Sentence transformers for semantic embeddings
- **Query Interface**: RAG-based question answering
- **Demo System**: End-to-end workflow demonstration

## Scripts

### Data Management
- **`scripts/ingest_data.py`**: Loads DIY snippets from CSV, validates structure, converts IDs to strings for ChromaDB compatibility
- **`scripts/setup_chroma.py`**: Initializes ChromaDB collection using EphemeralClient, stores documents with metadata

### Embedding Pipeline
- **`scripts/generate_embeddings.py`**: Generates embeddings using sentence transformers, stores in ChromaDB using EphemeralClient and get_or_create_collection()
- **`scripts/query_system.py`**: Handles user queries, generates query embeddings, performs semantic search

### Demo and Testing
- **`scripts/demo.py`**: Complete end-to-end demonstration script

## Data Structure

### Data Format (`data/diy_snippets.csv`)
```csv
id,category,snippet_text,tools_required,ppe_required
```

### Metadata Fields
- **`id`**: Unique identifier (converted to string for ChromaDB)
- **`category`**: Project type (Home Decor, Painting, Refinishing, Woodworking, Lighting, Tools, Plumbing)
- **`snippet_text`**: Question and answer content
- **`tools_required`**: Comma-separated list of necessary tools
- **`ppe_required`**: Required personal protective equipment

### Document Structure in ChromaDB
```python
{
    'id': 'string_id',
    'text': 'snippet_text_content',
    'metadata': {
        'category': 'project_category',
        'tools_required': 'tool_list',
        'ppe_required': 'safety_equipment'
    }
}
```

## Embedding Configuration

### Embedding Model
- **Model**: sentence-transformers
- **Storage Embeddings**: Generated using sentence transformers
- **Query Embeddings**: Generated using same sentence transformers model
- **Generation Method**: Real semantic embeddings from sentence transformers

### ChromaDB Configuration
- **Client Type**: EphemeralClient (in-memory)
- **Collection Name**: "diy_snippets"
- **Collection Method**: get_or_create_collection()

## Pipeline Workflow

### 1. Data Ingestion
```bash
python scripts/ingest_data.py [csv_path]
```
- Loads data from local source
- Validates required columns
- Converts numeric IDs to strings
- Prepares documents for ChromaDB

### 2. ChromaDB Setup
```bash
python scripts/setup_chroma.py [csv_path]
```
- Initializes EphemeralClient
- Creates or retrieves collection
- Stores documents with metadata
- Verifies collection contents

### 3. Embedding Generation
```bash
python scripts/generate_embeddings.py [csv_path]
```
- Generates embeddings using sentence transformers
- Stores embeddings in ChromaDB
- Uses EphemeralClient for consistency

### 4. Query Processing
```bash
python scripts/query_system.py [query_string]
```
- Generates query embedding
- Performs semantic search
- Returns top-k relevant results
- Displays formatted results

## Demo Instructions

### Complete End-to-End Demo
```bash
python scripts/demo.py
```
Runs the full pipeline: data loading → ChromaDB setup → embedding generation → sample queries

### Interactive Query Testing
```bash
python scripts/query_system.py "how to install floating shelves"
```
Test specific DIY questions and see semantic search results


## Technical Specifications

### Dependencies
- **chromadb**: Vector database operations
- **pandas**: Data processing
- **sentence-transformers**: Embedding generation
- **torch**: Deep learning framework for sentence transformers
- **logging**: System logging and debugging

### Error Handling
- Data validation with required column checking
- ChromaDB collection existence handling
- Embedding model consistency validation
- Comprehensive logging throughout pipeline

### Performance Notes
- Uses EphemeralClient for fast development
- Real sentence transformer embeddings for semantic search
- In-memory storage for quick testing
- Modular script architecture for easy modification

## Configuration Files

### Environment
- **`env.template`**: API key configuration template
- **`requirements.txt`**: Python package dependencies
- **`.gitignore`**: Version control exclusions

### Data Storage
- **`data/diy_snippets.csv`**: Primary data source
- **`chroma_db/`**: ChromaDB persistent storage (when using PersistentClient)
- **`venv/`**: Python virtual environment

## Development Notes

### Current State
This system uses sentence transformers for real semantic embeddings. The architecture provides a complete RAG pipeline for a DIY companion.

### Future Enhancements
- Next iteration: rewrite using modern AI stack (LangChain, LlamaIndex, Pinecone)
- Ingest live data from external APIs for real-time context
- Note: This rewrite will occur in a separate repository to be linked here. 