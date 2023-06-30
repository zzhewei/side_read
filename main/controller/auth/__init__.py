from flask_restx import Namespace, fields


class AuthInit:
    auth = Namespace("Auth", path='/', description="Auth")

    Code = auth.model(
        "Code",
        {
            "Code": fields.String,
        },
    )

    Remain = auth.model(
        "Remain",
        {
            "RemainId": fields.Integer(readonly=True),
            "RemainTime": fields.String,
            "ReadNum": fields.Integer,
            "ReadTime": fields.Integer,
            "UserNo": fields.String,
        },
    )

    RemainPUT = auth.model(
        "RemainPUT",
        {
            "RemainId": fields.Integer(),
            "RemainTime": fields.String,
            "ReadNum": fields.Integer,
            "ReadTime": fields.Integer,
            "UserNo": fields.String,
        },
    )

    RemainDELETE = auth.model(
        "RemainDELETE",
        {
            "RemainIdList": fields.List(fields.Integer)
        },
    )
