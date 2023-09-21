[[featuretools is a package for automating feature engineering]]

1. [initialize](https://featuretools.alteryx.com/en/stable/getting_started/using_entitysets.html#Creating-an-EntitySet)

   ```python
   ft.EntitySet(id="customer_data")
```

2. [add `DataFrames`](https://featuretools.alteryx.com/en/stable/getting_started/using_entitysets.html#Adding-dataframes)

```python
from woodwork.logical_types import Categorical, PostalCode

es = es.add_dataframe(
	dataframe_name="transactions",
	dataframe=transactions_df,
	index="transaction_id",
	time_index="transaction_time",
	logical_types={
		"product_id": Categorical,
		"zip_code": PostalCode,
	},
)
```

