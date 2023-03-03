FROM python:3.8
WORKDIR /FlaskApp-SampleApi
RUN pip install -r requirements.txt
COPY ./app ./app
CMD ["python","./app/flaskapp.py"]
