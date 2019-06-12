import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Quick Access Libgen API</h1><p>This site is a prototype API for fetching download urls from libgen</p>"


@app.route('/books', methods=['GET'])
def api_id():
    if 'name' in request.args:
        bookName = int(request.args['id'])
    else:
        return "Error: Please Enter a book name"

    # Create an empty list for our results
    results = []
    return jsonify(results)


app.run()
