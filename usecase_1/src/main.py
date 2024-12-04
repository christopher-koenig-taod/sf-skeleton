from src.utils.connect import get_session

# Create a session
session = get_session()

# Load data from Snowflake
snowpark_df = session.table("")

# Transform to pandas DataFrame
df = snowpark_df.to_pandas("")