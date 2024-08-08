from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome_page():
    return (
        'Welcome to our store! We\'ve made exciting updates to ensure a smooth and seamless shopping experience during the Black Friday sales. Enjoy your shopping!'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)