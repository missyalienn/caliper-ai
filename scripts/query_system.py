#!/usr/bin/env python3
"""
RAG Query System for Caliper-AI Prototype

Simple query system that finds relevant DIY snippets using semantic search.
"""

import os
import sys
import logging
import numpy as np
from typing import List, Dict, Any, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def generate_query_embedding(query: str) -> List[float]:
    # Generate mock embedding for user query (same format as stored embeddings)
    embedding = np.random.normal(0, 1, 1536).tolist()
    return embedding


def search_chroma(query: str, top_k: int = 3) -> List[Dict[str, Any]]:
    # Search ChromaDB for similar DIY snippets
    logger.info(f"Searching for: '{query}'")
    
    try:
        import chromadb
        
        # Get ChromaDB collection
        client = chromadb.PersistentClient(path="./chroma_db")
        collection = client.get_collection(name="diy_snippets")
        
        # Generate query embedding
        query_embedding = generate_query_embedding(query)
        
        # Search for similar documents
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        # Format results
        formatted_results = []
        for i in range(len(results['ids'][0])):
            result = {
                'id': results['ids'][0][i],
                'text': results['documents'][0][i],
                'metadata': results['metadatas'][0][i],
                'distance': results['distances'][0][i]
            }
            formatted_results.append(result)
        
        logger.info(f"Found {len(formatted_results)} relevant snippets")
        return formatted_results
        
    except Exception as e:
        logger.error(f"Error searching ChromaDB: {e}")
        return []


def display_results(query: str, results: List[Dict[str, Any]]):
    # Display search results in a readable format
    print(f"\n🔍 Search Results for: '{query}'")
    print("=" * 50)
    
    if not results:
        print("No relevant DIY snippets found.")
        return
    
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['metadata']['category']} - ID: {result['id']}")
        print(f"   Tools: {result['metadata']['tools_required']}")
        print(f"   PPE: {result['metadata']['ppe_required']}")
        print(f"   Content: {result['text'][:200]}...")
        print(f"   Relevance: {1 - result['distance']:.2f}")


def interactive_query():
    # Interactive query interface
    print("🔧 Caliper DIY Assistant - Interactive Query")
    print("Type your DIY question (or 'quit' to exit)")
    print("-" * 50)
    
    while True:
        query = input("\n❓ Your question: ").strip()
        
        if query.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
        
        if not query:
            print("Please enter a question.")
            continue
        
        # Search and display results
        results = search_chroma(query)
        display_results(query, results)


def main():
    # Main function - can run interactively or with command line query
    if len(sys.argv) > 1:
        # Command line query
        query = " ".join(sys.argv[1:])
        results = search_chroma(query)
        display_results(query, results)
    else:
        # Interactive mode
        interactive_query()


if __name__ == "__main__":
    main()
