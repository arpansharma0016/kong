from flask import Flask, request, send_file, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

upload_folder = "uploads/"
if not os.path.exists(upload_folder):
   os.mkdir(upload_folder)

app.config['UPLOAD_FOLDER'] = upload_folder

class Upload(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	filename = db.Column(db.String(100))

with app.app_context():
	db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		file = request.files['file']
		if not file:
			return "Please enter a file"
		upload = Upload(filename=file.filename)
		db.session.add(upload)
		db.session.commit()
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
		return f'Uploaded: {file.filename}\nURL: http://localhost:8000/download/{upload.id}'
	return render_template('index.html')
	
@app.route('/url/<filename>')
def url(filename):
	upload = Upload.query.filter_by(filename=filename).first()
	if upload:
		return f"http://localhost:8000/download/{upload.id}"
	else:
		return "Asset not found"

@app.route('/download/<upload_id>')
def download(upload_id):
	upload = Upload.query.filter_by(id=upload_id).first()
	if upload:
		return send_file(os.path.join(app.config['UPLOAD_FOLDER'], upload.filename), as_attachment=True)
	else:
		return "Asset not found"


if __name__ == "__main__":
    app.run(port=5000, debug=True)