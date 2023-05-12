from flask_restful import Resource, reqparse, inputs
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User, Message
from app.api.validators.address import validate_address_data
from datetime import datetime


class MessageApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("receiver_mail", required=True, type=str)
    parser.add_argument("title", required=True, type=str )
    parser.add_argument("content", required=True, type=str)
    parser.add_argument("file_path", required=False, type=str)

    @jwt_required()
    def post(self):
        args = self.parser.parse_args()
        current_user = get_jwt_identity()
        
        sender = User.query.filter_by(email=current_user).first()
        receiver =  User.query.filter_by(email=args["receiver_mail"]).first()

        if not sender.check_permission("can_send_message") and not receiver.check_permission("can_send_message"):
            return "Bad request", 400
        
        message = Message(sender=sender.id, 
                          receiver=receiver.id,
                          title=args["title"],
                          content=args["content"],
                          file_path=args["file_path"],
                          date=datetime.now())
        message.create()
        message.save()

        return "Success", 200
    
    @jwt_required()
    def get(self):

        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()
        sent_msg = Message.query.filter_by(sender=user.id).all()  #sent message
        received_msg = Message.query.filter_by(receiver=user.id).all() #received message 

        if not user.check_permission("can_send_message"):
            return "Bad request", 400        


        sent_messages = [{ "title" : item.title, 
                          "content":item.content, 
                          "file_path":item.file_path, 
                          "date":item.date} for item in sent_msg]
        received_messages = [{ "title" : item.title,
                               "content":item.content, 
                               "file_path":item.file_path, 
                               "date":item.date} for item in received_msg]
        data = {
            "sent messages": sent_messages,
            "received messages": received_messages
        }

        
        return data,200
            


        
        
        



        
        



