from flask import Flask, render_template, jsonify
from database import load_jobs

app = Flask(__name__)
    

@app.route("/")
def index():
    return render_template("home.html", jobs=load_jobs(), company_name= "Zokmon")


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
