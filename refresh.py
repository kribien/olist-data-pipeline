from pathlib import Path
import subprocess

import duckdb

from ingest import DATABASE_PATH, load_raw

ROOT = Path(__file__).resolve().parent


def run_dbt() -> None:
    subprocess.run(["dbt", "build"], cwd=ROOT, check=True)
def show_summary() -> None:
    with duckdb.connect(str(DATABASE_PATH), read_only=True) as connection:
        order_count, item_count, gross_sales_value = connection.execute(
            """
            SELECT
                COUNT(DISTINCT order_id),
                COUNT(*),
                SUM(gross_item_value)
            FROM analytics.fact_order_items
            """
        ).fetchone()

    print("\nRésumé prêt pour le dashboard")
    print(f"Commandes: {order_count:,}")
    print(f"Lignes de commande: {item_count:,}")
    print(f"Valeur brute: {gross_sales_value:,.2f}")

def main() -> None:
    counts = load_raw()
    for name, count in counts.items():
        print(f"raw.{name}: {count:,} lignes")
    show_summary()

    run_dbt()


if __name__ == "__main__":
    main()