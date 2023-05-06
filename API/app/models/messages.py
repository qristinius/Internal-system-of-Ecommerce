from app.extensions import db
from app.models.base import BaseModel


class Message(BaseModel):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key = True)
    sender = db.Column(db.Integer, db.ForeignKey("registered_users.id"))
    receiver = db.Column(db.Integer, db.ForeignKey("registered_users.id"))
    title = db.Column(db.String)
    content = db.Column(db.Text)
    file_path = db.Column(db.String)
    date = db.Column(db.Text)
    deleted = db.Column(db.Boolean, default = False)
    delete_date = db.Column(db.Text)

    sender_ref = db.relationship("User", backref = "sent_message", foreign_keys=[sender])
    receiver_ref = db.relationship("User", backref = "recieved_message", foreign_keys=[receiver])


    
    


    

