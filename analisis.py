import pandas as pd

try:
    df_integration = pd.read_csv("data_integration.csv")

    desc_stats = df_integration.describe(include="all")

    missing = df_integration.isnull().sum()

    analysis = pd.DataFrame({
        "missing_values": missing,
        "data_type": df_integration.dtypes.astype(str)
    })

    analysis = analysis.join(desc_stats.transpose(), how="left")

    analysis.to_csv("data_analysis.csv")

    print("Tahap 3 (Analisis) selesai → data_analysis.csv berhasil dibuat")

except Exception as e:
    print("Error di tahap Analisis:", e)
