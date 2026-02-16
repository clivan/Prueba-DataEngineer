CREATE TABLE dim_customer
(
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT
);

CREATE TABLE dim_date
(
    date_id DATE PRIMARY KEY,
    year INTEGER,
    month INTEGER
);

CREATE TABLE fact_sales
(
    invoice_id TEXT,
    date_id DATE,
    customer_id TEXT,
    qty REAL,
    unit_price REAL,
    total REAL,
    status NEXT,
    FOREIGN KEY(customer_id), REFERENCES dim_customer(customer_id),
    FOREIGN KEY(date_id), REFERENCES dim_date(date_id)
);

