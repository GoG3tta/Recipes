from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.__init__ import DATABASE
from flask_app.models.users_model import User
from flask import flash



class Recipe: # CHANGE PROJECT TO FILE NAME
    def __init__( self , data ): 
        self.id = data['id']        # CHANGE SELF.__ TO MATCH SCHEMA
        self.recipe_name = data['recipe_name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
        

    @staticmethod
    def validate_recipe(data):
        is_valid=True

        if len(data['recipe_name']) < 3:
            flash("Dish name but be at least 3 character")
            is_valid = False

        if len(data['description']) < 3:
            flash("Dish name must be at least 3 character")
            is_valid = False

        if data['date_cooked'] == "":
            flash("Date cooked is required")
            is_valid = False

        if not 'under_30' in data:
                flash("Time cooked is required")
                is_valid = False


        return is_valid

    @classmethod
    def save(cls, form_data):
        query = """
        INSERT INTO recipe (recipe_name, description, instructions,date_cooked, under_30, user_id)
        VALUES (%(recipe_name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30)s, %(user_id)s);
        """
        recipe =connectToMySQL(DATABASE).query_db(query, form_data)
        return recipe

    @classmethod
    def edit_one(cls, form_data):
        query = """
        UPDATE recipe
        SET recipe_name = %(name)s,
        description = %(description)s,
        instructions = %(instruction)s, 
        date_cooked = %(date_cooked)s, 
        under_30 = %(0)s
    WHERE id = %(id)s
        """
        recipe =connectToMySQL(DATABASE).query_db(query, form_data)
        return True


#READ ONE
    @classmethod
    def get_one(cls, id):
        data = {'id': id}
        query = '''
            SELECT * FROM users WHERE id = %(id)s;
        '''
        result = connectToMySQL(DATABASE).query_db(query, data)
        return User(result[0])
    
    @classmethod 
    def get_all_with_user(cls):
        query ="""
             SELECT * FROM recipe
            LEFT JOIN users ON recipe.user_id = users.id
"""

        results = connectToMySQL(DATABASE).query_db(query)
        recipe = []
        for row in results:
            each_recipe = cls(row)
            user_dict = {
                "id" : row["users.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "email" : row["email"],
                "password" : row["password"],
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"],
            }
            user_from_row = User(user_dict)
            each_recipe.user = user_from_row
            recipe.append(each_recipe)

        return recipe

    @classmethod
    def get_one_with_owner(cls,id):
        id_dict = {"id" : id}

        query = """
            SELECT * FROM recipe
            LEFT JOIN users ON recipe.user_id = users.id
            WHERE recipe.id = %(id)s;    
        """
        results = connectToMySQL(DATABASE).query_db(query, id_dict)
        row = results[0]
        recipe = cls(row)

        recipe = cls(results[0])
        user_dict = {
                "id" : row["users.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "email" : row["email"],
                "password" : row["password"],
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"],
        }
        recipe.user = User(user_dict)
        return recipe


    #UPDATE
    @classmethod
    def update(cls, data):
        query = '''
            UPDATE users 
            SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
            WHERE id = %(id)s;
        '''
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results


    #DELETE
    @classmethod
    def delete_one_by_id(cls, id):
        data = {'id': id}
        query = """
        DELETE FROM recipe WHERE id = %(id)s;
    """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return True
    
    """
    [
   {
    "id": 1,
    "recipe_name": "deep dish",
    "description": "Chicago Style Pizza",
    "instructions": "cook for 20 mins",
    "date_cooked": "Sat, 20 Apr 2024 00:00:00 GMT",
    "under_30": 1,
    "user_id": 1,
    "created_at": "Tue, 23 Apr 2024 09:15:00 GMT",
    "updated_at": "Tue, 23 Apr 2024 09:15:00 GMT",


    "email": "co@you.com",
    "first_name": "cory",
    "last_name": "mack",
    "password": "$2b$12$GErAJmGB8Rh0O1rsoPi7NehJe.KlGmRIRYAVaBUpri1N8LVBsgtOi",
    "users.created_at": "Mon, 22 Apr 2024 18:12:15 GMT",
    "users.id": 1,
    "users.updated_at": "Mon, 22 Apr 2024 18:12:15 GMT"
  }
    ]
    """