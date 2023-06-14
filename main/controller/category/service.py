from flask import current_app
from main.model import User, db, pc


class UserService:
    @staticmethod
    def get(data):
        try:
            # 單一搜尋
            if "UserId" in data and data["UserId"]:
                result = User.query.filter_by(UserId=data["UserId"]).first()
            # 模糊搜尋 is bullshit
            else:
                # SelectField有值 Select跟Role有沒有值都沒差
                if data["SelectField"]:
                    return_data = db.session.execute('''select fuzzy."UserId", fuzzy."RoleId", "UserName", "UserNo", "Account", "PasswordHash", "Email", "Phone", "Image", "UserName", "AreaId", "UnitId", string_agg(up."PeriodId"::varchar, ',') as "PeriodId" from\
                                                        (select u.*\
                                                         from (SELECT * FROM test."User" where "'''+data["SelectField"]+'''" like concat('%', :Select, '%')) as u\
                                                         left join test."Role" as r on u."RoleId" = r."RoleId" where r."RoleName" like concat('%', :Role)) as fuzzy\
                                                        left join test."UserPeriod" as up on fuzzy."UserId" = up."UserId"\
                                                        group by fuzzy."UserId", fuzzy."RoleId", "UserName", "UserNo", "Account", "PasswordHash", "Email", "Phone", "Image", "UserName", "AreaId", "UnitId";''',
                                                     {"Select": data['Select'], "Role": data['Role']})
                # SelectField沒值 Select有值直接把全部都模糊搜尋 Role有沒有值都沒差
                elif data["Select"]:
                    return_data = db.session.execute('''select fuzzy."UserId", fuzzy."RoleId", "UserName", "UserNo", "Account", "PasswordHash", "Email", "Phone", "Image", "UserName", "AreaId", "UnitId", string_agg(up."PeriodId"::varchar, ',') as "PeriodId" from\
                                                        (select u.*\
                                                         from (SELECT * FROM test."User" where "Account" like concat('%', :Select, '%') or "UserNo" like concat('%', :Select, '%') or "UserName" like concat('%', :Select, '%')) as u\
                                                         left join test."Role" as r on u."RoleId" = r."RoleId" where r."RoleName" like concat('%', :Role)) as fuzzy\
                                                        left join test."UserPeriod" as up on fuzzy."UserId" = up."UserId"\
                                                        group by fuzzy."UserId", fuzzy."RoleId", "UserName", "UserNo", "Account", "PasswordHash", "Email", "Phone", "Image", "UserName", "AreaId", "UnitId";''',
                                                     {"Select": data['Select'], "Role": data['Role']})
                else:
                    return_data = db.session.execute('''select fuzzy."UserId", fuzzy."RoleId", "UserName", "UserNo", "Account", "PasswordHash", "Email", "Phone", "Image", "UserName", "AreaId", "UnitId", string_agg(up."PeriodId"::varchar, ',') as "PeriodId" from\
                                                        (select u.*\
                                                         from (SELECT * FROM test."User") as u\
                                                         left join test."Role" as r on u."RoleId" = r."RoleId" where r."RoleName" like concat('%', :Role)) as fuzzy\
                                                        left join test."UserPeriod" as up on fuzzy."UserId" = up."UserId"\
                                                        group by fuzzy."UserId", fuzzy."RoleId", "UserName", "UserNo", "Account", "PasswordHash", "Email", "Phone", "Image", "UserName", "AreaId", "UnitId";''',
                                                     {"Select": data['Select'], "Role": data['Role']})

                user = return_data.mappings().all()
                result = []
                for i, v in enumerate(user):
                    result.append(dict(v))
                    result[i]["PeriodId"] = list(map(int, v["PeriodId"].split(","))) if v["PeriodId"] else []
                    result[i]["Password"] = pc.decrypt(v["PasswordHash"])

            return result
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")

    @staticmethod
    def post(data):
        try:
            pass
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")

    @staticmethod
    def put(data):
        try:
            pass
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")

    @staticmethod
    def delete(data):
        try:
            pass
        except Exception as e:
            current_app.logger.error(e)
            raise Exception("DB Operation Error")
