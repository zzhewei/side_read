from flask import request, abort, current_app
from flask_restx import Resource, reqparse
from flask_jwt_extended import jwt_required
from . import ReadInit
# from .serializers import UserSchema
from .service import UserService

Read = ReadInit.read
parser = reqparse.RequestParser()
parser.add_argument("sort", type=str, required=True, action="split")
# UserSc = UserSchema()


@Read.route('/Read')
class ReadOpe(Resource):
    ReadGetSer = ReadInit.ReadGET
    ReadPostSer = ReadInit.ReadPOST
    ReadPutSer = ReadInit.ReadPUT
    ReadDELETESer = ReadInit.ReadDELETE

    @Read.marshal_list_with(ReadGetSer)
    def get(self):
        """首頁上半部(全部、未分類...)"""
        try:
            pass
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @Read.expect(ReadPostSer)
    @Read.marshal_with(ReadPostSer, code=201)
    def post(self):
        """新增文章"""
        try:
            data = request.get_json()
            # data_valid = UserSsc.load(data)
            # instance = UserService.post(data_valid)
            # return UserSc.dump(instance)
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @Read.expect(ReadPutSer)
    @Read.marshal_with(ReadPutSer)
    def put(self):
        """更新文章
           更改星級、更改分類用"""
        try:
            data = request.get_json()
            # data_valid = UserSc.load(data)
            # instance = UserService.post(data_valid)
            # return UserSc.dump(instance)
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @Read.expect(ReadDELETESer)
    @Read.response(204, 'Read deleted')
    def delete(self):
        """刪除文章"""
        try:
            data = request.get_json()
            # data_valid = UserSc.load(data)
            # instance = UserService.post(data_valid)
            # return UserSc.dump(instance)
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))


@Read.route('/Read/<int:CategoryId>')
class ReadByCategoryOpe(Resource):
    ReadByCategorySer = ReadInit.ReadByCategoryGET

    @Read.marshal_with(ReadByCategorySer)
    @Read.expect(parser)
    def get(self, CategoryId):
        """首頁下半部"""
        try:
            args = parser.parse_args()
            print(args['sort'])
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))
