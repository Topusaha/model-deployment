from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    email = ""
    if request.method == "POST":
        email = request.form.get('Email-Content')

    return render_template('index.html', text=email)


if __name__ == "__main__":
    app.run(port=8000, debug=True)