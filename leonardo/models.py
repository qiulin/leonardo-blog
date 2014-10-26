from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username


class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sitename = db.Column(db.String)
    rooturl = db.Column(db.String)

    def __init__(self, sitename, rooturl):
        self.sitename = sitename
        self.rooturl = rooturl

    def __repr__(self):
        return '<Site %r>' % self.sitename


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    slug = db.Column(db.String)
    md = db.Column(db.String)
    html = db.Column(db.String)

    def __init__(self, title, slug, md, html):
        self.title = title
        self.slug = slug
        self.md = md
        self.html = html

    def __repr__(self):
        return '<Post %r>' % self.title
