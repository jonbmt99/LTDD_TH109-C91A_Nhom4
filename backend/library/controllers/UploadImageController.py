import os

from config import ALLOWED_EXTENSIONS
from library import app, db
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from library.DAL.models import Books


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/book-store')
def upload_form():
    return render_template('upload.html')


@app.route('/upload_book_image', methods=['POST'])
def upload_image():
    book_id = request.form.get("book_id")
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No uploads selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully uploaded and displayed')

        user_image = Books.query.get(book_id)
        file.filename =user_image.book_name
        user_image.image = file.filename

        db.session.add(user_image)
        db.session.commit()
        return render_template('upload.html', filename=filename)
    else:
        flash('Allowed uploads types are -> png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run()
