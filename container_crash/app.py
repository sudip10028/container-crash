
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  a=10
  b=0
  print(a/b)
  return 'Hello, Docker!'

