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
            "ReadId": fields.Integer(readonly=True),
            "Time": fields.String,
            "ReadNum": fields.Integer,
            "ReadTime": fields.Integer,
            "Read": fields.Boolean,
        },
    )
