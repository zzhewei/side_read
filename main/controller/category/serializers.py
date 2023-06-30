from flask_marshmallow import Marshmallow
from marshmallow import validates_schema, fields
from main.model import Category


ma = Marshmallow()


class CategorySchema(ma.SQLAlchemyAutoSchema):
    UserNo = fields.String(load_only=True)
    CategoryIdList = fields.List(fields.Integer)

    class Meta:
        model = Category
        exclude = ['CreateTime', 'UpdateTime', 'CreateUser', 'UpdateUser']
        include_fk = True

    @validates_schema
    def validate(self, data, **kwargs):


        return data

    # @post_load  # 反序列並驗證後執行的
    # def post_load(self, data, **kwargs):
    #     try:
    #         period = data.pop("PeriodId")
    #         user = User(**data)
    #         db.session.add(user)
    #         db.session.flush()
    #         for i in period:
    #             up = UserPeriod(UserId=user.UserId,
    #                             PeriodId=i)
    #             db.session.add(up)
    #         db.session.commit()
    #         return user
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         raise Exception("DB Operation Error")
