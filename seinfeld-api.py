from flask import Flask, jsonify
from random import randint
import pandas as pd

app = Flask(__name__)

@app.route('/api/random')
def random():
	return jsonify({'quote' : getRandomQuote()})

def getQuoteDict(quote):
	return {'Character': str(quote[0]),'Dialogue' : str(quote[1]), 'EpisodeNo' : str(quote[2]), 'SEID' : str(quote[3]), 'Season' : str(quote[4])}


def getRandomQuote():
	return getQuoteDict(scripts[randint(0,54615)])

if __name__ == '__main__':

	scripts = pd.read_csv('scripts.csv').drop('Index', axis=1).as_matrix()
	# print(len(scripts)) # 54616 -- gonna hardcode this
	app.run()
