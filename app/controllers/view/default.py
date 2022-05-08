from app import app
from flask import Flask, render_template, request, redirect, session, flash, url_for, jsonify
import requests
import simplejson as json
from dateutil.parser import parse
import bcrypt
import base64
import time
import sys
import datetime
from datetime import datetime, timedelta


@app.route('/', methods=['GET'])
def index():
    
    return render_template('index.html', titulo='Blog LAB AS Digital',title='Blog LAB AS Digital')