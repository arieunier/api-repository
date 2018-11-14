import datetime
import uuid
from flask import request
import os

FOLLOWANALYTICS_API_KEY = os.getenv("FOLLOWANALYTICS_APPLICATION_KEY", None)
FOLLOWANALYTICS_API_TOKEN = os.getenv("FOLLOWANALYTICS_API_TOKEN", None)
FOLLOWANALYTICS_SOR_IDENTIFIER = os.getenv("FOLLOWANALYTICS_SOR_IDENTIFIER", None)
APPNAME = os.getenv("APPNAME", "api-repository")

def getCookie():
    import flask
    cookie_exists = True
    cookie_value = flask.request.cookies.get(APPNAME)
    if (cookie_value == None):
        cookie_value = uuid.uuid4().__str__()
        cookie_exists = False

    return cookie_value, cookie_exists
    
def returnResponse(data, code, cookie_value, cookie_exists):
    from flask import make_response
    resp = make_response(data, code )
    if (cookie_exists == False):
        resp.set_cookie(APPNAME, cookie_value)
    return resp