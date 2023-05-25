# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM silver.pizza_query.pedido
# MAGIC WHERE flKetchup IS NOT NULL

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM silver.pizza_query.pedido
# MAGIC WHERE descUF = 'Goiás'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT descUF, count(*) AS qtdePedidos
# MAGIC FROM silver.pizza_query.pedido 
# MAGIC
# MAGIC WHERE descUF != 'São Paulo' AND descUF != 'Rio de Janeiro'
# MAGIC
# MAGIC GROUP BY descUF
# MAGIC ORDER BY qtdePedidos DESC
# MAGIC
# MAGIC LIMIT 10

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT flKetchup, count(*) AS ket
# MAGIC FROM silver.pizza_query.pedido
# MAGIC
# MAGIC WHERE flKetchup IS NOT NULL
# MAGIC
# MAGIC GROUP BY flKetchup
# MAGIC ORDER BY ket DESC
# MAGIC
# MAGIC LIMIT 6

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM silver.pizza_query.produto
# MAGIC WHERE descItem LIKE '%laranja%'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT descUF, count(*) AS qtdePedidos
# MAGIC FROM silver.pizza_query.pedido 
# MAGIC
# MAGIC WHERE descUF != 'São Paulo' AND descUF != 'Rio de Janeiro'
# MAGIC
# MAGIC GROUP BY descUF
# MAGIC HAVING qtdePedidos <= 75 AND qtdePedidos >= 20
# MAGIC ORDER BY qtdePedidos DESC
# MAGIC
# MAGIC LIMIT 10

# COMMAND ----------


