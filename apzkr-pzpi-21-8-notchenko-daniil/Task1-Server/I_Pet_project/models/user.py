from tortoise import Model, fields
from datetime import datetime


class User(Model):
    id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=50, null=False, unique=True)
    email = fields.CharField(max_length=100, null=False, unique=True)
    password = fields.CharField(max_length=100, null=False)
    is_verified = fields.BooleanField(default=False)
    joined_date = fields.DatetimeField(default=datetime.now())

