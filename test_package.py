import os
import logging
from ollama_vision_extract import DocumentExtractor

def test_extraction():
    try:
        # Set up logging
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        
        # Initialize the document extractor with the correct model
        extractor = DocumentExtractor(model_name="llama3.2-vision:latest")
        logger.info("Successfully initialized DocumentExtractor")

        # Get the image path from environment variable or use a default
        image_path = os.getenv("TEST_IMAGE_PATH", "test_image.jpeg")
        
        if not os.path.exists(image_path):
            logger.error(f"Test image not found at: {image_path}")
            return False
            
        # Extract text from the image
        result = extractor.extract_from_image(image_path)
        logger.info(f"Extraction result: {result}")
        
        return True
        
    except Exception as e:
        logger.error(f"Extraction error: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_extraction()
    exit(0 if success else 1)
