from . import AuthInit
from main.model import User
from main.config import BaseConfig
from flask import request, abort, current_app, jsonify
from flask_restx import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, decode_token, get_jwt
import time

auth = AuthInit.auth


@auth.route('/Auth/Code')
class Auth(Resource):
    CodeSer = AuthInit.Code

    @auth.marshal_with(CodeSer)
    def get(self):
        """取得唯一碼
           ＊若沒有unicode，產生一組代碼給前端儲存之後都帶該代碼，否則都視為初次登入"""
        try:
            pass
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))


@auth.route('/Auth/Setting')
class Auth(Resource):
    RemainSer = AuthInit.Remain

    @auth.marshal_with(RemainSer)
    def get(self):
        """取得提醒時間與篇數"""
        try:
            pass
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @auth.marshal_with(RemainSer)
    def post(self):
        """新增提醒時間與篇數"""
        try:
            pass
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))
