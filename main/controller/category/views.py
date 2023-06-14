from flask import request, abort, current_app
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from . import CategoryInit
# from .serializers import UserSchema
from .service import UserService

Category = CategoryInit.category
# UserSc = UserSchema()


@Category.route('/Category')
class CategoryOpe(Resource):

    CategoryPostSer = CategoryInit.CategoryPOST
    CategoryPutSer = CategoryInit.CategoryPUT
    CategoryDeleteSer = CategoryInit.CategoryDELETE

    def get(self):
        """搜尋文章分類"""
        try:
            pass
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @Category.expect(CategoryPostSer)
    @Category.marshal_with(CategoryPostSer, code=201)
    def post(self):
        """新增文章分類"""
        try:
            data = request.get_json()
            # data_valid = UserSc.load(data)
            # instance = UserService.post(data_valid)
            # return UserSc.dump(instance)
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @Category.expect(CategoryPutSer)
    @Category.marshal_with(CategoryPutSer)
    def put(self):
        """更新文章分類"""
        try:
            data = request.get_json()
            # data_valid = UserSc.load(data)
            # instance = UserService.post(data_valid)
            # return UserSc.dump(instance)
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @Category.expect(CategoryDeleteSer)
    @Category.response(204, 'Category deleted')
    def delete(self):
        """刪除文章分類"""
        try:
            data = request.get_json()
            # data_valid = UserSc.load(data)
            # instance = UserService.post(data_valid)
            # return UserSc.dump(instance)
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))
