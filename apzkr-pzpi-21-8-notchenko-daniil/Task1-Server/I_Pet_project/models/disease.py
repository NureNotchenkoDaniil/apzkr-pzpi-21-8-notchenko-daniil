from tortoise import Model, fields
from datetime import date


class StoryOfDisease(Model):
    id = fields.IntField(pk=True, index=True)
    first_visit_date = fields.DateField(null=False)
    last_visit_date = fields.DateField(null=False)
    medications = fields.TextField(null=True)
    pet = fields.ForeignKeyField('models.Pet', related_name='disease_stories')

