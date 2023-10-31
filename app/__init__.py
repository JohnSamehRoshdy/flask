from flask import Flask
from flask import render_template
from app.config import app_config as AppConfig
from app.models import db 
from app.posts import post_blueprint
from app.categories import categories_blueprint
from flask_migrate import Migrate
from flask_restful import Api,Resource
from app.posts.api.api_views import PostListClass,PostResource



def create_app(config_mod="dev"):
    app = Flask(__name__)
    CurrentConfigClass = AppConfig[config_mod]
    app.config["SQLALCHEMY_DATABASE_URI"] = CurrentConfigClass.SQLALCHEMY_DATABASE_URI
    app.config.from_object(CurrentConfigClass)
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)
    
    api.add_resource(PostListClass,'/api/posts/')
    api.add_resource(PostResource,'/api/posts/<int:post_id>')

    UPLOAD_FOLDER = 'static/posts/images'  
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
       
    
    


    
    @app.errorhandler(404)
    def not_found(error):
        return render_template('notfound.html')
    
    
    app.register_blueprint(post_blueprint)
    app.register_blueprint(categories_blueprint)
    
    
    return app