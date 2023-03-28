from flask import request
import re
from random import randint
from datetime import datetime, timedelta

from ..__request import request_to_db as rdb


def controll():
    phone = request.json.get("phone")

    rqst_users = f"select user_id from users where phone = {repr(phone)}"
    users = rdb(rqst_users)

    if not validate_phone(phone):
        return {"message":"Некорректный номер телефона"}, 400

    if not users:
        rdb(f"insert into users (phone) values ({repr(phone)})", 1) 

    user_id = rdb(rqst_users)[0][0]
    code = f"{randint(100,999)}-{randint(100,999)}"
    ended_at = (datetime.now() + timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
    rdb(f"insert into access_codes (user_id, code, ended_at) values ({repr(user_id)},{repr(code)},{repr(ended_at)})", 1)
    
    return "", 204
    

def validate_phone(phone:str):
    pattern = r'^\+\d{12}$'
    return re.match(pattern, phone)

