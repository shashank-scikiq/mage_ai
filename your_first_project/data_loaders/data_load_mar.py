from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_postgres(*args, **kwargs):
    """
    Template for loading data from a PostgreSQL database.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#postgresql
    """

    query = """select concat(sm."Seller App" , concat('__',sm.provider_id)) as provider_key,  sm."Date" as order_date,
    sm.category as category, sm."Sub - Category" as sub_category, sm.pin_code
    from public.sku_master sm
    where extract (month from sm."Date") = '03' and extract (year from sm."Date") = '2024'"""  # Specify your SQL query here

    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'SRC'

    with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        return loader.load(query)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
