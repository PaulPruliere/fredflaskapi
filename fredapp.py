import os
from flask import Flask, render_template
from fetching import fetcher

app = Flask(__name__)
app.debug = True


@app.route('/', defaults={'path': ''})
@app.route('/probabilities/<path:path>')
def probabilities(path):
	spreadsheet = "dataset-code-challenge - personalities_data.csv"
	data = fetcher(path,spreadsheet)
	return render_template("probabilities.html",data=data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)