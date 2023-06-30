from flask_restx import Namespace, fields


class CategoryInit:
    category = Namespace("Category", path='/', description="類別")

    CategoryPOST = category.model(
        "CategoryPOST",
        {
            "CategoryId": fields.Integer(readonly=True),
            "CategoryName":  fields.String,
            "UserNo":  fields.String,
        },
    )

    CategoryPUT = category.model(
        "CategoryPUT",
        {
            "CategoryId": fields.Integer(),
            "CategoryName":  fields.String,
            "UserNo":  fields.String,
        },
    )

    CategoryDELETE = category.model(
        "CategoryDELETE",
        {
            "CategoryIdList":  fields.List(fields.Integer),
        },
    )