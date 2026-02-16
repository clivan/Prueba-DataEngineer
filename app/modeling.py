import pandas as pd

def build_dimensions(df):
    customers=(df[["customer_id", "customer_name"]].drop_duplicates().reset_index(drop=True))
    dates=(df[["issue_date"]].drop_duplicates().assign(year=lambda x: pd.to_datetime(x["issue_date"]).dt.year, month=lambda x: pd.to_datetime(x["issue_date"]).dt.month).rename(columns={"issue_date": "date_id"}))
    return customers, dates
