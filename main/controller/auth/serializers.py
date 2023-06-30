from flask_marshmallow import Marshmallow
from marshmallow import validates_schema, fields
from main.model import Remain


ma = Marshmallow()


class SettingSchema(ma.SQLAlchemyAutoSchema):
    UserNo = fields.String(load_only=True)
    RemainIdList = fields.List(fields.Integer)

    class Meta:
        model = Remain
        exclude = ['CreateTime', 'UpdateTime', 'CreateUser', 'UpdateUser']
        include_fk = True

    @validates_schema
    def validate(self, data, **kwargs):

        return data
