from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def current_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)
    profile = db.relationship('Profile', backref='user', uselist=False)

    def __str__(self):
        return self.name

class Profile(db.Model):
    __tablename__ = "profiles"
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.Unicode(124), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __str__(self):
        return self.name

class Instituicao(db.Model):
    __tablename__ = "instituicao"
    id = db.Column(db.Integer, primary_key=True)
    nameinst = db.Column(db.Unicode(124), nullable=False)
    enderecoinst = db.Column(db.Unicode(124), nullable=False)
    donoinst1 = db.Column(db.Unicode(124), nullable=False)
    donoinst2 = db.Column(db.Unicode(124))
    donoinst3 = db.Column(db.Unicode(124))
    tipodoacao = db.Column(db.Unicode(124), nullable=False)
    descricao = db.Column(db.Unicode(2000),nullable=False)


    def __str__(self):
        return self.name
    

