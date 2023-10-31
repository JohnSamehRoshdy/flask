from flask import request,render_template,redirect,url_for,current_app
from app.models import Post,Category,db
from werkzeug.utils import secure_filename
import os
from app.posts import post_blueprint


@post_blueprint.route('', endpoint = 'index')
def posts_index():
    posts = Post.get_all_posts()
    return render_template('posts/index.html',posts=posts)


@post_blueprint.route('/<int:id>', endpoint = 'show')
def posts_show(id):
    post = Post.get_specific_post(id)
    return render_template('posts/show.html',onepost=post)


@post_blueprint.route('/<int:id>/delete', endpoint = 'delete')
def posts_delete(id):
    Post.delete_post(id)
    return redirect(url_for('posts.index'))
    
 
    
# UPLOAD_FOLDER = 'static/posts/images'  
# current_app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
# filename = ""


@post_blueprint.route('/create', endpoint = 'create', methods = ["GET","POST"])
def post_create():
    categories = Category.get_all_categories()
    if request.method == 'POST':
        
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            image_path = f"app/uploads/{image.filename}"
            image.save(image_path) 
        else:
            filename = None
        post = Post(title=request.form['title'], body=request.form['body'], image=filename,category_id=request.form['category_id'])
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts.index'))
    return render_template('posts/create.html',categories = categories)



@post_blueprint.route('/<int:id>/update', endpoint = 'update',methods = ["GET","POST"])
def update_post(id):
    categories = Category.get_all_categories()
    post = Post.query.get_or_404(id)

    if request.method == 'POST':

        post.title = request.form['title']
        post.body = request.form['body']
        post.category_id = request.form['category_id']

        newimage = request.files['image']
        if newimage:
            filename = secure_filename(newimage.filename)
            image_path = f"app/uploads/{newimage.filename}"
            newimage.save(image_path)
            post.image = filename

        db.session.commit()
        return redirect(url_for('posts.show', id=post.id))

    return render_template('posts/update.html', post=post,categories = categories)