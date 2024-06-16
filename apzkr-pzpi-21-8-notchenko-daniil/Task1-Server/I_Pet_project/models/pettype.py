from tortoise import Model, fields


class PetType(Model):
    id = fields.IntField(pk=True, index=True)
    type_name = fields.CharField(max_length=50, null=False, unique=True)

