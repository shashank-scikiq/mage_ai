if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df_pc = args[0]
    df_data = data
    df_joined = df_data.merge(df_pc,
    left_on="pin_code",
    right_on="Pincode",
    how="left"
    )
    df_joined.drop(columns = ["index","Pincode","pin_code"], inplace=True)
    df_joined.columns = ["provider_key","order_date","category","sub_category","seller_district","seller_state","seller_state_code"]

    return df_joined


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
