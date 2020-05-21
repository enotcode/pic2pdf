import random
import string

from fpdf import FPDF

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'heic'}


def allowed(files):
    for file in files:
        if '.' in file.filename and file.filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS:
            return True


def name_generator():
    return "".join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(6))


def converter(images):
    pdf = FPDF()
    for i in images:
        pdf.add_page()
        pdf.image(i, x=10, y=8, w=190)
    name = name_generator() + '.pdf'
    pdf.output('uploads/' + name)
    return name
