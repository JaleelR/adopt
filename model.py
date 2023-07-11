from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    "connect to database"
    db.app = app
    db.init_app(app)


class Pet(db.Model):
        __tablename__ = "pets"

        id = db.Column(db.Integer, primary_key = True, autoincrement =True)
        name = db.Column(db.Text, nullable = False)
        species = db.Column(db.Text)
        photo_url = db.Column(db.Text, nullable = True)
        age = db.Column(db.Integer, nullable = True)
        notes = db.Column(db.Text, nullable = True)
        available = db.Column(db.Boolean, default=True)
        def __repr__(self):
            return f"id:{self.id}, name:{self.name}, species:{self.species}, age: {self.age}, available: {self.available}"
            