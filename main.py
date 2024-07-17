import fitz  

def extract_pages(input_pdf, output_pdf, pages):
    doc = fitz.open(input_pdf) 
    new_doc = fitz.open() 
   
    for page_num in pages:
        new_doc.insert_pdf(doc, from_page=page_num-1, to_page=page_num-1)

    new_doc.save(output_pdf)

input_pdf = "path/to/input.pdf" 
output_pdf = "path/to/output.pdf" 

# Specify the pages you want to extract
pages = [24, 25] + list(range(1, 23))

extract_pages(input_pdf, output_pdf, pages)
