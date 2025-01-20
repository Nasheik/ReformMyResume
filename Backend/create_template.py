from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_sample_template(output_path="template.pdf"):
    """
    Creates a sample template PDF with placeholders for Name, Email, and Phone.
    """
    c = canvas.Canvas(output_path, pagesize=letter)

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Resume Information Template")

    # Placeholder fields
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, "Name: ____________________________")
    c.drawString(100, 680, "Email: ___________________________")
    c.drawString(100, 660, "Phone: ___________________________")

    # Add more placeholders if needed
    c.drawString(100, 620, "Skills: __________________________")
    c.drawString(100, 600, "Experience: ______________________")

    # Save the PDF
    c.save()
    print(f"Sample template saved as '{output_path}'")

if __name__ == "__main__":
    create_sample_template()
