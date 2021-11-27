from flask import Flask,jsonify
import csv

stars = []
with open('main.csv','r') as f:
    reader = csv.reader(f)
    data = list(reader)
    stars = data[1:]

app = Flask(__name__)

@app.route('/data')
def get_data():
    return jsonify({
        'data':stars,
        'status':'sucess'
    })

if __name__ == "__main__":
    app.run()