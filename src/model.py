from peewee import *

from src.environment import *

psql_db = PostgresqlDatabase(DATABASE_NAME,
                             user=DATABASE_USER,
                             password=DATABASE_PASSWORD,
                             host=DATABASE_HOST)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = psql_db


class Department(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()


class Town(BaseModel):
    id = IntegerField(primary_key=True)
    dept = ForeignKeyField(Department)
    name = CharField()


class Location(BaseModel):
    id = IntegerField(primary_key=True)
    town = ForeignKeyField(Town)
    adr = CharField()
    long = IntegerField()
    lat = IntegerField()


class VehicleType(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()


class UserCategory(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()


class Gravity(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()


class UserType(BaseModel):
    id = IntegerField(primary_key=True)
    place = IntegerField()
    sex = IntegerField()
    birth_year = IntegerField()
    gravity = ForeignKeyField(Gravity)
    user_category = ForeignKeyField(UserCategory)


class LumCondition(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()


class Surface(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()


class AtmosphericCondition(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()


class WeatherCondition(BaseModel):
    id = IntegerField(primary_key=True)
    surface = ForeignKeyField(Surface)
    atm = ForeignKeyField(AtmosphericCondition)


class Accident(BaseModel):
    id = IntegerField(primary_key=True)
    weather_condition = ForeignKeyField(WeatherCondition)
    user_type = ForeignKeyField(UserType)
    lum = ForeignKeyField(LumCondition)
    veh_type = ForeignKeyField(VehicleType)
    year = IntegerField()
    user_number = IntegerField()
