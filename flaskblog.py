from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'John Wich',
        'title': 'My dog',
        'content': 'my dog',
        'date_posted': 'April 1, 2020'
    },
    {
        'author': 'Jack Sparrow',
        'title': 'Black Pearl',
        'content': 'my ship',
        'date_posted': 'July 1, 2020'
    }
     
     
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)