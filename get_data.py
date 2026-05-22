import pandas as pd

# Header configuration to prevent Wikipedia from blocking the request
options = {"storage_options": {"User-Agent": "Mozilla/5.0"}}

# Download the specific table using its unique caption
url = "https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations"
target_caption = "Codes and abbreviations for U.S. states, federal district, territories, and other regions"

df_states = pd.read_html(url, match=target_caption, **options)[0]

# Save to CSV file
df_states.to_csv("us_states_abbreviations_full.csv", index=False, encoding="utf-8")


# Download and save the state population table (extracting the first table from the list)
url_pop = "https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population"
target_caption_pop = "Census population"

df_pop = pd.read_html(url_pop, match=target_caption_pop, **options)[0]

# Save to CSV file
df_pop.to_csv("us_states_by_population.csv", index=False, encoding="utf-8")

print("Both CSV files have been successfully saved!")