from flask_restx import Api
from flask import Blueprint
from .category.views import Category
from .auth.views import auth
from .read.views import Read


v1 = Blueprint('v1', __name__, url_prefix='/API')
api = Api(v1, version='1.0',
          title='SideRead API',
          description='Just API',)

api.add_namespace(Category)
api.add_namespace(Read)
api.add_namespace(auth)
