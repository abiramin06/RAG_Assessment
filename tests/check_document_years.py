import json
import re

with open("results/chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

year_pattern = re.compile(r"\b20\d{2}\b")

year_sources = {}

for chunk in chunks:
    years = set(year_pattern.findall(chunk.get("text", "")))

    for year in years:
        year_sources.setdefault(year, set()).add(
            chunk.get("source", "Unknown")
        )

print("\n===== DOCUMENT YEAR CHECK =====")

if year_sources:
    for year in sorted(year_sources):
        print(f"\nYear: {year}")
        print("Documents:", len(year_sources[year]))

        for source in sorted(year_sources[year])[:5]:
            print(" -", source)
else:
    print("No years between 2000 and 2099 found.")