import datetime

from app.main import db


class Storage(db.Model):
    __tablename__ = "storage"

    storage_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    memo = db.Column(db.String(80), nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())

    def __init__(self, memo):
        self.memo = memo
