# Import the necessary libraries
from ocr import convert_from_path
import pytesseract
import os

# Function to perform OCR on a PDF file
def pdf_to_text(pdf_path):
    # Convert PDF to images
    pages = convert_from_path(pdf_path)
    
    # Initialize an empty string to store the extracted text
    extracted_text = ''
    
    # Process each page
    for page_num, image in enumerate(pages):
        # Perform OCR on the image
        text = pytesseract.image_to_string(image)
        
        # Append the extracted text to the result
        extracted_text += f'Page {page_num + 1}:\n{text}\n\n'
    
    return extracted_text

# Main function
def main():
    # Path to the PDF file
    pdf_path = 'file.pdf'
    
    # Perform OCR on the PDF file
    extracted_text = pdf_to_text(pdf_path)
    
    # Print the extracted text
    print(extracted_text)

# Entry point of the script
if __name__ == "__main__":
    main()
