import pandas as pd
from fastapi import FastAPI
import sqlite3
from app.db import get_connection

app = FastAPI(title="Sales API")

def query(sql: str) -> pd.DataFrame:
    with get_connection() as conn:
        df = pd.read_sql(sql, conn)

    # 🔹 Limpiar valores incompatibles con JSON
    df = df.replace([float("inf"), float("-inf")], None)
    df = df.where(pd.notnull(df), None)

    return df

    
@app.get("/sales/monthly")
def sales_by_month():
    sql = """
    SELECT d.year, d.month, SUM(f.total) AS total_sales
    FROM fact_sales f
    JOIN dim_date d ON f.date_id = d.date_id
    GROUP BY d.year, d.month
    ORDER BY d.year, d.month
    """

    df = query(sql)
    return df.to_dict(orient="records")


@app.get("/sales/top")
def top_customers():
    sql = """
    SELECT 
        COALESCE(c.customer_name, 'UNKNOWN') AS customer_name,
        COALESCE(SUM(f.total), 0) AS total_sales
    FROM fact_sales f
    JOIN dim_customer c ON f.customer_id = c.customer_id
    GROUP BY c.customer_name
    ORDER BY total_sales DESC
    LIMIT 5
    """

    try:
        df = query(sql)

        if df.empty:
            return []

        return df.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving top customers: {str(e)}"
        )




