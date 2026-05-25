# Databricks notebook source
# MAGIC %md
# MAGIC ## File reading

# COMMAND ----------

df=spark.read.format("csv").option('header',True).option('inferschema',True).load("/Volumes/workspace/default/databricks2027/empData.csv")
df.display()