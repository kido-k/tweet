FROM python:3.7.4
RUN pip install Flask python-dotenv
COPY main.py .
COPY ./app/ ./app
COPY ./public/ ./public
CMD ["python", "main.py"]
