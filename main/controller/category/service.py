from flask import current_app
from main.model import db, Category


class CategoryService:
    @staticmethod
    def get():
        try:
            result = Category.query.all()

            return result
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")

    @staticmethod
    def post(data):
        try:
            category = Category(CategoryName=data["CategoryName"],
                                UpdateUser=data["UserNo"],
                                CreateUser=data["UserNo"], )
            db.session.add(category)
            db.session.commit()
            return category
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")

    @staticmethod
    def put(data):
        try:
            temp = Category.query.filter_by(CategoryId=data["CategoryId"]).first()
            if temp:
                temp.CategoryName = data["CategoryName"]
                temp.UpdateUser = data["UserNo"]
                db.session.commit()
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")

    @staticmethod
    def delete(data):
        try:
            for i in data["CategoryIdList"]:
                Category.query.filter_by(CategoryId=i).delete()
            db.session.commit()
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")
