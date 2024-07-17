
# PDFPageExtractor
Extracts specified pages from an input PDF and saves them to an output PDF.

## Features
- **Extract Specific Pages**: Select individual pages to extract from the input PDF.
- **Extract Page Ranges**: Specify a range of pages to extract, making it easy to handle large sections.
- **Combine Pages and Ranges**: Flexibly combine specific pages and ranges in a single extraction.
- **Preserve Text Extractability**: If the original PDF text is extractable, the output PDF will also retain text extractability. Unlike using the 'Print' feature (e.g., Microsoft Print to PDF) which may render text unextractable, this script ensures that the text remains accessible for copying or further processing.
- **Simple and Lightweight**: Minimal dependencies with an easy-to-understand code structure.
- **Python 3.x Compatible**: Works with modern versions of Python.

## Installation
**1. Clone the repository:**
```bash
git clone https://github.com/roshni-chaubey100/PDFPageExtractor.git
cd PDFPageExtractor
```
**2. Install the required dependencies:**
```bash
pip install pymupdf
```

## Usage
To use this script, specify the input PDF path, output PDF path, and the pages you want to extract. You can provide a combination of specific pages and a range of pages. Run `main.py` script and `output.pdf` will be generated in the location `"path/to/output.pdf"`

### Examples:
* **Specific Pages Only:**
```python
pages = [24, 25]
```
* **Range of Pages Only:**
```python
pages = list(range(1, 23))  # Pages 1 to 22
```
* **Combination of Both:**
```python
pages = [24, 25] + list(range(1, 23))  # Pages 24 and 25 plus Pages 1 to 22
```  

