#!/usr/bin/env python3
"""
Embedding Generation Script for Caliper-AI
Generates vector embeddings for DIY snippets using local sentence-transformers.
"""

import os
import sys
import logging
from typing import List, Dict, Any, Optional
from ingest_data import load_diy_data
from local_embeddings import generate_batch_embeddings

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def generate_embeddings(texts: List[str]) -> List[List[float]]:
    # Generate semantic embeddings using local sentence-transformers
    return generate_batch_embeddings(texts)


def generate_embeddings_for_documents(documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    # Generate embeddings for all documents
    logger.info(f"Generating embeddings for {len(documents)} documents")
    
    try:
        # Extract texts
        texts = [doc['text'] for doc in documents]
        
        # Generate semantic embeddings
        embeddings = generate_embeddings(texts)
        
        # Add embeddings to documents
        for i, doc in enumerate(documents):
            doc['embedding'] = embeddings[i]
        
        logger.info(f"Successfully generated {len(documents)} embeddings")
        return documents
        
    except Exception as e:
        logger.error(f"Error generating embeddings: {e}")
        return []


def store_embeddings_in_chroma(documents_with_embeddings: List[Dict[str, Any]]) -> bool:
    # Store documents with embeddings in ChromaDB
    logger.info("Storing embeddings in ChromaDB")
    
    try:
        import chromadb
        
        # Use EphemeralClient instead of PersistentClient
        client = chromadb.EphemeralClient()
        
        # Get or create collection
        collection_name = "diy_snippets"
        collection = client.get_or_create_collection(name=collection_name)
        logger.info(f"Using collection: {collection_name}")
        
        # Extract data
        ids = [doc['id'] for doc in documents_with_embeddings]
        texts = [doc['text'] for doc in documents_with_embeddings]
        metadatas = [doc['metadata'] for doc in documents_with_embeddings]
        embeddings = [doc['embedding'] for doc in documents_with_embeddings]
        
        # Add documents with embeddings to collection
        collection.add(
            ids=ids,
            documents=texts,
            metadatas=metadatas,
            embeddings=embeddings
        )
        
        logger.info(f"Successfully stored {len(documents_with_embeddings)} embeddings")
        return True
        
    except Exception as e:
        logger.error(f"Error storing embeddings: {e}")
        return False


def main() -> bool:
    # Main function to generate and store embeddings
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "data/diy_snippets.csv"
    
    logger.info("Starting embedding generation")
    
    # Load documents
    documents = load_diy_data(csv_path)
    if not documents:
        logger.error("Failed to load documents")
        return False
    
    # Generate embeddings
    documents_with_embeddings = generate_embeddings_for_documents(documents)
    if not documents_with_embeddings:
        logger.error("Failed to generate embeddings")
        return False
    
    # Store embeddings
    if not store_embeddings_in_chroma(documents_with_embeddings):
        logger.error("Failed to store embeddings")
        return False
    
    logger.info("Embedding generation completed successfully")
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
