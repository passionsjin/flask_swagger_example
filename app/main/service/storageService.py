from app.main import db
from app.main.model.storage import Storage


def save_storage(number):
    storage = Storage(number)
    db.session.add(storage)
    db.session.commit()
    return storage


def get_all_storage():
    return Storage.query.all()
