from fpdf import FPDF

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'heic'}


def allowed(files):
    for file in files:
        if '.' in file.filename and file.filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS:
            return True


def converter(images):
    pdf = FPDF()
    for i in images:
        pdf.add_page()
        pdf.image(i, x=10, y=8, w=190)
        pdf.set_font("Arial", size=12)
        pdf.ln(85)
    pdf.output("uploads/test.pdf")
