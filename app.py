from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return render_template('home.html')
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)