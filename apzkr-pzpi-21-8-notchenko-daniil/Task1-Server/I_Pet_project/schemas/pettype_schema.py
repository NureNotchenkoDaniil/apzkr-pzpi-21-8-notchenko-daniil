from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from models import PetType


class PetTypeIn(BaseModel):
    type_name: str

pet_type_pydantic = pydantic_model_creator(PetType, name='PetType')
pet_type_pydanticIn = pydantic_model_creator(PetType, name='PetTypeIn', exclude_readonly=True)
