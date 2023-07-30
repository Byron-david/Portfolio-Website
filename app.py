from flask import Flask, render_template
import os

app = Flask(__name__)

sony_folder = os.listdir('static/sony/')
sony_folder.sort()

hallmark_folder = os.listdir('static/hallmark/')
hallmark_folder.sort()

personal_folder = os.listdir('static/personal/')
personal_folder.sort()

@app.route("/")
def index():
    return render_template("layout.html", sony_folder=sony_folder, hallmark_folder=hallmark_folder, personal_folder=personal_folder)