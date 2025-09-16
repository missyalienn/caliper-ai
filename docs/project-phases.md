# Caliper-V1 Project Phases

## Overview

This document outlines the development phases for Caliper-V1, an AI assistant prototype for beginner DIY projects. The project follows a modular, incremental approach with clear separation of concerns and safety-first principles.

## Phase 1: Foundation & Data Preparation

### Objectives
- Establish project structure and safety protocols
- Prepare and validate DIY project data
- Set up core development environment

### Key Deliverables
- **Project Structure**: Organized repository with `data/`, `scripts/`, `notebooks/`, and `docs/` directories
- **Data Collection**: CSV file (`data/diy_snippets.csv`) with structured DIY snippets
- **Data Validation**: Ensure proper CSV structure with required columns:
  - `id`: Unique identifier
  - `category`: Safe string categories (no special characters)
  - `snippet_text`: DIY project content
  - `tools_required`: Necessary tools
  - `ppe_required`: Personal protective equipment
- **Environment Setup**: Virtual environment, requirements.txt, and configuration templates

### Success Criteria
- ✅ Clean, organized project structure
- ✅ Validated CSV data with proper formatting
- ✅ Safe category strings (no `/` or special characters)
- ✅ Development environment ready for Phase 2

---

## Phase 2: Core Data Processing & ChromaDB Setup

### Objectives
- Implement data ingestion pipeline
- Set up ChromaDB vector database
- Create modular scripts for data processing

### Key Deliverables
- **Data Ingestion Script** (`scripts/ingest_data.py`):
  - CSV parsing and validation
  - Data structure verification
  - Error handling for malformed data
- **ChromaDB Setup** (`scripts/setup_chroma.py`):
  - Database initialization
  - Collection creation
  - Metadata schema definition
- **Core Logic Separation**: Database operations work without API keys

### Success Criteria
- ✅ Robust CSV ingestion with error handling
- ✅ ChromaDB collections properly configured
- ✅ Metadata schema supports all required fields
- ✅ Core functionality runs without external API dependencies

---

## Phase 3: Embedding Generation & Vector Storage

### Objectives
- Implement embedding generation for DIY snippets
- Store vectors in ChromaDB with metadata
- Create flexible API integration (with fallback to mock functions)

### Key Deliverables
- **Embedding Generation Script** (`scripts/generate_embeddings.py`):
  - OpenAI embeddings integration
  - Hugging Face embeddings alternative
  - Mock/placeholder functions when API keys unavailable
  - Comprehensive docstrings and error handling
- **Vector Storage**: Embeddings stored in ChromaDB with proper metadata
- **API Flexibility**: Graceful degradation when API keys missing

### Success Criteria
- ✅ Embeddings generated for all DIY snippets
- ✅ Vectors stored in ChromaDB with complete metadata
- ✅ Mock functions work when API keys unavailable
- ✅ Clear logging shows embedding generation progress

---

## Phase 4: RAG Query System Implementation

### Objectives
- Build semantic search functionality
- Implement context-aware response generation
- Create interactive query interface

### Key Deliverables
- **Query System** (`scripts/query_system.py`):
  - User question processing
  - Query embedding generation
  - ChromaDB similarity search
  - Top-k snippet retrieval
  - Context-aware answer generation
- **Interactive Interface**: Command-line query interface
- **RAG Pipeline**: Complete retrieval-augmented generation workflow

### Success Criteria
- ✅ Semantic search returns relevant DIY snippets
- ✅ Query embedding generation works reliably
- ✅ Top-k retrieval provides contextually appropriate results
- ✅ Interactive query system responds to user questions

---

## Phase 5: Demo & Integration

### Objectives
- Create comprehensive demo showcasing full pipeline
- Integrate all components into cohesive system
- Prepare for conference demonstration

### Key Deliverables
- **Demo Script** (`scripts/demo.py`):
  - End-to-end pipeline execution
  - Sample queries and responses
  - Clear logging and progress indicators
- **Jupyter Notebook** (`notebooks/demo.ipynb`):
  - Interactive step-by-step exploration
  - Visual demonstration of each phase
  - Educational content for conference audience
- **Documentation**: Complete usage instructions and examples

### Success Criteria
- ✅ Full pipeline runs from data ingestion to query response
- ✅ Demo script executes without errors
- ✅ Jupyter notebook provides clear educational value
- ✅ System ready for conference demonstration

---

## Phase 6: Testing & Validation

### Objectives
- Implement basic testing and validation
- Ensure system reliability and error handling
- Validate data integrity and search quality

### Key Deliverables
- **Error Handling**: Comprehensive try/catch blocks throughout
- **Input Validation**: CSV structure and data integrity checks
- **Search Quality**: Validation of semantic search relevance
- **Type Hints**: Python type annotations for code clarity
- **Basic Testing**: Simple validation of core functions

### Success Criteria
- ✅ Robust error handling prevents system crashes
- ✅ Input validation catches malformed data
- ✅ Search results are contextually relevant
- ✅ Code includes proper type hints and documentation

---

## Phase 7: Documentation & Finalization

### Objectives
- Complete comprehensive documentation
- Ensure reproducibility for conference demo
- Finalize configuration management

### Key Deliverables
- **Complete Documentation**:
  - Updated README.md with full instructions
  - API integration documentation
  - Configuration management guide
- **Reproducibility**: Clear setup instructions for conference demo
- **Configuration Management**: Easy switching between mock and real API integrations

### Success Criteria
- ✅ Complete documentation enables easy setup
- ✅ System reproducible on different environments
- ✅ Configuration management supports both development and demo modes
- ✅ Ready for conference presentation

---

## Implementation Principles

### Safety & Security
- Never execute shell commands automatically
- Never commit to Git automatically
- Keep secrets in `.env` files only
- Respect `.gitignore` rules

### Code Quality
- Modular architecture with clear separation of concerns
- Comprehensive docstrings and inline comments
- Small, incremental outputs for review
- DRY principles and descriptive naming

### Prototype Focus
- Prioritize semantic search + context-aware answers
- Ensure reproducibility for conference demo
- Balance functionality with development speed
- Focus on demonstrating core RAG capabilities

---

## Success Metrics

### Technical Metrics
- ✅ All scripts execute without errors
- ✅ ChromaDB stores and retrieves vectors correctly
- ✅ Semantic search returns relevant results
- ✅ RAG pipeline generates contextually appropriate responses

### Demo Readiness
- ✅ End-to-end demo runs smoothly
- ✅ Interactive query system responds appropriately
- ✅ Jupyter notebook provides educational value
- ✅ Documentation enables easy setup and usage

### Conference Value
- ✅ Demonstrates practical AI application
- ✅ Shows clear value proposition for beginners
- ✅ Illustrates RAG implementation
- ✅ Provides actionable next steps for audience
