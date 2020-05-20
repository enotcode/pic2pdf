import os

from flask import Flask, request, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename

from helpers import allowed, converter

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist("file[]")
        if files and allowed(files):
            images = []
            for file in files:
                filename = secure_filename(file.filename)
                file.save(os.path.join('uploads/', filename))
                images.append('uploads/' + filename)
            converter(images)
            return redirect(url_for('uploaded_file',
                                    filename='test.pdf'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name="file[]" multiple="">
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads/',
                               filename)


if __name__ == '__main__':
    app.run()
