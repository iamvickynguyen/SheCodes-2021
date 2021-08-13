from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # TODO
        people = [('static/img/i1.jpg', 'Person 1', 'some descriptions'),
                    ('static/img/i2.jpg', 'Person 2', 'some descriptions'),
                    ('static/img/i3.jpg', 'Person 3', 'some descriptions'),
                    ('static/img/i4.jpg', 'Person 4', 'some descriptions'),
                    ('static/img/i5.jpg', 'Person 5', 'some descriptions'),
                    ('static/img/i6.jpg', 'Person 6', 'some descriptions')]
        return render_template('home.html', people = people)
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)