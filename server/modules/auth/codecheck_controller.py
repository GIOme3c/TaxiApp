from flask import request
from datetime import datetime

from ..__request import request_to_db as rdb


def controll():
    phone = request.json.get("phone")
    code = request.json.get("code")

    user_data = rdb(f"""
            select users.user_id, ended_at from users
            join access_codes on access_codes.user_id = users.user_id
            where phone = {repr(phone)} and code = {repr(code)}
            """)
    
    if not user_data :
        return {"message":"Некорректный код"}, 400

    user_id = user_data[0][0]
    code_deadline = user_data[0][1]

    if code_deadline < datetime.now():
        return {"message":"Код устарел"}, 400
    
    #!РАБОТА С ТОКЕНОМ
    rdb(f"delete from access_codes where user_id = {user_id}",1)
    return {},204



