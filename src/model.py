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
    id = CharField(primary_key=True, unique=True)
    name = CharField()


# class Town(BaseModel):
#     id = IntegerField(primary_key=True)
#     dept = ForeignKeyField(Department)
#     name = CharField()


class Location(BaseModel):
    id = AutoField(primary_key=True)
    dept = ForeignKeyField(Department, column_name="dept")
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
    id = AutoField(primary_key=True)
    place = IntegerField()
    sex = IntegerField()
    birth_year = IntegerField()
    gravity = ForeignKeyField(Gravity, column_name="gravity")
    user_category = ForeignKeyField(UserCategory, column_name="user_category")


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
    id = AutoField(primary_key=True)
    surface = ForeignKeyField(Surface, column_name="surface")
    atm = ForeignKeyField(AtmosphericCondition, column_name="atm")


class Accident(BaseModel):
    num_acc = IntegerField(primary_key=True)
    weather_cond = ForeignKeyField(WeatherCondition, column_name="weather_cond")
    user_type = ForeignKeyField(UserType, column_name="user_type")
    lum = ForeignKeyField(LumCondition, column_name="lum")
    veh_type = ForeignKeyField(VehicleType, column_name="veh_type")
    location = ForeignKeyField(Location, column_name="location")
    year = IntegerField()
    # user_number = IntegerField()
