from peewee import CharField, IntegerField, Model


class DogFact(Model):
    id = IntegerField(primary_key=True)
    fact = CharField(max_length=255)
