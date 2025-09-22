#!/usr/bin/env python3
"""
Caliper-AI Demo Script

Complete end-to-end demo of the RAG system for DIY project assistance.
"""

import os
import sys
import logging
import time
from typing import List, Dict, Any

# Configure logging based on environment variable
log_level = logging.DEBUG if os.getenv('DEBUG') else logging.WARNING
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def run_demo():
    # Complete end-to-end demo of Caliper-AI system
    print("🔧 Caliper-AI: DIY Assistant Demo")
    print("=" * 50)
    print("This demo shows the complete RAG pipeline:")
    print("1. Load DIY data from CSV")
    print("2. Setup ChromaDB collection")
    print("3. Generate embeddings for semantic search")
    print("4. Query the system for relevant DIY guidance")
    print("=" * 50)
    
    # Step 1: Load data
    print("\n📁 Step 1: Loading DIY data...")
    try:
        from ingest_data import load_diy_data
        documents = load_diy_data("data/diy_snippets.csv")
        if documents:
            print(f"✅ Loaded {len(documents)} DIY snippets")
            print(f"   Categories: {list(set(doc['metadata']['category'] for doc in documents))}")
        else:
            print("❌ Failed to load data")
            return False
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return False
    
    # Step 2: Setup ChromaDB
    print("\n🗄️ Step 2: Setting up ChromaDB...")
    try:
        from setup_chroma import setup_chroma_collection, store_documents, verify_collection
        client, collection = setup_chroma_collection()
        if collection:
            print("✅ ChromaDB collection ready")
            if store_documents(collection, documents):
                print("✅ Documents stored in ChromaDB")
                verify_collection(collection)
            else:
                print("❌ Failed to store documents")
                return False
        else:
            print("❌ Failed to setup ChromaDB")
            return False
    except Exception as e:
        print(f"❌ Error setting up ChromaDB: {e}")
        return False
    
    # Step 3: Generate embeddings
    print("\n🧠 Step 3: Generating embeddings...")
    try:
        from generate_embeddings import generate_embeddings_for_documents, store_embeddings_in_chroma
        documents_with_embeddings = generate_embeddings_for_documents(documents)
        if documents_with_embeddings:
            print("✅ Embeddings generated")
            if store_embeddings_in_chroma(documents_with_embeddings):
                print("✅ Embeddings stored in ChromaDB")
            else:
                print("❌ Failed to store embeddings")
                return False
        else:
            print("❌ Failed to generate embeddings")
            return False
    except Exception as e:
        print(f"❌ Error generating embeddings: {e}")
        return False
    
    # Step 4: Demo queries
    print("\n🔍 Step 4: Testing semantic search...")
    try:
        from query_system import search_chroma, display_results
        
        # Sample queries to demonstrate the system
        demo_queries = [
            "how to fix a leaky faucet",
            "what tools do I need for woodworking",
            "how to paint a room properly",
            "safety equipment for sanding"
        ]
        
        for query in demo_queries:
            print(f"\n🔍 Query: '{query}'")
            results = search_chroma(query, top_k=2)
            if results:
                print(f"✅ Found {len(results)} relevant snippets")
                for i, result in enumerate(results, 1):
                    print(f"   {i}. {result['metadata']['category']} - {result['text'][:100]}...")
            else:
                print("❌ No results found")
            
            time.sleep(1)  # Pause for demo effect
        
    except Exception as e:
        print(f"❌ Error testing queries: {e}")
        return False
    
    # Demo complete
    print("\n🎉 Demo Complete!")
    print("=" * 50)
    print("✅ Caliper-AI RAG system is working!")
    print("✅ Semantic search is functional")
    print("✅ Ready for DIY project assistance")
    print("\nTo try interactive queries, run:")
    print("python scripts/query_system.py")
    print("=" * 50)
    
    return True


def main():
    # Main demo function
    success = run_demo()
    if success:
        print("\n🚀 Demo completed successfully!")
    else:
        print("\n❌ Demo failed!")
    
    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
