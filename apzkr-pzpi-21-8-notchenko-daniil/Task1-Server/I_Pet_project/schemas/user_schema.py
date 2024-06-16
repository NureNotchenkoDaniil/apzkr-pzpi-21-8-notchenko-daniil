# schemas/user_schema.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from tortoise.contrib.pydantic import pydantic_model_creator

from models import User


class UpdateUserVerification(BaseModel):
    is_verified: bool

user_pydantic = pydantic_model_creator(User, name='User')
user_pydanticIn = pydantic_model_creator(User, name='UserIn', exclude_readonly=True, exclude=('is_verified', 'join_date'))
user_pydanticOut = pydantic_model_creator(User, name='UserOut', exclude=('password', ))

