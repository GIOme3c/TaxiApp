from flask import Flask, request
from flask_cors import cross_origin

from .login_controller import controll as login_c
from .codecheck_controller import controll as check_code_c

def init(app:Flask):
    
    @cross_origin
    @app.route("/login", methods=["POST"])
    def login():
        return login_c()


    @cross_origin
    @app.route("/login/code", methods=["POST"])
    def check_code():
        return check_code_c()
