#!/usr/bin/env python3
"""
CSV Data Ingestion Script for Caliper-AI Prototype

Simple script to load DIY snippets from CSV and prepare for ChromaDB.
"""

import pandas as pd
import os
import sys


def load_diy_data(csv_path="data/diy_snippets.csv"):
    # Load and validate DIY snippets from CSV file
    # Args: csv_path (str): Path to CSV file
    # Returns: list: List of documents ready for ChromaDB
    print(f"Loading DIY data from: {csv_path}")
    
    # Check if file exists
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found: {csv_path}")
        return None
    
    try:
        # Load CSV
        df = pd.read_csv(csv_path)
        print(f"✓ Loaded {len(df)} DIY snippets")
        
        # Basic validation
        required_cols = ['id', 'category', 'snippet_text', 'tools_required', 'ppe_required']
        missing_cols = [col for col in required_cols if col not in df.columns]
        
        if missing_cols:
            print(f"Error: Missing columns: {missing_cols}")
            return None
        
        # Prepare data for ChromaDB
        documents = []
        for _, row in df.iterrows():
            doc = {
                'id': str(row['id']),
                'text': str(row['snippet_text']),
                'metadata': {
                    'category': str(row['category']),
                    'tools_required': str(row['tools_required']),
                    'ppe_required': str(row['ppe_required'])
                }
            }
            documents.append(doc)
        
        print(f"✓ Prepared {len(documents)} documents for ChromaDB")
        print(f"✓ Categories: {df['category'].unique().tolist()}")
        
        return documents
        
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None


def main():
    # Main function to run CSV ingestion
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "data/diy_snippets.csv"
    
    documents = load_diy_data(csv_path)
    
    if documents:
        print("✓ Data ingestion successful!")
        return True
    else:
        print("✗ Data ingestion failed!")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
