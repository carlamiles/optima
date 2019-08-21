from __future__ import unicode_literals
from django.db import models

import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name_min"] = "First name should be at least 2 characters"
        if postData['first_name'].isalpha() == False:
            errors["first_name_alpha"] = "First name must be letters only"
        if len(postData['last_name']) < 2:
            errors["last_name_min"] = "Last name should be at least 2 characters"
        if postData['last_name'].isalpha() == False:
            errors["last_name_alpha"] = "Last name must be letters only"
        if len(postData['password_reg']) < 8:
            errors["password_reg_min"] = "Password should be at least 8 characters"
        if postData['password_reg'] != postData['confirm_password_reg']:
            errors["password_reg_match"] = "Password and Confirm PW must match"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_reg_invalid'] = "Please enter a valid email address"
        return errors
    def login_validator(self, postData):
        errors = {}
        if len(postData['email_log']) == 0:
            errors['email_log_empty'] = 'Please enter your email'
            print('*'*25, 'email empty')
        if len(postData['password_log']) == 0:
            errors['password_log_empty'] = 'Please enter your password'
            print('*'*25, 'password empty')
        if not EMAIL_REGEX.match(postData['email_log']):
            errors['email_log_invalid'] = "Please enter a valid email address"
            print('*'*25, 'email invalid')
        return errors
    def update_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name_min"] = "First name should be at least 2 characters"
        if postData['first_name'].isalpha() == False:
            errors["first_name_alpha"] = "First name must be letters only"
        if len(postData['last_name']) < 2:
            errors["last_name_min"] = "Last name should be at least 2 characters"
        if postData['last_name'].isalpha() == False:
            errors["last_name_alpha"] = "Last name must be letters only"
        if len(postData['password_reg']) < 8:
            errors["password_reg_min"] = "Password should be at least 8 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_reg_invalid'] = "Please enter a valid email address"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    password = models.CharField(max_length=55)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<User object: {self.first_name} {self.last_name} ({self.id}) {self.email_address} {self.password} {self.created_at} {self.updated_at}>"