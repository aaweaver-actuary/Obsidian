
1.  load dataframes
2. put dataframes in a dictionary:
   
   ```python 
   # include index column and time index (if applicable)
   dataframes = {
	   "customers": (customers_df, "customer_id"),
	   "sessions": (sessions_df, "session_start"),
	   "transactions": 
		   (transactions_df, "transaction_id", "transaction_time")
   }
```

3. define a series of relationships between dataframes:
   ```python
   relationships = [
	   ("sessions", "session_id", "transactions", "session_id"),
	   ("customers", "customer_id", "sessions", "customer_id")
   ]
```
	
> [!info]
> use the `EntitySet` class - it has a convenient API for managing data like this
> 
	
4. run deep feature synthesis ( [[featuretools does deep feature synthesis]] )
	- minimal input: `dict` of `pd.DataFrame`'s'
  ```python
  feature_matrix_customers, feature_defs = ft.dfs(
	  dataframes=dataframes,
	  relationships=relationships,
	  target_dataframe_name="customers"
  )
```

- this produces dozens of new features

[[featuretools contains methods to help understand feature output]]





