import os
import pandas as pd
import matplotlib.pyplot as plt
from app.db import get_connection

OUTPUT_DIR="output"

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def sales_trend():
    query="""
    SELECT d.year, d.month, SUM(f.total) AS total
    FROM fact_sales f
    JOIN dim_date d ON f.date_id = d.date_id
    GROUP BY d.year, d.month
    ORDER BY d.year, d.month
    """

    with get_connection() as conn:
        df=pd.read_sql(query, conn)

    if df.empty:
        print("No hay datos para tendencia histórica.")
        return

    df=df.dropna(subset=["year", "month", "total"])

    if df.empty:
        print("Todos los registros eran nulos.")
        return

    # Convertir tipos
    df["year"]=df["year"].astype(int)
    df["month"]=df["month"].astype(int)
    df["total"]=pd.to_numeric(df["total"], errors="coerce")

    # Construir fecha real
    df["date"]=pd.to_datetime(
        df["year"].astype(str) + "-" +
        df["month"].astype(str).str.zfill(2) + "-01"
    )

    df=df.sort_values("date")

    plt.figure()
    plt.plot(df["date"], df["total"])
    plt.xticks(rotation=45)
    plt.title("Tendencia histórica de ventas")
    plt.tight_layout()
    plt.savefig("output/sales_trend.png")
    plt.close()

    print("Gráfica de tendencia generada.")


def pending_amount():
    query = """
    SELECT c.customer_name, SUM(f.total) AS pending
    FROM fact_sales f
    JOIN dim_customer c ON f.customer_id = c.customer_id
    WHERE f.status != 'PAID'
    GROUP BY c.customer_name
    ORDER BY pending DESC
    LIMIT 10
    """

    with get_connection() as conn:
        df=pd.read_sql(query, conn)

    if df.empty:
        print("No hay datos pendientes.")
        return

    # Eliminar NULLs antes de graficar
    df = df.dropna(subset=["customer_name", "pending"])

    if df.empty:
        print("Todos los registros tenían valores nulos.")
        return

    # Asegurar tipos correctos
    df["customer_name"] = df["customer_name"].astype(str)
    df["pending"] = pd.to_numeric(df["pending"], errors="coerce")

    plt.figure()
    plt.bar(df["customer_name"].tolist(), df["pending"].tolist())
    plt.xticks(rotation=45)
    plt.title("Top Deudores")
    plt.tight_layout()
    plt.savefig("output/pending.png")
    plt.close()



def run():
    ensure_output_dir()
    sales_trend()
    pending_amount()
    print("Dashboard generado correctamente.")


if __name__=="__main__":
    run()
