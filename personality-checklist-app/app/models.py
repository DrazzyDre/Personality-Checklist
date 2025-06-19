from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PersonalityChecklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(50), nullable=False)

class Apostle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    traits = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Apostle {self.name}>'