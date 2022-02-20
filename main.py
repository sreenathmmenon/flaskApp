from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World! This is a test Flask App'

app.run(host='0.0.0.0', port=8080)
