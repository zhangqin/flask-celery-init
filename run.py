#!/usr/bin/env python
# coding=utf-8
# author: b0lu
# mail: b0lu_xyz@163.com
from flask import Flask, Blueprint, render_template, make_response, Response
from m1.blueblue import blue

app = Flask(__name__, template_folder="tpl")
app.register_blueprint(blue, template_folder="template")

@app.route("/")
def index():
    return render_template("1.html")

@app.route("/cookie")
def cookie():
    #resp = make_response(render_template("1.html"))
    resp = Response(render_template("1.html"))
    resp.set_cookie("test", "xxxxxxxxxx")
    return resp

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
