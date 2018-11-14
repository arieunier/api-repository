from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os, logging, psycopg2
from datetime import datetime
import ujson
import uuid
from flask_bootstrap import Bootstrap
from libs import   utils , logs
from appsrc import app, logger
from flask import make_response

@app.route('/hello', methods=['GET'])
def contact():
    try:
        cookie, cookie_exists =  utils.getCookie()

        tmp_dict = {"Result" : "World"}
        data = ujson.dumps(tmp_dict)
        return utils.returnResponse(data, 200, cookie, cookie_exists)
    except Exception as e:
        import traceback
        traceback.print_exc()
        cookie, cookie_exists =  utils.getCookie()
        return utils.returnResponse("An error occured, check logDNA for more information", 403, cookie, cookie_exists)