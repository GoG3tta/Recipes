from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.users_model import User
from flask_app.models.recipes_model import Recipe


@app.route('/recipes')
def dashboard_page():
    if not "user_id" in session:
        return redirect('/')
    logged_user = User.get_one_by_id(session['user_id'])
    recipe_list = Recipe.get_all_with_user()
    return render_template('dashboard.html',logged_user = logged_user, recipe_list = recipe_list)
#READ ALL

@app.route('/recipes/new')
def create_recipes_page():
    if not "user_id" in session:
        return redirect('/')
    logged_user = User.get_one_by_id(session['user_id'])
    return render_template('add_recipe.html', logged_user = logged_user )

@app.route('/recipes/new/process', methods=['POST'])
def create_new_recipe():
    if not "user_id" in session:
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    form_data =  {
        **request.form,
        "user_id" : session["user_id"]
    }

    Recipe.save(request.form)
    return redirect('/recipes')



@app.route('/recipes/<int:id>')
def recipe_details(id):
        if not "user_id" in session:
            return redirect('/')
        logged_user = User.get_one_by_id(session['user_id'])
        recipe_with_owner = Recipe.get_one_with_owner(id)
        return render_template('details_recipe.html', logged_user = logged_user, recipe_with_owner = recipe_with_owner)

@app.route('/recipes/<int:id>/edit')
def recipe_edit_page(id):
        if not "user_id" in session:
            return redirect('/')
        logged_user = User.get_one_by_id(session['user_id'])

        recipe_with_owner = Recipe.get_one_with_owner(id)

        return render_template('recipe_edit_page.html', logged_user = logged_user, recipe = recipe_with_owner)

@app.route('/recipes/<int:id>/edit/process',methods = ['POST'])
def recipe_edit_process(id):
    form_with_id = {
        **request.form,
        'id' : id     
        }
    if not Recipe.validate_recipe(request.form):
        return redirect (f'/recipes/{id}/edit')
    Recipe.edit_one(form_with_id)
    return redirect('/recipes')


@app.route('/recipes/<int:id>/delete')
def item_delete_process(id):
    if not "user_id" in session:
            return redirect('/')
    logged_user = User.get_one_by_id(session['user_id'])

    Recipe.delete_one_by_id(id)
    return redirect('/recipes')
     





@app.route('/success')
def success():
    if "user_id" not in session:
        return redirect ('/logout')
    return render_template ('dashboard.html')




@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')
