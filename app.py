from flask import Flask, render_template, request
from flask_dropzone import Dropzone
from app.utils.IO_DIR import Handler

import os

app = Flask (__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config.update(
    UPLOADED_PATH = os.path.join(os.path.join(basedir,'uploads')),
    DROPZONE_MAX_FILE_SIZE = 1024,
    DROPZONE_TIMEOUT = 5*50*1000
)
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = '.json'

dropzone = Dropzone(app)

@app.route("/", methods=["POST", "GET"])
def file_uploads ():

    if request.method == 'POST':

        # Getting the files
        file = request.files.get('file')
        # Saving file
        file.save(os.path.join(app.config['UPLOADED_PATH'],file.filename))
        handler = Handler(os.path.join(app.config['UPLOADED_PATH'],file.filename))
        handler.extract_aspect_from_reviews ()
        handler.export_all_aspect()

    return render_template("/main.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
