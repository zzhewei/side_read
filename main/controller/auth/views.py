from . import AuthInit
from flask import request, abort, current_app
from flask_restx import Resource
from .serializers import SettingSchema
from .service import SettingService
import uuid

auth = AuthInit.auth
SettingSc = SettingSchema()


@auth.route('/Auth/Code')
class Auth(Resource):
    CodeSer = AuthInit.Code

    @auth.marshal_with(CodeSer)
    def get(self):
        """取得唯一碼
           ＊若沒有unicode，產生一組代碼給前端儲存之後都帶該代碼，否則都視為初次登入"""
        try:
            return {"Code": str(uuid.uuid3(uuid.NAMESPACE_DNS, 'u3'))}
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))


@auth.route('/Auth/Setting')
class Auth(Resource):
    RemainSer = AuthInit.Remain
    RemainPUTSer = AuthInit.RemainPUT
    RemainDELETESer = AuthInit.RemainDELETE

    @auth.marshal_with(RemainSer)
    def get(self):
        """取得提醒時間與篇數"""
        try:
            return SettingService.get()
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @auth.expect(RemainSer)
    @auth.marshal_with(RemainSer)
    def post(self):
        """新增提醒時間與篇數"""
        try:
            data = request.get_json()
            data_valid = SettingSc.load(data)
            instance = SettingService.post(data_valid)
            return SettingSc.dump(instance)
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @auth.expect(RemainPUTSer)
    def put(self):
        """更新提醒時間與篇數"""
        try:
            data = request.get_json()
            data_valid = SettingSc.load(data)
            SettingService.put(data_valid)
            return {"Status": "Update Success"}
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @auth.expect(RemainDELETESer)
    @auth.response(204, 'Remain deleted')
    def delete(self):
        """刪除提醒時間與篇數"""
        try:
            data = request.get_json()
            data_valid = SettingSc.load(data, partial=True)
            SettingService.delete(data_valid)
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))
