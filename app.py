from flask import Flask, render_template
import os

app = Flask(__name__)

google_video = os.listdir('static/google/minitaur')

google_folder = os.listdir('static/google/')
google_folder.sort()

sony_folder = os.listdir('static/sony/')
sony_folder.sort()

hallmark_folder = os.listdir('static/hallmark/')
hallmark_folder.sort()

personal_folder = os.listdir('static/personal/')
personal_folder.sort()

design_folder = os.listdir('static/2d/')
design_folder.sort()

@app.route("/")
def index():
    return render_template("layout.html", 
                           google_folder=google_folder,
                           google_video=google_video,
                           sony_folder=sony_folder, 
                           hallmark_folder=hallmark_folder, 
                           personal_folder=personal_folder,
                           design_folder=design_folder)