from app import app,db
from config import *

from flask import render_template,flash,redirect,url_for,jsonify

from multiprocessing import Process,Value 


import urllib2
import urllib
import sys
import base64

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

#global variables

average = Value('i',0)



try:
	import json
except ImportError:
	import simplejson as json

@app.route('/')
def index():
	return render_template('landing.html')

	

@app.route('/start')
def start_process():
	global p
	
	if p is None:
		print("Trying to restart")
		p = Process(target=infinite,args=(average,))
	p.start()
	#p.join()

	return jsonify("ok")


@app.route('/stop')
def stop_process():
	global p

	if p.is_alive():
		average.value = 0
		p.terminate()
		p = None

	return jsonify("ok")	

@app.route('/update')
def update():
	#print('In update'+str(average.value))
	return jsonify(average.value)


def infinite(average):

	oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

	# Initiate the connection to Twitter Streaming API
	twitter_stream = TwitterStream(auth=oauth)

	# Get a sample of the public data following through Twitter
	iterator = twitter_stream.statuses.filter(track="#SPITElection")

	average.value = 0
	total=0	
	count=0
	tweet_count = 3
	fill_text=""
	id_count = 1
	input_texts = '{"documents":['
	end_text = "]}'"
	for tweet in iterator:
		tweet_count -= 1
		# Twitter Python Tool wraps the data returned by Twitter 
		# as a TwitterDictResponse object.
		# We convert it back to the JSON format to print/score


		if 'text' in tweet: # only messages contains 'text' field is a tweet
			received = tweet['text']
			input_texts = '{"documents":['
			end_text = "]}'"
			fill_text = '{"id":"%d","text":"%s"},'%(id_count,received)
			print received
			id_count +=1;
			

		# The command below will do pretty printing for JSON data, try it out
		# print json.dumps(tweet, indent=4)

			
		# Azure portal URL.
		base_url = 'https://westus.api.cognitive.microsoft.com/'
		# Your account key goes here.
		account_key = '9xxx....xxxxxf'

		headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}
				
		input_texts += fill_text + end_text
		print input_texts

		num_detect_langs = 1;

		'''# Detect key phrases.
		batch_keyphrase_url = base_url + 'text/analytics/v2.0/keyPhrases'
		req = urllib2.Request(batch_keyphrase_url, input_texts, headers) 
		response = urllib2.urlopen(req)
		result = response.read()
		obj = json.loads(result)
		for keyphrase_analysis in obj['documents']:
			#print('Key phrases ' + str(keyphrase_analysis['id']) + ': ' + ', '.join(map(str,keyphrase_analysis['keyPhrases'])))

		# Detect language.
		language_detection_url = base_url + 'text/analytics/v2.0/languages' + ('?numberOfLanguagesToDetect=' + num_detect_langs if num_detect_langs > 1 else '')
		req = urllib2.Request(language_detection_url, input_texts, headers)
		response = urllib2.urlopen(req)
		result = response.read()
		obj = json.loads(result)
		for language in obj['documents']:
			#print('Languages: ' + str(language['id']) + ': ' + ','.join([lang['name'] for lang in language['detectedLanguages']]))'''

		# Detect sentiment.
		batch_sentiment_url = base_url + 'text/analytics/v2.0/sentiment'
		req = urllib2.Request(batch_sentiment_url, input_texts, headers) 
		response = urllib2.urlopen(req)
		result = response.read()
		obj = json.loads(result)
		
		array_avg=[]
		array_time=[]
		for sentiment_analysis in obj['documents']:
			#print('Sentiment ' + str(sentiment_analysis['id']) + ' score: ' + str(sentiment_analysis['score']))
			#array_time.append(sentiment_analysis['created_at'])
			total+=sentiment_analysis['score']
			count+=1
			print("current "+str(sentiment_analysis['score'])+" total "+str(total)+" count"+str(count))
			average.value = int((total/count)*100)
			print(average.value)
			#print average
			#array_avg.append(average)



p = None



