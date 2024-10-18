from PyPDF2 import PdfReader  # Import PdfReader from the PyPDF2 library to read PDF files
from docx import Document  # Import Document from the python-docx library to read DOCX files


def read_pdf(file_path):
    reader = PdfReader(file_path)  # Create a PdfReader object to read the PDF file
    text = ""  # Initialize an empty string to hold the extracted text
    for page in reader.pages:  # Iterate over each page in the PDF
        text += page.extract_text()  # Extract text from the page and add it to the text string
    return text  # Return the combined text from the PDF


def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:  # Open the TXT file in read mode with UTF-8 encoding
        return f.read()  # Read and return the contents of the file


def read_docx(file_path):
    doc = Document(file_path)  # Create a Document object to read the DOCX file
    text = ""  # Initialize an empty string to hold the extracted text
    for paragraph in doc.paragraphs:  # Iterate over each paragraph in the DOCX file
        text += paragraph.text + "\n"  # Add the paragraph text to the text string, followed by a newline
    return text  # Return the combined text from the DOCX


# Specify the file paths for your files
txt_file_path = 'input files/txtfile.txt'  # Path to the TXT file
pdf_file_path = 'input files/pdffile.pdf'  # Path to the PDF file
docx_file_path = 'input files/docfile.docx'  # Path to the DOCX file

# Read the files
combined_text = ""  # Initialize an empty string to combine text from all files
combined_text += read_txt(txt_file_path)  # Read and append text from the TXT file
combined_text += read_pdf(pdf_file_path)  # Read and append text from the PDF file
combined_text += read_docx(docx_file_path)  # Read and append text from the DOCX file

# Print the combined text
print(combined_text)  # Output the combined text from all files to the console
