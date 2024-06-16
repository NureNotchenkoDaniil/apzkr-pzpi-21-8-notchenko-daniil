from tortoise import Model, fields


class Role(Model):
    id = fields.IntField(pk=True, index=True)
    user = fields.ForeignKeyField('models.User', related_name='roles')
    is_admin = fields.BooleanField(default=False)
    is_veterinarian = fields.BooleanField(default=False)
    is_government = fields.BooleanField(default=False)

