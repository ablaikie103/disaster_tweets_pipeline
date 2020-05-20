from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import numpy as np
"""
clf = pickle.load(open('classifier/trained_classifier.pkl'))

def label_tweet(tweet):
    y = clf.predict(tweet)
    return y
"""
app = Flask(__name__)

class HelloForm(Form):
    sayhello = TextAreaField('', [validators.DataRequired()])

@app.route('/')
def index():
    form = HelloForm(request.form)
    return render_template('disaster_tweet_app.html', form=form)

@app.route('/hello', methods=['POST'])
def hello():
    form = HelloForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['sayhello']
        return render_template('hello.html', name=name)
    return render_template('disaster_tweet_app.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
