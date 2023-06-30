from flask import current_app
from main.model import db, Remain


class SettingService:
    @staticmethod
    def get():
        try:
            result = Remain.query.all()

            return result
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")

    @staticmethod
    def post(data):
        try:
            remain = Remain(ReadNum=data["ReadNum"],
                            ReadTime=data["ReadTime"],
                            RemainTime=data["RemainTime"],
                            UpdateUser=data["UserNo"],
                            CreateUser=data["UserNo"], )
            db.session.add(remain)
            db.session.commit()
            return remain
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")

    @staticmethod
    def put(data):
        try:
            s1 = Remain.query.filter_by(RemainId=data["RemainId"]).first()
            if s1:
                s1.ReadNum = data["ReadNum"]
                s1.ReadTime = data["ReadTime"]
                s1.RemainTime = data["RemainTime"]
                s1.UpdateUser = data["UserNo"]
                db.session.commit()
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")

    @staticmethod
    def delete(data):
        try:
            for i in data["RemainIdList"]:
                Remain.query.filter_by(RemainId=i).delete()
            db.session.commit()
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")
