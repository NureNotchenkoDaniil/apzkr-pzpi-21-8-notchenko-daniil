from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from models import Pet


class PetIn(BaseModel):
    pet_name: str
    pet_type: int
    breed: str
    vaccinated: bool


pet_pydanticIn = PetIn


class PetVaccinationUpdate(BaseModel):
    vaccinated: bool

pet_vaccination_update_pydantic = PetVaccinationUpdate
pet_pydantic = pydantic_model_creator(Pet, name='Pet')

