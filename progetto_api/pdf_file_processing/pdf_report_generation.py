""" Dependency installation:

pip install pytesseract """
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer

# Create report content
def create_report(output_file, data):
    # Create PDF document object
    doc = SimpleDocTemplate(output_file, pagesize=A4)

    # Load stylesheet
    styles = getSampleStyleSheet()

    # Create report content elements
    elements = []

    # Add title
    title = Paragraph("Sales report", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 20))

    # Add table
    table_data = data
    table = Table(table_data)
    elements.append(table)
    elements.append(Spacer(1, 20))

    # Generate charts and save as PNG images
    plt.plot(data[1][1:], marker='o')
    plt.xlabel("date")
    plt.ylabel("Sales revenue")
    plt.title("Sales Trend Chart")
    plt.savefig("sales_plot.png")
    plt.close()

    # Add charts to the report content.
    image = Image("sales_plot.png", width=400, height=300)
    elements.append(image)

    # Generate report
    doc.build(elements)

# Create report data
report_data = [
    ["date", "Sales revenue"],
    ["1/1", 100],
    ["1/2", 200],
    ["1/3", 150],
    ["1/4", 300],
]

# Generate report
create_report('sales_report.pdf', report_data)

print("Table generation completed! Now you can view the generated report file.")