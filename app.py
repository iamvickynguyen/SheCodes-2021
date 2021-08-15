from flask import Flask, render_template, request

app = Flask(__name__)

class User:
    def __init__(self, name):
        self.name = name

username = User('')

girls = [
    ('Nguyễn Cẩm Vân', '14', 'Thường xuyên bị cha đánh, quát mắng', 'Bạo lực gia đình'),
    ('N/A', '16', 'Em có nên phá thai?', 'Lạm dụng'),
    ('Bắp', '15', 'Bị thầy cô chửi ngu vì không hiểu bài', 'Học quá nhiều'),
    ('Tường Vân', '15', 'Em muốn nhận hỗ trợ học bổng để tiếp tục đi học', 'Học bổng'),
    ('Silo', '14', 'Ap luc hoc tap vi me la hieu truong cua truong, ban be soi moi, co lap', 'Hoc tap')
]

companions = [
    ('Cô Vành Khuyên', '38', 'Có thể lắng nghe và cho  các em giải pháp phù hợp', 'Tư vấn tâm lý'),
    ('Cô Thúy', '56', 'Hiểu các con', 'Tư vấn tâm lý'),
    ('Dũng', '40', 'Có thể tài trợ học bổng', 'Tài trợ học bổng'),
    ('Minh', '30', 'Tư vấn các vấn đề tâm lý (trầm cảm, áp lực bạn bè cùng trang lứa…)', 'Tư vấn tâm lý'),
    ('Hà', '25', 'Tư vấn pháp lý, quyền trẻ em', 'Tư vấn tâm lý')
]

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username.name = request.form.get('username')
        return render_template('home.html', people = companions if username.name == 'cutecookie' else girls, home = True, profile = False, matches = True, isgirl = username.name == 'cutecookie')
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('register.html')

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    return render_template('home.html', people = [], home = False, profile = False, matches = False, isgirl = username.name == 'cutecookie')

@app.route('/matches', methods=['POST', 'GET'])
def matches():
    return render_template('home.html', people = companions if username.name == 'cutecookie' else girls, home = True, profile = False, matches = True, isgirl = username.name == 'cutecookie')

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    return render_template('home.html', people = [girls[0]] if username.name == 'cutecookie' else [companions[0]], home = True, profile = True, matches = False, isgirl = username.name == 'cutecookie')

if __name__ == "__main__":
    app.run(debug=True)