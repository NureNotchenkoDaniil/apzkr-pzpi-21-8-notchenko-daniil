from tortoise import Model, fields


class Pet(Model):
    id = fields.IntField(pk=True, index=True)
    pet_name = fields.CharField(max_length=50, null=False)
    pet_type = fields.ForeignKeyField('models.PetType', related_name='pets')
    breed = fields.CharField(max_length=100, null=False)
    vaccinated = fields.BooleanField(default=False)
    owner = fields.ForeignKeyField('models.User', related_name='pets')

