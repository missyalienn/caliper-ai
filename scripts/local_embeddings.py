#!/usr/bin/env python3
"""
Local Embedding Service for Caliper-AI
Provides sentence-transformer based embeddings without API calls.
"""

import logging
import numpy as np
import os
from typing import List, Optional
from sentence_transformers import SentenceTransformer

# Configure logging based on environment variable
log_level = logging.DEBUG if os.getenv('DEBUG') else logging.WARNING
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Global model instance for caching
_model = None
_model_name = "all-MiniLM-L6-v2"  # 384-dim, fast, good quality


def load_model(model_name: str = _model_name) -> Optional[SentenceTransformer]:
    # Load sentence-transformer model with caching
    global _model
    
    if _model is not None:
        return _model
    
    try:
        logger.info(f"Loading sentence-transformer model: {model_name}")
        _model = SentenceTransformer(model_name)
        logger.info(f"Model loaded successfully. Embedding dimension: {_model.get_sentence_embedding_dimension()}")
        return _model
        
    except Exception as e:
        logger.error(f"Failed to load model {model_name}: {e}")
        return None


def generate_text_embedding(text: str) -> Optional[List[float]]:
    # Generate embedding for a single text using sentence-transformers
    model = load_model()
    if model is None:
        logger.error("Model not available for embedding generation")
        return None
    
    try:
        # Generate embedding
        embedding = model.encode(text, convert_to_tensor=False)
        
        # Convert to list and ensure it's the right type
        embedding_list = embedding.tolist()
        
        # Validate dimensions
        if len(embedding_list) != 384:
            logger.warning(f"Expected 384 dimensions, got {len(embedding_list)}")
        
        return embedding_list
        
    except Exception as e:
        logger.error(f"Error generating embedding for text: {e}")
        return None


def generate_batch_embeddings(texts: List[str]) -> List[List[float]]:
    # Generate embeddings for multiple texts efficiently
    model = load_model()
    if model is None:
        logger.error("Model not available for batch embedding generation")
        return []
    
    if not texts:
        logger.warning("No texts provided for embedding")
        return []
    
    try:
        logger.info(f"Generating embeddings for {len(texts)} texts")
        
        # Generate batch embeddings
        embeddings = model.encode(texts, convert_to_tensor=False, show_progress_bar=False)
        
        # Convert to list of lists
        embeddings_list = [embedding.tolist() for embedding in embeddings]
        
        # Validate batch
        if len(embeddings_list) != len(texts):
            logger.error(f"Mismatch: {len(texts)} texts, {len(embeddings_list)} embeddings")
            return []
        
        # Validate dimensions
        if embeddings_list and len(embeddings_list[0]) != 384:
            logger.warning(f"Expected 384 dimensions, got {len(embeddings_list[0])}")
        
        logger.info(f"Successfully generated {len(embeddings_list)} embeddings")
        return embeddings_list
        
    except Exception as e:
        logger.error(f"Error generating batch embeddings: {e}")
        return []


def get_model_info() -> dict:
    # Get information about the loaded model
    model = load_model()
    if model is None:
        return {"status": "not_loaded", "model_name": _model_name}
    
    return {
        "status": "loaded",
        "model_name": _model_name,
        "embedding_dimension": model.get_sentence_embedding_dimension(),
        "max_seq_length": model.max_seq_length
    }


def main():
    # Test the local embedding service
    logger.info("Testing local embedding service")
    
    # Test model loading
    info = get_model_info()
    logger.info(f"Model info: {info}")
    
    if info["status"] == "loaded":
        # Test single embedding
        test_text = "How to install floating shelves safely?"
        embedding = generate_text_embedding(test_text)
        if embedding:
            logger.info(f"Single embedding test: {len(embedding)} dimensions")
        else:
            logger.error("Single embedding test failed")
        
        # Test batch embeddings
        test_texts = [
            "How to fix a leaky faucet?",
            "What tools do I need for painting?",
            "Safety equipment for woodworking"
        ]
        batch_embeddings = generate_batch_embeddings(test_texts)
        if batch_embeddings:
            logger.info(f"Batch embedding test: {len(batch_embeddings)} embeddings generated")
        else:
            logger.error("Batch embedding test failed")
    else:
        logger.error("Model failed to load")


if __name__ == "__main__":
    main()

