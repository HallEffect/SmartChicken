# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)
from app import views