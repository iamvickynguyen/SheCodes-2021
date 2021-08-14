from flask import Flask, render_template, request

app = Flask(__name__)

class User:
    def __init__(self, name):
        self.name = name

username = User('')

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username.name = request.form.get('username')
        people = []
        if username.name != 'cutecookie':
            people = [('Person 1', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
                    ('Person 2', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
                    ('Person 3', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
                ]
        else:
            people = [('Person 1', 'my strengths: bla bla bla...'),
                    ('Person 2', 'my strengths: bla bla bla...'),
                    ('Person 3', 'my strengths: bla bla bla...')
                ]
        return render_template('home.html', people = people, home = True, profile = False)
    return render_template('login.html')

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    return render_template('home.html', people = [], home = False, profile = False)

@app.route('/matches', methods=['POST', 'GET'])
def matches():
    if username.name != 'cutecookie':
        people = [('Person 1', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
                ('Person 2', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
                ('Person 3', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
            ]
    else:
        people = [('Person 1', 'my strengths: bla bla bla...'),
                ('Person 2', 'my strengths: bla bla bla...'),
                ('Person 3', 'my strengths: bla bla bla...')
            ]
    return render_template('home.html', people = people, home = True, profile = False)

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    if username.name == 'cutecookie':
        people = [('Cute Cookie', 'I am a cute cookie!')]
    else:
        people = [(username.name, 'my strengths: bla bla bla...')]
    return render_template('home.html', people = people, home = True, profile = True)

if __name__ == "__main__":
    app.run(debug=True)