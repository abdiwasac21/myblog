from mongoengine import Document, fields
from datetime import datetime
from mongoengine import Document, StringField, EmailField
from django_mongoengine.mongo_auth.models import AbstractUser

# Create your models here.


class Post(Document):
    title = fields.StringField(max_length=100, required=True)
    content = fields.StringField(required=True)
    date_posted = fields.DateTimeField(default=datetime.now)
    author = fields.StringField(max_length=100, required=True)

    meta = {
        'collection': 'posts'  # MongoDB collection name
    }


class User(AbstractUser, Document):
    meta = {'collection': 'users'}  # MongoDB collection name
    email = EmailField(unique=True, required=True)
    username = StringField(max_length=150, unique=True, required=True)
    password = StringField(required=True)
