import os

from app import db
from app.bot.models.accuracy import Accuracy


def add_accuracy(result: dict):
    new_accuracy = Accuracy(
        value=result['value'],
        epoch=result['epoch']
    )
    save_changes(new_accuracy)
    response_object = {
        'status': 'success',
        'message': 'Successfully added accuracy.'
    }
    return response_object, 201

def get_all_accuracy():
    return Accuracy.query.all()

def get_best_accuracy():
    # TODO: release function that return best accuracy
    pass

def save_changes(data):
    db.session.add(data)
    db.session.commit()

# TODO add bot with aiogram
# TODO add func "send_message"
