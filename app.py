from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'name': "Nirbhay",
    'skill': "underdog",
    'nickname':"niru"
  },
  {
    'id': 2,
    'name': "Uttam",
    'skill': "CG",
    'nickname':"maggu"
  },
  {
    'id': 3,
    'name': "Abhinav",
    'skill': "ML GAWD",
    'nickname':"lavda"
  },
  {
    'id': 4,
    'name': "bishanka",
    'skill': "SCORER",
    'nickname':""
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                        jobs=JOBS,
                        company_name="FOLKS")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0' , debug=True)