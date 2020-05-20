from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('disaster_tweet_app.html')

if __name__ == '__main__':
    app.run()
