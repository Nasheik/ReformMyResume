import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import pikepdf


def insert_data_into_pdf(template_path, output_path, data):
    """
    Insert data into a PDF template and save the result using pikepdf.
    
    Args:
        template_path (str): Path to the PDF template.
        output_path (str): Path to save the filled PDF.
        data (dict): Dictionary with extracted data to insert (e.g., name, email, phone).
    """
    # Create an overlay PDF in memory with the data
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

    # Open the template PDF using pikepdf
    with pikepdf.open(template_path) as template_pdf:
        # Load the overlay created with ReportLab
        overlay_pdf = pikepdf.Pdf.open(packet)

        # Iterate through template pages and overlay the content
        for template_page, overlay_page in zip(template_pdf.pages, overlay_pdf.pages):
            template_page.add_overlay(overlay_page)

        # Save the filled PDF
        template_pdf.save(output_path)
        print(f"Data inserted into '{output_path}'")


if __name__ == "__main__":
    # Example usage
    template_path = "template.pdf"  # Path to your template PDF
    output_path = "filled_output.pdf"  # Output file name
    extracted_data = {
        "name": "Jn Doe",
        "email": "jodoe@example.com",
        "phone": "1234890",
    }
    insert_data_into_pdf(template_path, output_path, extracted_data)
