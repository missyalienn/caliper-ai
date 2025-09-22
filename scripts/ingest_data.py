#!/usr/bin/env python3
"""
CSV Data Ingestion Script for Caliper AI. 
Simple script to load DIY snippets from CSV and prepare for ChromaDB.
"""

import pandas as pd
import os
import sys
from typing import List, Dict, Any, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def load_diy_data(csv_path: str = "data/diy_snippets.csv") -> Optional[List[Dict[str, Any]]]:
    # Load and validate DIY snippets from CSV file
    logger.info(f"Loading DIY data from: {csv_path}")
    
    # Check if file exists
    if not os.path.exists(csv_path):
        logger.error(f"CSV file not found: {csv_path}")
        return None
    
    try:
        # Load CSV
        df = pd.read_csv(csv_path)
        logger.info(f"Loaded {len(df)} DIY snippets")
        
        # Basic validation - check required columns
        required_cols = ['id', 'category', 'snippet_text', 'tools_required', 'ppe_required']
        missing_cols = [col for col in required_cols if col not in df.columns]
        
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        # Prepare documents for ChromaDB
        documents = []
        for _, row in df.iterrows():
            doc = {
                'id': str(row['id']),  # Convert ID to string for ChromaDB
                'text': row['snippet_text'],
                'metadata': {
                    'category': row['category'],
                    'tools_required': row['tools_required'],
                    'ppe_required': row['ppe_required']
                }
            }
            documents.append(doc)
        
        logger.info(f"Prepared {len(documents)} documents for ChromaDB")
        logger.info(f"Categories: {df['category'].unique().tolist()}")
        
        return documents
        
    except Exception as e:
        logger.error(f"Error loading CSV: {e}")
        return None


def main() -> bool:
    # Main function to run CSV ingestion
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "data/diy_snippets.csv"
    
    logger.info("Starting CSV data ingestion")
    documents = load_diy_data(csv_path)
    
    if documents:
        logger.info("Data ingestion completed successfully")
        return True
    else:
        logger.error("Data ingestion failed")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
