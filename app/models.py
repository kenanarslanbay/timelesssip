from . import db

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(32), nullable=False)
    description = db.Column(db.Text)