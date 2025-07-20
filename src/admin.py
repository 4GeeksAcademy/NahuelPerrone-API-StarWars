import os
from flask_admin import Admin
from models import db, User, Planeta, Personaje, Planetas_favoritos, Personajes_favoritos
from flask_admin.contrib.sqla import ModelView

# class Personajes_favoritosAdmin(ModelView):
#     column_list = ('id', 'name','user_id', 'personaje_id')
#     form_columns = ('name','user_id', 'personaje_id')

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Planeta, db.session))
    admin.add_view(ModelView(Personaje, db.session))
    admin.add_view(ModelView(Planetas_favoritos, db.session))
    admin.add_view(ModelView(Personajes_favoritos, db.session))

    # admin.add_view(Personajes_favoritosAdmin(Personajes_favoritos, db.session))
    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))