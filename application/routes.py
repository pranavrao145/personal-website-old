from . import app, mail
from flask_mail import Message
from flask import url_for, render_template, redirect, flash, current_app, send_from_directory
from .forms import ContactMeForm
import os


@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    form = ContactMeForm()
    if form.validate_on_submit():
        msg = Message(subject="Email From Personal Website", recipients=[os.environ.get('EMAIL_RECIPIENT')])
        msg.body = f'''Name of sender: {form.name.data}
Return email address: {form.email.data}

Message:
{form.message.data}
'''
        mail.send(msg)
        flash("Your message has been sent successfully.", "is-success")
        return redirect(url_for('home'))
    return render_template("home.html", title="Home", form=form)


@app.route('/all_projects')
def all_projects():
    return render_template("all_projects.html", title="All Projects")


# the download mechanism does not work as yet
@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename)


@app.route('/about_me')
def about_me():
    return render_template("about.html")