# llama_ocr

A Python package for document text extraction using Ollama Vision models, with a focus on OCR (Optical Character Recognition) capabilities.

## Features

- 🔍 Text extraction from images using Ollama Vision models
- 🖼️ Advanced image preprocessing for better OCR results
- 🛠️ Configurable settings and parameters
- 🔧 Extensible architecture with dependency injection
- 📝 Comprehensive logging and error handling

## Installation

```bash
pip install llama_ocr_py
```

Or install from source:

```bash
git clone https://github.com/princexoleo/llama_ocr.git
cd llama_ocr
pip install -e .
```

## Quick Start

```python
from llama_ocr import DocumentExtractor

# Initialize extractor
extractor = DocumentExtractor()

# Extract text from an image
result = extractor.extract_from_image(
    "path/to/image.jpg",
    prompt="Extract all text from this document"
)

# Print extracted text
print(result["text"])
```

## Advanced Usage

### Custom Configuration

```python
from llama_ocr import DocumentExtractor, OCRConfig

config = OCRConfig(
    model_name="llama3.2-vision",
    preprocess_images=True,
    optimize_for_ocr=True,
    log_level="INFO"
)

extractor = DocumentExtractor(config=config)
```

### Image Processing Options

```python
# Extract with OCR optimization
result = extractor.extract_from_image(
    "path/to/image.jpg",
    save_processed=True  # Save processed image for inspection
)
```

## Architecture

The package follows SOLID principles and uses dependency injection for flexibility:

- `DocumentExtractor`: Main class orchestrating the extraction process
- `VisionClient`: Abstract base class for vision model interactions
- `ImagePreprocessor`: Abstract base class for image processing
- `OCRConfig`: Configuration management using dataclasses

### Components

1. **Core Module**
   - `extractor.py`: Main document extraction logic
   - `vision_client.py`: Ollama Vision API integration
   - `image_processor.py`: Image preprocessing utilities
   - `base.py`: Abstract base classes and interfaces

2. **Configuration**
   - `config.py`: Configuration management using dataclasses

## Dependencies

- ollama>=0.1.27
- Pillow>=10.1.0
- python-dotenv>=1.0.0
- opencv-python>=4.8.1.78
- numpy>=1.21.0

## Development

### Setting up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
python -m unittest discover -s tests
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Ollama team for providing the vision models
- Built with ❤️ by Mazharul Islam Leon
