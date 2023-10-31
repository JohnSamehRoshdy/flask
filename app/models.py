from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from datetime import datetime



db = SQLAlchemy()


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)
    desc = db.Column(db.String)
    image = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    posts = db.relationship('Post',backref='category') 
    
    @classmethod
    def get_all_categories(cls):
        return cls.query.all() 
    
    @classmethod
    def get_specific_category(cls,id):
        return cls.query.get_or_404(id)
    
    @classmethod
    def delete_category(cls,id):
        post = cls.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()
        return True
    
    # @property
    # def delete_url(self):
    #     return url_for('categories.delete',id=self.id)
    
    @property
    def show_url(self):
        return url_for('categories.show',id=self.id)
    
    
    
    

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    image = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'),nullable = True)
    
    @classmethod
    def get_all_posts(cls):
        return cls.query.all() 
    
    @classmethod
    def get_specific_post(cls,id):
        return cls.query.get_or_404(id)
    
    @classmethod
    def delete_post(cls,id):
        post = cls.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()
        return True
    
    @property
    def delete_url(self):
        return url_for('posts.delete',id=self.id)
    
    @classmethod
    def save_post(cls,requestdata):
        post = cls(**requestdata)
        db.session.add(post)
        db.session.commit()
        return post