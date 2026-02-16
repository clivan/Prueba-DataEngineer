from app.entry import load_raw_data
from app.cleaning import clean_data
from app.modeling import build_dimensions
from app.db import get_connection
from app.loading import load_to_sqlite

def run():
    df=load_raw_data("data/raw/2026012_data.csv")
    df=clean_data(df)
    customers, dates=build_dimensions(df)

    conn=get_connection()
    load_to_sqlite(df, customers, dates, conn)
    conn.close()

if __name__=="__main__":
    run()


    