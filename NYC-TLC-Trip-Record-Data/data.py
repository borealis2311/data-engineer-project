import pandas as pd
df = pd.read_parquet("NYC-TLC-Trip-Record-Data\yellow_tripdata_2026-01.parquet")
print(df.columns.tolist())

print(df.dtypes)   # schema có sẵn
print(len(df))     # ~3 triệu dòng, file chỉ ~50MB