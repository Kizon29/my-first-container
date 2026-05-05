from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Cloud Engineer! My container is running."

if __name__ == '__main__':
    # This tells the app to listen on all available networks
    app.run(host='0.0.0.0', port=5000)

#Test Commit