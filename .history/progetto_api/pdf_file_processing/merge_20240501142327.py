from PyPDF2 import PdfMerger, PdfReader, PdfWriter

# Create a PDF merger
merger = PdfMerger()

# Merge multiple PDF files
merger.append('example.pdf')
merger.append('file2.pdf')

# Save the merged file.
merger.write('merged.pdf')
merger.close()

# Split a PDF file
with open('merged.pdf', 'rb') as file:
    reader = PdfReader(file)
    num_pages = len(reader.pages)
  
    # Split every 10 pages into one file.
    for start in range(0, num_pages, 10):
        end = min(start + 9, num_pages - 1)
        writer = PdfWriter()
    
        # Add specified range of pages to a new file.
        for page_num in range(start, end + 1):
            writer.add_page(reader.pages[page_num])
    
        # Save the split files.
        with open(f'part_{start+1}-{end+1}.pdf', 'wb') as output_file:
            writer.write(output_file)

print("Ta-da! The magic of merging and splitting is complete.！")