import pandas as pd

try:
    df = pd.read_csv("camera_dataset.csv")

    df.to_csv("data_collecting.csv", index=False)

    print("Tahap 1 (Collecting) selesai → data_collecting.csv berhasil dibuat")

except Exception as e:
    print("Error di tahap Collecting:", e)
