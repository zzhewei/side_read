from flask import request, abort, current_app
from flask_restx import Resource, reqparse
from . import ReadInit
from .serializers import ReadSchema
from .service import ReadService

Read = ReadInit.read
parser = reqparse.RequestParser()
parser.add_argument("sort", type=str, required=True, action="split")
ReadSc = ReadSchema()


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
            return ReadService.get()
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @Read.expect(ReadPostSer)
    @Read.marshal_with(ReadPostSer, code=201)
    def post(self):
        """新增文章"""
        try:
            data = request.get_json()
            data_valid = ReadSc.load(data)
            instance = ReadService.post(data_valid)
            x = ReadSc.dump(instance)
            print('x', x)
            return x
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @Read.expect(ReadPutSer)
    # @Read.marshal_with(ReadPutSer)
    def put(self):
        """更新文章
           更改星級、更改分類用"""
        try:
            data = request.get_json()
            data_valid = ReadSc.load(data)
            print(data_valid)
            ReadService.put(data_valid)
            return {"Status": "Update Success"}
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @Read.expect(ReadDELETESer)
    @Read.response(204, 'Read deleted')
    def delete(self):
        """刪除文章"""
        try:
            data = request.get_json()
            data_valid = ReadSc.load(data)
            ReadService.delete(data_valid)
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))


@Read.route('/Read/<string:CategoryName>')
class ReadByCategoryOpe(Resource):
    ReadByCategorySer = ReadInit.ReadByCategoryGET

    @Read.expect(parser)
    # @Read.marshal_with(ReadByCategorySer)
    def get(self, CategoryName):
        """首頁下半部
            sort參數範例 sort=要排序欄位,升降序
            要排序欄位有star,time 剩下一個不知道是三小
            升降序有asc,desc"""
        try:
            result = {"Read": [], "Unread": []}
            args = parser.parse_args()
            read, unread = ReadService.getByCategory(CategoryName, args['sort'])
            for i in read:
                i.UpdateTime = i.UpdateTime.strftime("%Y-%B-%d")
            for i in unread:
                i.UpdateTime = i.UpdateTime.strftime("%Y-%B-%d")
            result["Read"] = ReadSchema(many=True).dump(read)
            result["Unread"] = ReadSchema(many=True).dump(unread)
            # print(result)
            return result
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))
