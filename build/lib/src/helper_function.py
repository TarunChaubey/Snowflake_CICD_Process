from snowflake.snowpark.session import Session

connection_parameters = {
      "account": "fd05331.central-india.azure",
      "user": "tarunchaubey55",
      "password": "Bhargav09@",
     "role" :'ACCOUNTADMIN',
     "warehouse":'TEST_WAREHOUSES',
     "database":'CLASSIFICATION_DATASETES',
      "schema": "PUBLIC"
   }

def create_session_object():
    session = Session.builder.configs(connection_parameters).create()
    print(session.sql('select current_warehouse(), current_database(), current_schema()').collect())
    return session