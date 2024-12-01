from ollama_vision_extract import DocumentExtractor
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_extraction():
    try:
        # Initialize the extractor
        extractor = DocumentExtractor()
        logger.info("Successfully initialized DocumentExtractor")

        # Get the image path from environment variable or use a default
        image_path = os.getenv("TEST_IMAGE_PATH", "path/to/your/test/image.jpg")
        
        if not os.path.exists(image_path):
            logger.error(f"Test image not found at: {image_path}")
            logger.info("Please set TEST_IMAGE_PATH environment variable to point to a valid image file")
            return

        # Extract information
        result = extractor.extract_from_image(
            image_path,
            prompt="Describe what you see in this image:",
            save_processed=True
        )

        # Print results
        if 'error' in result:
            logger.error(f"Extraction error: {result['error']}")
        else:
            logger.info("Extraction successful!")
            logger.info(f"Extracted content: {result['content']}")
            if result['processed_image']:
                logger.info(f"Processed image saved at: {result['processed_image']}")

    except Exception as e:
        logger.error(f"Test failed with error: {str(e)}")

if __name__ == "__main__":
    test_extraction()
