from flask import Flask, render_template
from markupsafe import escape
import os
from flask import send_from_directory

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/")
def index():
    return 'index'
    # return render_template('index.html',name=name)

@app.route("/software_development/")
def software_development():
    return 'software_development'

@app.route('/infrastrucutre')
def infrastructure(blog_id):
    return 'infrastrucutre'


# Possible templates
# https://html5up.net/landed
# https://html5up.net/forty
# https://html5up.net/ethereal
# PRE LAUNCH: https://html5up.net/eventually
