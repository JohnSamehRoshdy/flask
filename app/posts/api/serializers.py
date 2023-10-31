from flask_restful import fields


# id = db.Column(db.Integer,primary_key = True)
#     title = db.Column(db.String)
#     body = db.Column(db.String)
#     image = db.Column(db.String)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
#     category_id 

category_serializer ={
    "id":fields.Integer,
    "name":fields.String,
    "desc":fields.String   
}



post_serializer={
    "id":fields.Integer,
    "title":fields.String,
    "body":fields.String,
    "image":fields.String,
    "created_at":fields.DateTime,
    "updated_at":fields.DateTime,
    "category_id":fields.Integer,
    "category":fields.Nested(category_serializer)
}

