
# PDFPageExtractor
Extracts specified pages from an input PDF and saves them to an output PDF.

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

