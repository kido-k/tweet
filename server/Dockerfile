FROM python:3.7.4
RUN pip install Flask flask-cors python-dotenv tweepy mecab-python3 matplotlib japanize-matplotlib
COPY main.py .
COPY ./app/ ./app
CMD ["python", "main.py"]
