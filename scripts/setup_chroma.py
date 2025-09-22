#!/usr/bin/env python3
"""
ChromaDB Setup Script for Caliper-AI 
Simple script to initialize ChromaDB collection and store DIY snippets.
"""

import chromadb
import os
import sys
import logging
from typing import Optional, Tuple, List, Dict, Any
from ingest_data import load_diy_data

# Configure logging based on environment variable
log_level = logging.DEBUG if os.getenv('DEBUG') else logging.WARNING
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def setup_chroma_collection(persist_directory: str = "./chroma_db"):
    # Initialize ChromaDB client with persistent storage
    logger.info(f"Setting up ChromaDB collection in: {persist_directory}")
    
    try:
        # Create ChromaDB client
        client = chromadb.EphemeralClient()
        logger.info("ChromaDB client initialized")
        
        # Create or get collection
        collection_name = "diy_snippets"
        try:
            collection = client.get_collection(name=collection_name)
            logger.info(f"Found existing collection: {collection_name}")
        except Exception:
            collection = client.create_collection(name=collection_name)
            logger.info(f"Created new collection: {collection_name}")
        
        return client, collection
        
    except Exception as e:
        logger.error(f"Error setting up ChromaDB: {e}")
        return None, None


def store_documents(collection, documents: List[Dict[str, Any]]) -> bool:
    # Store documents in ChromaDB collection
    logger.info(f"Storing {len(documents)} documents in ChromaDB")
    
    try:
        # Extract data for ChromaDB
        ids = [doc['id'] for doc in documents]
        texts = [doc['text'] for doc in documents]
        metadatas = [doc['metadata'] for doc in documents]
        
        # Add documents to collection
        collection.add(
            ids=ids,
            documents=texts,
            metadatas=metadatas
        )
        
        logger.info(f"Successfully stored {len(documents)} documents")
        return True
        
    except Exception as e:
        logger.error(f"Error storing documents: {e}")
        return False


def verify_collection(collection) -> bool:
    # Verify documents were stored correctly
    logger.info("Verifying collection")
    
    try:
        # Get collection count
        count = collection.count()
        logger.info(f"Collection contains {count} documents")
        
        # Show sample categories
        results = collection.get(limit=5)
        if results['metadatas']:
            categories = [meta['category'] for meta in results['metadatas']]
            logger.info(f"Sample categories: {list(set(categories))}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error verifying collection: {e}")
        return False


def main() -> bool:
    # Main function to set up ChromaDB
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "data/diy_snippets.csv"
    
    logger.info("Starting ChromaDB setup")
    
    # Step 1: Load DIY data
    documents = load_diy_data(csv_path)
    if not documents:
        logger.error("Failed to load DIY data")
        return False
    
    # Step 2: Setup ChromaDB collection
    client, collection = setup_chroma_collection()
    if not collection:
        logger.error("Failed to setup ChromaDB collection")
        return False
    
    # Step 3: Store documents
    if not store_documents(collection, documents):
        logger.error("Failed to store documents")
        return False
    
    # Step 4: Verify collection
    if not verify_collection(collection):
        logger.error("Failed to verify collection")
        return False
    
    logger.info("ChromaDB setup completed successfully")
    logger.info("Ready for semantic search and RAG queries")
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
