def load_to_sqlite(df, customers, dates, conn):
    customers.to_sql("dim_customer", conn, if_exists="replace", index=False)
    dates.to_sql("dim_date", conn, if_exists="replace", index=False)
    fact=df.rename(columns={"issue_date": "date_id"})
    fact.to_sql("fact_sales", conn, if_exists="replace", index=False)

