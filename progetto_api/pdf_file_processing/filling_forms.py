from PyPDF2 import PdfReader, PdfWriter

from reportlab.pdfgen import canvas

# Automatically fill in form fields
def fill_form(input_file, output_file, data):
    c = canvas.Canvas(output_file)
    c.setFont("Helvetica", 12)
    
    # Read input file, process page by page.
    reader = PdfReader(input_file)
    for page_num, page in enumerate(reader.pages, start=1):
        # Obtain the size of the page and create a canvas of corresponding size.
        page_width = float(page.mediabox.width)
        page_height = float(page.mediabox.width)
        c.setPageSize((page_width, page_height))
        
        # Draw page content
        c.showPage()
        
        # Check if the page has form fields.
        if '/Annots' in page:
            # Traverse all form fields
            for annot in page['/Annots']:
                # Check the field type as text area.
                if '/T' in annot and '/V' in annot and annot['/Type'] == '/Annot':
                    field_name = annot['/T'][1:-1]  # Get field name
                    # Replace the field value with the incoming data.
                    if field_name in data:
                        field_value = data[field_name]
                        c.drawString(annot['/Rect'][0], annot['/Rect'][1], field_value)
    
    # Save the PDF with filled data.
    c.save()

# Read the filled data.
def read_form_data(input_file):
    data = {}
    reader = PdfReader(input_file)
    
    # Traverse all pages.
    for page in reader.pages:
        # Check if there are form fields.
        if '/Annots' in page:
            # Traverse all form fields
            for annot in page['/Annots']:
                # Check the field type as text area.
                if '/T' in annot and '/V' in annot and annot['/Type'] == '/Annot':
                    field_name = annot['/T'][1:-1]  # Get field name
                    field_value = annot['/V'][1:-1] if isinstance(annot['/V'], str) else ''
                    data[field_name] = field_value
    
    return data

# Create a new PDF form
def create_form(output_file, data):
    c = canvas.Canvas(output_file)
    c.setFont("Helvetica", 12)
    
    # Add data line by line to the form.
    y = 800
    for field, value in data.items():
        c.drawString(50, y, f"{field}: {value}")
        y -= 20
    
    # Save form
    c.save()

# Fill in the form fields and save.
fill_form('form_template.pdf', 'filled_form.pdf', {'name': 'joe', 'age': '18'})

# Read the filled data and print.
form_data = read_form_data('filled_form.pdf')
print(form_data)

# Create a new PDF form
create_form('my_form.pdf', {'name': 'joe', 'age': '18'})

print("Magic completed! Now you can easily handle PDF forms!")
