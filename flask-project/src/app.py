from flask import Flask, render_template
import redis

app = Flask(__name__)

r = redis.Redis(host='cache', port=6379, db=0)

@app.route('/')
def index():
	r.incr('hits', amount=1)
	hits = int(r.get('hits').decode('utf-8'))
	return render_template("index.html", hits=hits)

if __name__ == '__main__':
	app.run(debug=True)