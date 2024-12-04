import os
from snowflake.snowpark.session import Session
from snowflake.snowpark.version import VERSION

def get_session(
        account = None,
        user = None,
        password = None,
        warehouse = None,
        database = None,
        schema = None,
        role = None,
    ):

    # Create a connection to Snowflake
    connection_parameters = {
        "account": account if account else os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": user if user else os.getenv("SNOWFLAKE_USER"),
        "password": password if password else os.getenv("SNOWFLAKE_PASSWORD"),
        "warehouse": warehouse if warehouse else os.getenv("SNOWFLAKE_WAREHOUSE"),
        "database": database if database else "",
        "schema": schema if schema else "",
        "role": role if role else "",
    }

    # Create Snowflake Session object
    print("Connecting to Snowflake...")
    session = Session.builder.configs(connection_parameters).create()

    # Current Environment
    print("Current Environment...")
    snowflake_environment = session.sql('select current_user(), current_role(), current_database(), current_schema(), current_version(), current_warehouse()').collect()
    snowpark_version = VERSION
    print('   User                        : {}'.format(snowflake_environment[0][0]))
    print('   Role                        : {}'.format(snowflake_environment[0][1]))
    print('   Database                    : {}'.format(snowflake_environment[0][2]))
    print('   Schema                      : {}'.format(snowflake_environment[0][3]))
    print('   Warehouse                   : {}'.format(snowflake_environment[0][5]))
    print('   Snowflake version           : {}'.format(snowflake_environment[0][4]))
    print('   Snowpark for Python version : {}.{}.{}'.format(snowpark_version[0],snowpark_version[1],snowpark_version[2]))

    # Return Session
    return session