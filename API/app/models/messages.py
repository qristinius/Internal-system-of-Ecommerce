from app.extensions import db
from app.models.base import BaseModel


class Message(BaseModel):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key = True)
    sender = db.Column(db.Integer, db.ForeignKey("registered_users.id"))
    reciever = db.Column(db.Integer, db.ForeignKey("registered_users.id"))
    message = db.Column(db.Text)
    file_path = db.Column(db.String)
    date = db.Column(db.Text)
    deleted = db.Column(db.Boolean, default = False)
    sender_ref = db.relationship("User", backref = "sent_message", foreign_keys=[sender])
    receiver_ref = db.relationship("User", backref = "recieved_message", foreign_keys=[reciever])


class Reply(BaseModel):
    __tablename__ = "replies"

    id = db.Column(db.Integer, primary_key = True)
    replying = db.Column(db.Integer, db.ForeignKey("messages.id"))
    reply = db.Column(db.Integer, db.ForeignKey("messages.id"))

    
    


    

