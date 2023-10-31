from flask import request,render_template,redirect,url_for,current_app
from app.categories import categories_blueprint
from werkzeug.utils import secure_filename
from app.models import Category,db




@categories_blueprint.route('', endpoint = 'index')
def categories_index():
    categories = Category.get_all_categories()
    return render_template('categories/index.html',categories=categories)



@categories_blueprint.route('/<int:id>', endpoint = 'show')
def categories_show(id):
    category = Category.get_specific_category(id)
    return render_template('categories/show.html',onecategory=category)



@categories_blueprint.route('/<int:id>/delete', endpoint = 'delete')
def categories_delete(id):
    Category.delete_category(id)
    return redirect(url_for('categories.index'))




@categories_blueprint.route('/create', endpoint = 'create', methods = ["GET","POST"])
def category_create():
    if request.method == 'POST':
        
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            image_path = f"app/uploads/{image.filename}"
            image.save(image_path) 
        else:
            filename = None
        category = Category(name=request.form['name'], desc=request.form['desc'], image=filename)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('categories.index'))
    return render_template('categories/create.html')







@categories_blueprint.route('/<int:id>/update', endpoint = 'update',methods = ["GET","POST"])
def update_category(id):
    category = Category.query.get_or_404(id)

    if request.method == 'POST':

        category.name = request.form['name']
        category.desc = request.form['desc']

        newimage = request.files['image']
        if newimage:
            filename = secure_filename(newimage.filename)
            image_path = f"app/uploads/{newimage.filename}"
            newimage.save(image_path)
            category.image = filename

        db.session.commit()
        return redirect(url_for('categories.show', id=category.id))

    return render_template('categories/update.html', category=category)