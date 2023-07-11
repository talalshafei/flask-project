from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": 'Data Analyst',
    "location": "Jenin, Palestine",
    "salary": "1000 USD",
  },
  {
    "id": 2,
    "title": 'Data Scientist',
    "location": "Nabuls, Palestine",
    "salary": "2000 USD",
  },
  {
    "id": 3,
    "title": 'Data Engineer',
    "location": "Ramallah, Palestine",
    "salary": "1000 USD",
  },
  {
    "id": 4,
    "title": 'Data Architect',
    "location": "Nablus, Palestine",
    "salary": "2000 USD",
  },
]


@app.route("/")
def hello():
  return render_template("home.html", jobs=JOBS, company_name= "Zokmon")

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
