from flask import Flask, render_template, request
import pickle

cv = pickle.load(open('models/cv.pkl', 'rb'))
model = pickle.load(open('models/clf.pkl', 'rb'))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')



@app.route("/predict", methods=["POST"])
def predict():
    email_text = request.form.get('Email-Content')

    tokenized_email = cv.transform([email_text])
    prediction = model.predict(tokenized_email)
    output = "This email does not seem like a spam"

    if prediction == 1:
        output = "This email seems like a spam" 

    return render_template('index.html', predictions = output, text=email_text)


if __name__ == "__main__":
    app.run(port=8000, debug=True)