from flask_restx import Namespace, fields


class ReadInit:
    read = Namespace("Read", path='/', description="文章清單")

    Read = read.model(
        "Read",
        {
            "ReadId": fields.Integer,
            "Title": fields.String,
            "Describe": fields.String,
            "Star": fields.Integer,
            "Read": fields.Boolean,
            "URL": fields.Url,
            "UpdateTime": fields.String,
        },
    )

    ReadGET = read.model(
        "ReadGET",
        {
            "CategoryId":  fields.Integer,
            "CategoryName":  fields.String,
            "Read":  fields.Integer,
            "Unread":  fields.Integer,
        },
    )

    ReadByCategoryGET = read.model(
        "ReadByCategoryGET",
        {
            "Read": fields.List(fields.Nested(Read)),
            "Unread": fields.List(fields.Nested(Read)),
        },
    )

    ReadPOST = read.model(
        "ReadPOST",
        {
            "ReadId": fields.Integer(readonly=True),
            "CategoryId":  fields.Integer,
            "URL":  fields.Url,
            "UserNo":  fields.String,
            "Star":  fields.Integer,
        },
    )

    ReadPUT = read.model(
        "ReadPUT",
        {
            "ReadIdList": fields.List(fields.Integer()),
            "CategoryId":  fields.Integer,
            "UserNo":  fields.String,
            "Star":  fields.Integer,
            "Study":  fields.Boolean,
        },
    )

    ReadDELETE = read.model(
        "ReadDELETE",
        {
            "ReadIdList": fields.List(fields.Integer()),
        },
    )
