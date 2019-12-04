
#from flask import url_for
from app import db




class Task(db.Model):

    task_id = db.Column(db.Integer, primary_key=True)
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))
    task_start = db.Column(db.Date)
    task_end = db.Column(db.Date)
    task_location = db.Column(db.String(128))
    task_customer = db.Column(db.String(128))