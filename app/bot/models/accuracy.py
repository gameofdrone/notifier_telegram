from app import db

class Accuracy(db.Model):
    """ Accuracy Model for storing accuracy related details"""
    __tablename__ = "accuracy"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.Float, primary_key=False)
    epoch = db.Column(db.Integer, primary_key=False)

    def __repr__(self):
        return f"<Accuracy '{self.value}'>"
