import pandas as pd
import numpy as np

df = pd.read_csv("outputs/powerbi/fact_scenarios.csv")

for c in ["lost_sales_usd","overstock_cost_usd","net_impact_usd"]:
    df[c] = (
        df[c].astype(str)
             .str.replace(",", "", regex=False)
             .str.replace("$", "", regex=False)
             .replace(["nan","NaN","Infinity","-Infinity",""], np.nan)
    )
    df[c] = pd.to_numeric(df[c], errors="coerce")

df.to_csv("outputs/powerbi/fact_scenarios_clean.csv", index=False)
print("Wrote outputs/powerbi/fact_scenarios_clean.csv")
