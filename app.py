from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    examples = [
        {
            'title': 'descriptivism.py',
            'embed_url': 'github.com/elimisteve/exphilorg/blob/master/templates/code/descriptivism.py',
            'output': render_template('code/descriptivism.out'),
        },
        {
            'title': 'direct_reference.py',
            'embed_url': 'github.com/elimisteve/exphilorg/blob/master/templates/code/direct_reference.py',
            'output': render_template('code/direct_reference.out'),
        },
        {
            'title': 'voting.py',
            'embed_url': 'github.com/elimisteve/exphilorg/blob/master/templates/code/voting.py',
            'output': render_template('code/voting.out'),
        },
    ]
    return render_template('index.html', examples=examples)


if __name__ == '__main__':
    app.run(debug=True)
