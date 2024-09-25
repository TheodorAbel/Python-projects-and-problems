from fpdf import FPDF


class ShirtificatePDF(FPDF):
    def header(self):
        # Set font
        self.set_font('Arial', 'B', 16)
        # Title
        self.cell(0, 10, 'CS50 Shirtificate', ln=True, align='C')
        # Line break
        self.ln(10)

    def footer(self):

        self.set_y(-15)
        # Set font
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_shirtificate(name: str, output_path: str = "shirtificate.pdf"):
    # Create instance of FPDF class
    pdf = ShirtificatePDF(orientation='P', unit='mm', format='A4')

    pdf.add_page()

    pdf.set_auto_page_break(auto=False)

    pdf.image("shirtificate.png", x=0, y=60, w=210)
    pdf.set_xy(0, 110)
    pdf.set_font("Arial", 'B', 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(210, 10, name, ln=True, align='C')
    pdf.output(output_path)

def main():

    name = input("Enter your name: ")
    create_shirtificate(name+" took CS50 ")

if __name__ == "__main__":
    main()
