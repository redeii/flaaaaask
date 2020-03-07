
from flask import Flask, render_template, url_for
app = Flask(__name__)

ayaya = [
    {
        'author':'Pedro Gomes',
        'title':'Blog Post 1',
        'content':'First post Content',
        'date_posted':'March 3, 2020'       
    },
    {
        'author':'Jane Dow',
        'title':'Blog Post 2',
        'content':'Second post Content',
        'date_posted':'March 30, 2020' 
    },
    {
        'author':'Pedro Gomes',
        'title': 'Preguicaaaa JUUUUUUUUUU',
        'content': 'to fazendo sitezinho',
        'date_posted': 'Hoje mesmo'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=ayaya)

@app.route('/about')
def about():
    return render_template('about.html',title='About')


if __name__ == '__main__':
    app.run(debug=True)