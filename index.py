from flask import *


app = Flask(__name__)

name = ''
login = ''
@app.route('/<int:id>', methods=['GET', 'POST'])
@app.route('/', methods=('GET', 'POST'))
def index(id=None):
    global name, login
    if request.method == 'POST':
        if request.form.get('account') == 'xiaoloveyuan' and request.form.get('pwd') == '1314':
            login = 'success'
            name = 'admin'
            return render_template('1.html', name=name, login=login)
        else:
            login = 'fail'
        if id ==1201:
            return render_template('index.html')
        if id ==1314:
            return render_template('3.html')
    if id == 520:
        return render_template('hellow.html')
    return render_template('404.html')

if __name__ == '__main__':
    app.run()