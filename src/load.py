from sqlalchemy import create_engine

from src.environment import DATABASE_USER, DATABASE_HOST, DATABASE_NAME, DATABASE_PASSWORD


def load(vehicles, users, places, characteristics):
    print("Transform ALL")

    location = characteristics.drop(columns=['year', 'lum', 'atm'])
    weathercondition = characteristics.drop(columns=['year', 'lum', 'lat', 'long', 'dept']) \
        .join(places.set_index('num_acc'), on='num_acc')
    accident = characteristics.drop(columns=['atm', 'lat', 'long', 'dept'])
    accident_vehtype = vehicles
    usertype = users

    print("accident")
    load_to_postgresql(accident, "accident")

    print("location")
    load_to_postgresql(location, "location")

    print("weathercondition")
    load_to_postgresql(weathercondition, "weathercondition")

    print("accident_vehtype")
    load_to_postgresql(accident_vehtype, "accident_vehtype")

    print("usertype")
    load_to_postgresql(usertype, "usertype")


def load_to_postgresql(data, table):
    alchemyEngine = create_engine(
        f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}",
        pool_recycle=3600)

    postgreSQLConnection = alchemyEngine.connect()

    try:
        frame = data.to_sql(table, postgreSQLConnection, if_exists='append', index=False)
    except ValueError as vx:
        print(vx)
    except Exception as ex:
        print(ex)
    else:
        print("PostgreSQL Table %s has been created successfully." % table)
    finally:
        postgreSQLConnection.close()
