from flask import Flask,render_template


app = Flask(__name__)


@app.route('C:\Users\madhumitha\OneDrive\Desktop\Plasma donor\templates\signin.html')
def home():
    return render_template("signin.html")
@app.route('C:\Users\madhumitha\OneDrive\Desktop\Plasma donor\templates\signup.html')
def sign_up():
    return render_template("signup.html")
@app.route('C:\Users\madhumitha\OneDrive\Desktop\Plasma donor\templates\home.html')
def ho():
    return render_template("home.html")
@app.route('C:\Users\madhumitha\OneDrive\Desktop\Plasma donor\templates\about.html')
def about():
    return render_template("about.html")
if __name__ == '__main__':
    app.run(debug=True)
