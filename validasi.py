import pandas as pd

try:
    df_integration = pd.read_csv("data_integration.csv")

    df_validation = df_integration.dropna(how="all")

    for col in df_validation.columns:
        if df_validation[col].dtype in ["float64", "int64"]:
            median_val = df_validation[col].median()
            df_validation[col].fillna(median_val, inplace=True)
        else:
            mode_val = df_validation[col].mode()
            if not mode_val.empty:
                df_validation[col].fillna(mode_val[0], inplace=True)

    df_validation.to_csv("data_validation.csv", index=False)

    print("✅ Tahap 4 (Validasi) selesai → data_validation.csv berhasil dibuat")

except Exception as e:
    print("❌ Error di tahap Validasi:", e)
