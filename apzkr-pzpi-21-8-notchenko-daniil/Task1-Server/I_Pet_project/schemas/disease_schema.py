from pydantic import BaseModel
from datetime import date

from tortoise.contrib.pydantic import pydantic_model_creator

from models import StoryOfDisease


class StoryOfDiseaseIn(BaseModel):
    first_visit_date: date
    last_visit_date: date
    medications: str = None
    pet: int


story_of_disease_pydanticIn = StoryOfDiseaseIn


class StoryOfDiseaseUpdate(BaseModel):
    first_visit_date: date
    last_visit_date: date
    medications: str = None


story_of_disease_pydanticUpdate = StoryOfDiseaseUpdate
story_of_disease_pydantic = pydantic_model_creator(StoryOfDisease, name='StoryOfDisease')