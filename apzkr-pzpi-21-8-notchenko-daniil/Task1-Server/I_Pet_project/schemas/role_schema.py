from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from models import Role


class RoleIn(BaseModel):
    user: int
    is_admin: bool
    is_veterinarian: bool
    is_government: bool

role_pydantic = pydantic_model_creator(Role, name='Role')
role_pydanticIn = pydantic_model_creator(Role, name='RoleIn', exclude_readonly=True)
