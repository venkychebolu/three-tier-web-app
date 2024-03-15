from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    age = db.Column(db.Integer)
    dob = db.Column(db.Date)

    def __repr__(self):
        return f'<User {self.name}>'
