from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:hGBFGg2BhFa4hbgbghEeD46AHE6b-BHb@viaduct.proxy.rlwy.net/railway'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy(app)
class users(db.Model):
    id = db.Column('user_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))

def __init__(self, name):
    self.name = name

@app.route('/')
def index():
    title = 'Deployment Test'
    return render_template('index.html', title=title, users = users.query.all())

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=os.getenv("PORT", default=80))