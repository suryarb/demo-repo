
import os
os.chdir("/workspaces/expenses/")
import numpy as np
import pandas as pd
import warnings
import src.utils as utils
import src.prepare_data as prepare_data

warnings.filterwarnings('ignore')
pd.options.display.float_format = "{:,.5f}".format
pd.set_option('display.max_columns', None)

config = utils.load_config()
datasets = utils.load_data(config)
df = prepare_data.prepare(datasets)

calc = (df[df['expense_category'].isnull()]
          .groupby(['merchant'])
          .agg(count=('merchant', 'count')
            , sum=('transaction_amount', 'sum')
            , date_from=('date', 'min')
            , date_to=('date', 'max')
                    )
          .reset_index()
)
print(calc.sort_values(by=['count'], ascending=[False]).head())
