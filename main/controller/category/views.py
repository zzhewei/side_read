from flask import request, abort, current_app
from flask_restx import Resource
from . import CategoryInit
from .serializers import CategorySchema
from .service import CategoryService

Category = CategoryInit.category
CgSc = CategorySchema()


@Category.route('/Category')
class CategoryOpe(Resource):

    CategoryPostSer = CategoryInit.CategoryPOST
    CategoryPutSer = CategoryInit.CategoryPUT
    CategoryDeleteSer = CategoryInit.CategoryDELETE

    def get(self):
        """搜尋文章分類"""
        try:
            instance = CategoryService.get()
            return CategorySchema(many=True).dump(instance)
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @Category.expect(CategoryPostSer)
    @Category.marshal_with(CategoryPostSer, code=201)
    def post(self):
        """新增文章分類"""
        try:
            data = request.get_json()
            data_valid = CgSc.load(data)
            instance = CategoryService.post(data_valid)
            return CgSc.dump(instance)
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @Category.expect(CategoryPutSer)
    def put(self):
        """更新文章分類"""
        try:
            data = request.get_json()
            data_valid = CgSc.load(data)
            CategoryService.put(data_valid)
            return {"Status": "Update Success"}
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @Category.expect(CategoryDeleteSer)
    @Category.response(204, 'Category deleted')
    def delete(self):
        """刪除文章分類"""
        try:
            data = request.get_json()
            data_valid = CgSc.load(data)
            CategoryService.delete(data_valid)
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))
