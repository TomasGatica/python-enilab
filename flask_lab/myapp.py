from flask import Flask, render_template
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'debugdatabase1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
#   to complete the initialization we create an object od the SQLAlchemy class
#   we provide our application as a parameter to its constructor
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        for u_email, u_password in users.items():
            if u_email == form.email.data and u_password == form.password.data:
                return render_template("login", message = "Successfully Logged In")
        return render_template("login", message = "Incorrect Email or Password")
    elif form.errors:
        print(form.errors.items())
    return render_template("login.html", form = form)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
