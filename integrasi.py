import pandas as pd

try:
    df = pd.read_csv("data_collecting.csv")

    df = df.drop_duplicates()

    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

    df.to_csv("data_integration.csv", index=False)

    print("✅ Tahap 2 (Integrasi) selesai → data_integration.csv berhasil dibuat")

except Exception as e:
    print("❌ Error di tahap Integrasi:", e)
