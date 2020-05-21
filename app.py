import os

from flask import Flask, request, send_from_directory, render_template
from werkzeug.utils import secure_filename

from helpers import allowed, converter

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist('file[]')
        if files and allowed(files):
            images = []
            for file in files:
                filename = secure_filename(file.filename)
                file.save(os.path.join('uploads/', filename))
                images.append('uploads/' + filename)
            fname = converter(images)
            return render_template('download.html', fname=fname)
    return render_template('index.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads/',
                               filename)


if __name__ == '__main__':
    app.run()
