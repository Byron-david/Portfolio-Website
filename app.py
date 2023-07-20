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

# @app.route("/sony")
# def index():
#     return render_template('sony.html')

# @app.route("/hallmark")
# def index():
#     return render_template("hallmark.html")


# @app.route("/google")
# def index():
#     return render_template("google.html")


# @app.route("/personal")
# def index():
#     return render_template("personal.html")


# @app.route("/contact")
# def index():
#     return render_template("contact.html")

# if __name__== '__main__':
#     app.run(debug=True)