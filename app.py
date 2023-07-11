from flask import Flask, render_template, jsonify
from database import load_jobs, load_job

app = Flask(__name__)
    

@app.route("/")
def index():
    return render_template("home.html", jobs=load_jobs(), company_name= "Zokmon")

@app.route("/job/<id>")
def show_job(id):
    job = load_job(id)
    if not job:
        return "Page not found", 404
        
    return render_template("jobpage.html", job=job)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
