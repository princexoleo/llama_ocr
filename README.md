# Llama OCR

A Python package for extracting text and information from documents using Ollama Vision model (llava). This package provides an easy-to-use interface for document processing, text extraction, and image analysis using the powerful Llama Vision model.

## Features

- 🚀 Easy integration with Ollama Vision model
- 🖼️ Advanced image preprocessing
- 📝 OCR optimization
- 📦 Batch processing support
- 🎯 Custom prompting
- 🔍 Error handling and logging

## Installation

```bash
# Install the package
pip install llama-ocr

# Make sure you have Ollama installed and pull the llava model
ollama pull llava
```

## Quick Start

```python
from llama_ocr import DocumentExtractor

# Initialize the extractor
extractor = DocumentExtractor()

# Extract from a single image
result = extractor.extract_from_image("path/to/your/document.jpg")
print(result['content'])

# Extract from multiple images
results = extractor.extract_from_images([
    "path/to/document1.jpg",
    "path/to/document2.jpg"
])
for result in results:
    print(result['content'])

# Use custom prompt
result = extractor.extract_with_custom_prompt(
    "path/to/image.jpg",
    prompt="Extract the following information from this document: date, invoice number, and total amount:"
)
print(result['content'])
```

## Advanced Usage

### Image Preprocessing

```python
# Initialize with preprocessing enabled
extractor = DocumentExtractor(
    preprocess_images=True,
    optimize_for_ocr=True
)

# Extract with processed image saving
result = extractor.extract_from_image(
    "path/to/image.jpg",
    save_processed=True
)
```

### Custom Prompts

```python
# Extract specific information
result = extractor.extract_with_custom_prompt(
    "path/to/invoice.jpg",
    prompt="List all line items and their prices from this invoice:"
)
```

## API Reference

### DocumentExtractor

Main class for document extraction.

```python
DocumentExtractor(
    model_name: str = "llava",
    preprocess_images: bool = True,
    optimize_for_ocr: bool = False
)
```

#### Methods

- `extract_from_image(image_path: str, prompt: Optional[str] = None, save_processed: bool = False) -> Dict[str, str]`
- `extract_from_images(image_paths: List[str], prompt: Optional[str] = None, save_processed: bool = False) -> List[Dict[str, str]]`
- `extract_with_custom_prompt(image_paths: Union[str, List[str]], prompt: str, save_processed: bool = False) -> Union[Dict[str, str], List[Dict[str, str]]]`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- Prince Leo
- Email: princexoleo@gmail.com
- GitHub: [@princexoleo](https://github.com/princexoleo)
