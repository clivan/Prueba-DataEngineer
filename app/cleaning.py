import pandas as pd

def clean_numeric(series: pd.Series)->pd.Series:
    return(series.astype(str).str.replace("r[^\d\.-]", "", regex=True).replace("", pd.NA).astype(float))

def clean_data(df: pd.DataFrame)->pd.DataFrame:
    df["issue_date"]=pd.to_datetime(["issue_date"], errors="coerce").dt.date
    for col in ["qty", "unit_price", "total"]:
        df[col]=clean_numeric(df[col])

    df["customer_name"]=df["customer_name"].str.upper().str.strip()
    df=df.drop_duplicates(subset=["invoice_id", "item_description"])
    return df






