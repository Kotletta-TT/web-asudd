from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/grooty/PycharmProjects/flask-test/test.db'
app.config['SECRET_KEY'] = 'thisissecret'

db = SQLAlchemy(app)
login_manger = LoginManager()
login_manger.init_app(app)

EQUIPMENT = {'cam': 'Камеры',
             'co': 'Светофоры',
             'sdot': 'Остановочные табло',
             'puid': 'ПУИДы',
             'serv': 'Серверная'}

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Nodes(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    type = db.Column(db.String(10), nullable=False)
    latitude = db.Column(db.Float(10, 6))
    longitude = db.Column(db.Float(10, 6))
    ext_ip = db.Column(db.String(15))
    vpn_ip = db.Column(db.String(15))
    main_ip = db.Column(db.String(15))
    status = db.Column(db.String(10))
    description = db.Column(db.String(150))


@login_manger.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def start():
    nodes = Nodes.query.all()
    return render_template("index.html", nodes=nodes)

@app.route('/index')
@login_required
def index():
    return render_template("index.html")

@app.route('/co')
@login_required
def co():
    return render_template("co.html")

@app.route('/cam')
@login_required
def cam():
    return render_template("cam.html")

@app.route('/sdot')
@login_required
def sdot():
    return render_template("sdot.html")

@app.route('/puid')
@login_required
def puid():
    return render_template("puid.html")

@app.route('/serv')
@login_required
def serv():
    return render_template("serv.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "You are now logged out"


@app.route('/home')
@login_required
def home():
    return "Current user is " + current_user.username


@app.route('/login', methods=['POST'])
def login():
    enter_username = request.form.get("username")
    enter_password = request.form.get("password")
    user = User.query.filter_by(username=enter_username).first()
    if user:
        if user.password == enter_password:
            login_user(user)
            print("you are login")
            return index()
        else:
            error_message = "Password incorrect"
            if error_message:
                print(error_message)
            return render_template('login.html', error_message=error_message)
    else:
        error_message = "Login does not exists"
        if error_message:
            print(error_message)
        return render_template("login.html", error_message=error_message)


@app.errorhandler(401)
def not_autorised(e):
    # note that we set the 404 status explicitly
    return render_template('login.html')



def get_all_nodes():
     return


if __name__ == '__main__':
    app.run(debug=True)
