
import sqlite3
import pandas as pd

con = sqlite3.connect("outputs/dsfr.sqlite")

def q(sql):
    return pd.read_sql_query(sql, con).iloc[0,0]

print("fact_sales", q("select count(1) as n from fact_sales"))
print("fact_features", q("select count(1) as n from fact_features"))
print("fact_forecast_total", q("select count(1) as n from fact_forecast"))
print("fact_forecast_horizon", q("select count(1) as n from fact_forecast where split='horizon'"))
print("fact_forecast_backtest", q("select count(1) as n from fact_forecast where split='backtest'"))
print("fact_scenarios", q("select count(1) as n from fact_scenarios"))

con.close()

