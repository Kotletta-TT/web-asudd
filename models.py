from app import db
from flask_login import UserMixin


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