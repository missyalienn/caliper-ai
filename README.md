# Caliper-AI

## Overview

**Caliper: Your AI companion for DIY — clear, practical steps to start building with confidence.**

Caliper helps beginner DIYers move from overwhelm to action by cutting through information overload and providing clear, practical, and safe steps — so they can start projects confidently without getting lost in endless research.

**In short: Caliper turns overwhelm into action.**


## Key Features

### ⚡ **Essential Skills + Minimum Required Tools**
- Reduce DIY decision fatigue by focusing on the skills and tools you actually need  
- Provide clear, no-frills instructions that are practical, safe, and beginner-friendly

### 🎯 **Smart, Context-Aware Guidance**
- Understand user questions and context to provide relevant advice.
- Combine semantic search with adaptive, situation-specific responses.

### 🛡️ **Safety-First Approach**
- Flag potential hazards and provide best practices for safety. 
- Reccommend essential personal protective equipment to keep you safe.

### 📒 **Project Notebook**
- Save generated steps and tool lists for a project in a single, easy-to-access notebook  
- Add personal notes and links for further guidance. 
  
---

## Key Technologies

### Vector Database & Search
- **ChromaDB**: Vector storage and similarity search for DIY project snippets
- **Semantic Search**: Find relevant project guidance based on meaning, not just keywords

### AI & Machine Learning
- **OpenAI Embeddings**: Generate vector representations of DIY content and user queries
- **Hugging Face Embeddings**: Alternative embedding model for flexibility
- **RAG (Retrieval-Augmented Generation)**: Combine semantic search with context-aware responses

### Data Processing
- **CSV/JSON**: Structured storage of DIY project snippets with metadata
- **Python**: Core development language with modular script architecture

## Project Structure

```
caliper-ai/
├── data/           # CSV/JSON files containing DIY project snippets
├── scripts/        # Python scripts for core functionality
├── notebooks/      # Optional interactive testing and exploration
├── venv/          # Python virtual environment
└── README.md      # This file
```

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare Data
- Edit or add your DIY snippets in `data/diy_snippets.csv`

### 3. Run the End-to-End Demo

```bash
python scripts/demo.py
```
- This will load data, set up ChromaDB, generate embeddings, and run sample queries.

### 4. Try Interactive Semantic Search

```bash
python scripts/query_system.py
```
- Enter your own DIY questions and see relevant results.

### 5. Explore in Jupyter Notebook

```bash
jupyter notebook notebooks/demo.ipynb
```
- Run each cell to see the pipeline step by step.

---

## Usage Examples

### Run the Demo Script
```bash
python scripts/demo.py
```

### Run a Query from the Command Line
```bash
python scripts/query_system.py "how to fix a leaky faucet"
```

### Run the Notebook
```bash
jupyter notebook notebooks/demo.ipynb
```

---

## Architecture Overview
- **Data Ingestion**: `scripts/ingest_data.py`
- **ChromaDB Setup**: `scripts/setup_chroma.py`
- **Embedding Generation**: `scripts/generate_embeddings.py`
- **RAG Query System**: `scripts/query_system.py`
- **Demo Script**: `scripts/demo.py`
- **Demo Notebook**: `notebooks/demo.ipynb`

---
