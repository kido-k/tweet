from flask import Flask, Response, request
import json

from app import get_tweet_data
from app import analyze_tweet_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
  res = {'message': 'hello world'}
  return Response(response=json.dumps(res), status=200)

@app.route('/tweet_analyze', methods=['POST'])
def analyze_tweet():
  post_data = request.data.decode('utf-8')
  post_data = json.loads(post_data)
  print(post_data['keyword'])
  print(post_data['use_retweet'])
  try:
    get_tweet_data.get_tweet_data(post_data['keyword'], post_data['use_retweet'])
    result = analyze_tweet_data.analyze_tweet_data()
    return Response(response=json.dumps(result), status=200)
  except expression as identifier:
    return Response(response=json.dumps(''), status=500)

@app.errorhandler(404)
def error_404(e):
    res = 'httpステータス:{}, メッセージ:{}, 詳細:{}'.format(e.code, e.name, e.description)
    return Response(response=json.dumps(res), status=404)

@app.errorhandler(500)
def error_500(e):
    res = 'httpステータス:{}, メッセージ:{}, 詳細:{}'.format(e.code, e.name, e.description)
    return Response(response=json.dumps(res), status=500)