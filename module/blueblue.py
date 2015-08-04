#!/usr/bin/env python
# coding=utf-8
# author: b0lu
# mail: b0lu_xyz@163.com
from flask import Blueprint, render_template, abort, session
from jinja2 import TemplateNotFound

blue = Blueprint("blue", __name__, template_folder="template", url_prefix="/blue")
#blue = Blueprint("blue", __name__, url_prefix="/blue")

@blue.route("/hello")
def blue_index():
    try:
        return render_template("1.html")
    except TemplateNotFound:
        abort(404)

@blue.route("/", defaults= {'page': '1'})
@blue.route("/<page>")
def blue_page(page):
    try:
        return render_template("%s.html"%page)
    except TemplateNotFound:
        abort(404)
