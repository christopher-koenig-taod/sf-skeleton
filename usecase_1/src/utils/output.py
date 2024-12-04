from typing import Any

from snowflake.ml.registry import Registry
from snowflake.snowpark.session import Session

def log_model_to_registry(session: Session, database: str, schema: str, model: Any, model_name: str):
    
    reg = Registry(
        session=session, 
        database_name=database, 
        schema_name=schema
    )

    mv = reg.log_model(
        model,
        model_name=model_name,
        version_name="v1",
        # conda_dependencies=["scikit-learn"],
        # metrics={"MSE": mse, "MAPE": mape},
        # sample_input_data=df_train[['year', 'month', 'lag_nettokaltmiete_1', 'lag_nettokaltmiete_2']]
)