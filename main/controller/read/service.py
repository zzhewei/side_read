from flask import current_app
from main.model import db, Read, Category
from sqlalchemy import func


class ReadService:
    @staticmethod
    def get():
        try:
            r = [
                    {
                        "CategoryId": 0,
                        "CategoryName": "全部",
                        "Read": 0,
                        "Unread": 0
                    },
                    {
                        "CategoryId": 0,
                        "CategoryName": "未分類",
                        "Read": 0,
                        "Unread": 0
                    }
                ]
            read = Read.query.filter_by(Read=True).with_entities(Read.CategoryId, func.count(Read.CategoryId).label('total')).group_by(Read.CategoryId)
            unread = Read.query.filter_by(Read=False).with_entities(Read.CategoryId, func.count(Read.CategoryId).label('total')).group_by(Read.CategoryId)

            for i in read:
                # 算已閱讀的總數
                r[0]["Read"] += 1

                # CategoryId = 0的就是未分配
                if i[0] == 0:
                    r[1]["Read"] = i[1]
            read = read.subquery()

            for i in unread:
                r[0]["Unread"] += 1

                if i[0] == 0:
                    r[1]["Unread"] = i[1]
            unread = unread.subquery()

            result = Category.query.with_entities(Category.CategoryId, Category.CategoryName, func.coalesce(read.c.total, 0).label('Read'), func.coalesce(unread.c.total, 0).label('Unread'))\
                .join(read, Category.CategoryId == read.c.CategoryId, isouter=True)\
                .join(unread, Category.CategoryId == unread.c.CategoryId, isouter=True).all()

            return r + result
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")

    @staticmethod
    def getByCategory(CategoryName, args):
        try:
            if CategoryName == "全部":
                read = Read.query.filter_by(Read=True)
                unread = Read.query.filter_by(Read=False)
            elif CategoryName == "未分類":
                read = Read.query.filter_by(Read=True, CategoryId=0)
                unread = Read.query.filter_by(Read=False, CategoryId=0)
            else:
                s1 = Category.query.filter_by(CategoryName=CategoryName).all()
                if s1:
                    read = Read.query.filter_by(Read=True, CategoryId=s1[0].CategoryId)
                    unread = Read.query.filter_by(Read=False, CategoryId=s1[0].CategoryId)
                else:
                    raise Exception("CategoryName Error")

            if args[1] == "asc":
                if args[0] == "star":
                    read = read.order_by(Read.Star.asc()).all()
                    unread = unread.order_by(Read.Star.asc()).all()
                elif args[0] == "time":
                    read = read.order_by(Read.UpdateTime.asc()).all()
                    unread = unread.order_by(Read.UpdateTime.asc()).all()
                else:
                    pass
            else:
                if args[0] == "star":
                    read = read.order_by(Read.Star.desc()).all()
                    unread = unread.order_by(Read.Star.desc()).all()
                elif args[0] == "time":
                    read = read.order_by(Read.UpdateTime.desc()).all()
                    unread = unread.order_by(Read.UpdateTime.desc()).all()
                else:
                    pass

            return read, unread
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")

    @staticmethod
    def post(data):
        try:
            read = Read(URL=data["URL"],
                        Star=data["Star"],
                        CategoryId=data["CategoryId"],
                        UpdateUser=data["UserNo"],
                        CreateUser=data["UserNo"],)
            db.session.add(read)
            db.session.commit()
            return read
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")

    @staticmethod
    def put(data):
        try:
            for i in data["ReadIdList"]:
                temp = Read.query.filter_by(ReadId=i).first()
                if temp:
                    temp.CategoryId = data["CategoryId"]
                    temp.UpdateUser = data["UserNo"]
                    temp.Star = data["Star"]
                    temp.Read = data["Read"]
            db.session.commit()
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")

    @staticmethod
    def delete(data):
        try:
            for i in data["ReadIdList"]:
                Read.query.filter_by(ReadId=i).delete()
            db.session.commit()
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")
