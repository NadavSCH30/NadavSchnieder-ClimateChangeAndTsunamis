"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from _5000__NadavSchnieder import app
import pandas as pd 

from _5000__NadavSchnieder.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines



from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json 
import requests

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError


from _5000__NadavSchnieder.Models.QueryFormStructure import QueryFormStructure 
from _5000__NadavSchnieder.Models.QueryFormStructure import LoginFormStructure 
from _5000__NadavSchnieder.Models.QueryFormStructure import UserRegistrationFormStructure 

db_Functions = create_LocalDatabaseServiceRoutines() 

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'Home.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='My contact page.'
    )

@app.route('/about')
def about():
    """Renders the contact page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='My about page.'
    )

@app.route('/DataModel')
def DataModel():
    """Renders the contact page."""
    return render_template(
        'DataModel.html',
        title='Data Model',
        year=datetime.now().year,
        message='This is how I will present my data.'
    )

@app.route('/Dataset1')
def Dataset1():
    """Renders the contact page."""
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\Data\GlobalTemperatures.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')
   

 
    return render_template(
        'DataSet1.html',
        title='This is Dataset 1 page',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='In this page we will display the datasets we are going to use in order to answer ARE THERE UFOs'
    )

@app.route('/Dataset2')
def Dataset2():
    """Renders the contact page."""
    df = pd.read_csv(path.join(path.dirname(__file__), 'static\Data\waves.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')
   

 
    return render_template(
        'DataSet2.html',
        title='This is Dataset 2 page',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='In this page we will display the datasets we are going to use in order to answer ARE THERE UFOs'
    )


    # -------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )




       #message='This page will show my datasets, how I will work with them and what do I plan to do with them.'
 



