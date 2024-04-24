from flask import Flask

DATABASE = 'recipe_schema' # CHANGE PROJECT_SCHEMA TO SQL SCHEMA

app = Flask(__name__)
app.secret_key = 'its go time'