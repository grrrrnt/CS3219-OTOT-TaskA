import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_lucky_number():
    lucky_number = random.randint(1, 100)
    return { "lucky_number": lucky_number }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')