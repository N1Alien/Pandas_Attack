import pandas as pd
from pathlib import Path

csv_files = list(Path(".").glob("*.csv"))

if len(csv_files) == 1:
    exit("Run get_data.py to download the necessary datasets.")

# 1. Load the three local databases from your folder
df_abbr = pd.read_csv("us_states_abbreviations_full.csv")
df_pop = pd.read_csv("us_states_by_population.csv")
df_shootings = pd.read_csv("fatal-police-shootings-data.csv")

# 2. Find columns CONTAINING keywords (vectorized approach without loops)
# .str.contains() searches for a match, and [0] extracts the plain string column name
name_col = df_abbr.columns[df_abbr.columns.str.contains("name|region", case=False)][0]
usps_col = df_abbr.columns[df_abbr.columns.str.contains("usps", case=False)][0]
state_col = df_pop.columns[df_pop.columns.str.contains("state", case=False)][0]
pop_col = df_pop.columns[df_pop.columns.str.contains("2020|census", case=False)][0]

# 3. Extract the columns and assign standardized names
df_a = df_abbr[[name_col, usps_col]].set_axis(["State", "USPS"], axis=1)
df_p = df_pop[[state_col, pop_col]].set_axis(["State", "Pop"], axis=1)

# 4. Clean data (convert population to numbers) and count incidents
df_p["Pop"] = pd.to_numeric(df_p["Pop"].astype(str).str.replace(r"[\s,]", "", regex=True), errors="coerce")
df_counts = df_shootings["state"].value_counts().reset_index(name="Incidents")

# 5. Merge the datasets and calculate the incident rate per 1000 residents
df_geo = pd.merge(df_a, df_p, on="State")
df_final = pd.merge(df_counts, df_geo, left_on="state", right_on="USPS")
df_final["Incidents_Per_1000"] = (df_final["Incidents"] / df_final["Pop"]) * 1000

# 6. Sort by the highest rate and save the final output to a CSV file
df_final.sort_values(by="Incidents_Per_1000", ascending=False).to_csv("shootings_rate_per_1000.csv", index=False)
print("Success! The 'shootings_rate_per_1000.csv' file has been saved.")
