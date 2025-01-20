from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def insert_data_into_pdf(template_path, output_path, data):
    """
    Insert data into a PDF template and save the result.
    
    Args:
        template_path (str): Path to the PDF template.
        output_path (str): Path to save the filled PDF.
        data (dict): Dictionary with extracted data to insert (e.g., name, email, phone).
    """
    # Create a PDF in memory with the data
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    # Example positions (adjust based on your template)
    can.drawString(100, 700, f"Name: {data.get('name', '')}")
    can.drawString(100, 680, f"Email: {data.get('email', '')}")
    can.drawString(100, 660, f"Phone: {data.get('phone', '')}")

    # Add more fields as necessary...
    can.save()

    # Move the in-memory PDF to the start
    packet.seek(0)

    # Read the template PDF
    template_pdf = PdfReader(template_path)
    new_pdf = PdfReader(packet)
    output_pdf = PdfWriter()

    # Merge the in-memory PDF onto the template
    for page_num, page in enumerate(template_pdf.pages):
        page.merge_page(new_pdf.pages[0])  # Merge the first (and only) page of the new PDF
        output_pdf.add_page(page)

    # Save the result
    with open(output_path, "wb") as output_file:
        output_pdf.write(output_file)

if __name__ == "__main__":
    # Example usage
    template_path = "template.pdf"  # Path to your template PDF
    output_path = "filled_output.pdf"  # Output file name
    extracted_data = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "1234567890",
    }
    insert_data_into_pdf(template_path, output_path, extracted_data)
    print(f"Data inserted into {output_path}")
