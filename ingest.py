from pathlib import Path

import duckdb

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data" / "raw"
DATABASE_PATH = ROOT / "olist.duckdb"

CSV_TABLES = {
    "customers": "olist_customers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "order_payments": "olist_order_payments_dataset.csv",
    "order_reviews": "olist_order_reviews_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "product_category_translation": "product_category_name_translation.csv",
}

def load_raw() -> dict[str, int]:
    missing_files = [
        DATA_DIR / filename
        for filename in CSV_TABLES.values()
        if not (DATA_DIR / filename).is_file()
    ]
    if missing_files:
        formatted = "\n".join(str(path) for path in missing_files)
        raise FileNotFoundError(f"Fichiers CSV manquants:\n{formatted}")

    row_counts: dict[str, int] = {}

    with duckdb.connect(str(DATABASE_PATH)) as connection:
        connection.execute("CREATE SCHEMA IF NOT EXISTS raw")

        for table_name, filename in CSV_TABLES.items():
            csv_path = (DATA_DIR / filename).as_posix().replace("'", "''")
            connection.execute(f"DROP TABLE IF EXISTS raw.{table_name}")
            connection.execute(
                f"CREATE TABLE raw.{table_name} AS "
                f"SELECT * FROM read_csv('{csv_path}', all_varchar = true)"
            )
            row_count = connection.execute(
                f"SELECT COUNT(*) FROM raw.{table_name}"
            ).fetchone()[0]
            row_counts[table_name] = row_count

    return row_counts

if __name__ == "__main__":
    counts = load_raw()
    for name, count in counts.items():
        print(f"raw.{name}: {count:,} lignes")