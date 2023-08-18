[Understanding Feature Output (featuretools docs)](https://featuretools.alteryx.com/en/stable/#Understanding-Feature-Output)

```python
  feature_matrix_customers, feature_defs = ft.dfs(
	  dataframes=dataframes,
	  relationships=relationships,
	  target_dataframe_name="customers"
  )
```

Use `feature_defs[0]` to see the definition of the first feature

[Feature lineage graphs (featuretools docs)](https://featuretools.alteryx.com/en/stable/#Feature-lineage-graphs)

```python
ft.graph_feature(feature)
```

![[index_22_0.svg]]
