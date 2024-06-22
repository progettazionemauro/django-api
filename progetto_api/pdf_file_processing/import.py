import PyPDF2
# riferimento: https://levelup.gitconnected.com/python-office-magic-a-complete-guide-to-pdf-file-processing-70552bc49151
# Open PDF file
# with open('SOPRALLUOGHI DIC23_MAR24.pdf', 'rb') as file:
with open('Scheda-Bando-Donne-innovazione-e-impresa.pdf', 'rb') as file:

  # Create a PDF reader object
  reader = PyPDF2.PdfReader(file)
  
  # Get the number of pages in a PDF file.
  num_pages = len(reader.pages)
  
  # Extract text content page by page and print.
  for page_num in range(num_pages):
    page = reader.pages[page_num]
    text = page.extract_text()
    print(text)