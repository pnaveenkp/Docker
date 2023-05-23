from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_geek():
   return '<h1>Hello from Flask & Docker</h2>'
@app.route('/megastar')
@app.route('/powerstar')
@app.route('/megapowerstar')
def mega():
   return '<h1>Welcome to MegaFamily!......</h2>'
@app.route('/superstar')
def super():
   return '<h1>Welcome to SuperstarFamily</h2>'
@app.route('/rebelstar')
def rebel():
   return '<h1>Welcome to RebelstarFamily</h2>'


if __name__ == "__main__":
   app.run(debug=True)
