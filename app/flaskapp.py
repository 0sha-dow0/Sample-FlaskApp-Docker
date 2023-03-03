from flask import Flask
import service

app = Flask(__name__)

@app.route("/")
def initial():
     return str(service.RandomNumberGen())


if __name__ =='__main__':
    app.run(debug = True,port=5000,host="0.0.0.0")