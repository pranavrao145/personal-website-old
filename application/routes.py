from . import app, mail
from flask_mail import Message
from flask import url_for, render_template, redirect, flash
from .forms import ContactMeForm
from os import environ


@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    form = ContactMeForm()
    if form.validate_on_submit():
        msg = Message(subject="Email From Personal Website", recipients=[environ.get('EMAIL_RECIPIENT')])
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
    return render_template("all_projects.html", title="All Projects ")