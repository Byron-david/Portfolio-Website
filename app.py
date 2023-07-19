from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout.html")

# @app.route("/sony")
# def index():
#     return render_template("sony.html")

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

if __name__== '__main__':
    app.run(debug=True)