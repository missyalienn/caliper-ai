# Caliper-AI Technical Documentation

## System Overview

Caliper-AI is a prototype AI companion for beginner DIY projects. The system ingests DIY project data from CSV files, generates embeddings, stores them in ChromaDB, and uses retrieval-augmented generation (RAG) to provide relevant project instructions along with metadata such as category, required tools, and safety equipment.


## Architecture

### Core Components
- **Data Pipeline**: CSV ingestion and validation
- **Vector Database**: ChromaDB for semantic search
- **Embedding System**: 384-dimension mock embeddings
- **Query Interface**: RAG-based question answering
- **Demo System**: End-to-end workflow demonstration

## Scripts

### Data Management
- **`scripts/ingest_data.py`**: Loads DIY snippets from CSV, validates structure, converts IDs to strings for ChromaDB compatibility
- **`scripts/setup_chroma.py`**: Initializes ChromaDB collection using EphemeralClient, stores documents with metadata

### Embedding Pipeline
- **`scripts/generate_embeddings.py`**: Generates 384-dimension mock embeddings, stores in ChromaDB using EphemeralClient and get_or_create_collection()
- **`scripts/query_system.py`**: Handles user queries, generates query embeddings, performs semantic search

### Demo and Testing
- **`scripts/demo.py`**: Complete end-to-end demonstration script
- **`notebooks/demo.ipynb`**: Interactive Jupyter notebook for step-by-step exploration

## Data Structure

### CSV Format (`data/diy_snippets.csv`)
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

### Dimensions
- **Storage Embeddings**: 384 dimensions (sentence-transformers format)
- **Query Embeddings**: 384 dimensions (matching storage)
- **Generation Method**: Mock random vectors using numpy

### ChromaDB Configuration
- **Client Type**: EphemeralClient (in-memory)
- **Collection Name**: "diy_snippets"
- **Collection Method**: get_or_create_collection()

## Pipeline Workflow

### 1. Data Ingestion
```bash
python scripts/ingest_data.py [csv_path]
```
- Loads CSV data
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
- Generates 384-dim mock embeddings
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

### Jupyter Notebook Exploration
```bash
jupyter notebook notebooks/demo.ipynb
```
Step-by-step interactive exploration of each pipeline component

## Technical Specifications

### Dependencies
- **chromadb**: Vector database operations
- **pandas**: CSV data processing
- **numpy**: Embedding generation
- **logging**: System logging and debugging

### Error Handling
- CSV validation with required column checking
- ChromaDB collection existence handling
- Embedding dimension consistency validation
- Comprehensive logging throughout pipeline

### Performance Notes
- Uses EphemeralClient for fast prototyping
- Mock embeddings for demo purposes
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
This is a prototype system using mock embeddings rather than real AI calls currently. The architecture demonstrates the core RAG pipeline for a DIY companion.

### Future Enhancements
- Real embedding models (OpenAI, Hugging Face)
- Persistent ChromaDB storage
- API integration for live queries
- Enhanced safety and tool recommendation features