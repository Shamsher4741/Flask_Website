from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/learn+python'
db = SQLAlchemy(app)

#sno name email phone msg date 
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable= False)
    email = db.Column(db.String(20), nullable= False)
    p-no = db.Column(db.String(12), nullable= False)
    msg = db.Column(db.String(120), nullable= False)
    date = db.Column(db.String(12), nullable= False)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods = ['POST', 'GET']
def contact():
    return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True)