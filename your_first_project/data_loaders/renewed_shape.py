from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd


# @data_loader
# def get_month_range():
    
#     query = """
#     select x.src_mnth, x.src_year from (
#     select distinct extract(month from sm."Date") as src_mnth, 
#     extract(year from sm."Date") as src_year
#     from public.sku_master sm 
#     where "Date" > '2023-10-31') as x
#     order by x.src_year, x.src_mnth;
#     """
#     config_path = path.join(get_repo_path(), 'io_config.yaml')
#     config_profile = 'SRC'

#     with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
#         return loader.load(query)


# def execute_for_month():
#     dt_range = pd.DataFrame(get_month_range())
#     # print("Inside month function")
#     # print(dt_range.loc[0,["src_mnth"]])
#     return dt_range


@data_loader
def load_mnth_data_from_postgres(*args, **kwargs):
    """
    Template for loading data from a PostgreSQL database.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#postgresql
    """

    query = f"""
    select concat(sm."Seller App" , concat('__',sm.provider_id)) as provider_key,
    sm."Date" as order_date,
    sm.category as category,
    sm."Sub - Category" as sub_category,
    sm.pin_code
    from public.sku_master sm
    where extract (month from sm."Date") = '{mnth}'
    and extract (year from sm."Date") = '{year}';"""

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