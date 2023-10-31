from flask_restful import Resource,marshal_with
from app.models import Post,db
from app.posts.api.serializers import post_serializer
from flask import request
from flask_restful import reqparse
from app.posts.api.parsers import post_request_parser


class PostListClass(Resource):
    @marshal_with(post_serializer)
    def get(self):
        posts = Post.get_all_posts() 
        return posts
    
    @marshal_with(post_serializer)
    def post(self):
        print(request.form)
        post_args = post_request_parser.parse_args()
        print(post_args)
        post = Post.save_post(post_args)
        
        return post,201
    
    
class PostResource(Resource):
    
    @marshal_with(post_serializer)
    def get(self,post_id):
        post = Post.get_specific_post(post_id)
        return post,200
            
    
    @marshal_with(post_serializer)
    def put(self,post_id):
        post = Post.get_specific_post(post_id)
        post_args = post_request_parser.parse_args()
        post.title = post_args['title']
        post.body = post_args['body']
        post.image = post_args['image']
        post.category_id = post_args['category_id']
        db.session.add(post)
        db.session.commit()
        return post
        
    
    
    
    
    def delete(self,post_id):
        Post.delete_post(post_id)
        return "no content",204
        