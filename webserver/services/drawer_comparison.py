"""One comparison model for purchased cabinets and printed frames."""
from pathlib import Path


SORT_FIELDS = {
    "name": "Product",
    "kind": "Type",
    "drawer_count": "Drawers",
    "capacity_ml": "ml / drawer",
    "total_litres": "Total litres",
    "price": "Unit cost",
    "per_drawer": "£ / drawer",
    "per_litre": "£ / litre",
    "weight_kg": "Empty kg",
    "per_kg": "£ / kg",
    "width_mm": "W mm",
    "height_mm": "H mm",
    "depth_mm": "D mm",
}


def comparison_row(record):
    d = record.get("data", {})
    if d.get("record_type") not in {"purchased_drawer_unit", "printed_drawer_unit"}:
        return None
    printed = d["record_type"] == "printed_drawer_unit"
    count = d.get("drawer_count") if printed else d.get("number_of_drawers")
    capacity = d.get("drawer_capacity_ml")
    litres = count * capacity / 1000 if count and capacity and not d.get("assembly_component") else None
    price = d.get("price_gbp")
    folder = Path(record["part_dir"])
    image = d.get("comparison_image") if printed else d.get("image_static_path")
    if printed and (not image or not (folder / image).exists() or d.get("comparison_measurement_status") != "current"):
        image = None
    return {
        "id": record["id"],
        "name": d.get("product_name", record["id"]),
        "kind": "Printed" if printed else "Purchased",
        "printed": printed,
        "sample": bool(d.get("comparison_sample")),
        "drawer_count": count,
        "capacity_ml": capacity,
        "capacity_estimated": "estimated" in d.get("drawer_capacity_basis", ""),
        "capacity_basis": d.get("drawer_capacity_basis", "").replace("_", " "),
        "total_litres": litres,
        "price": price,
        "per_drawer": price / count if price is not None and count and not d.get("assembly_component") else None,
        "per_litre": price / litres if price is not None and litres else None,
        "weight_kg": d.get("weight_kg"),
        "weight_basis": d.get("weight_basis", "").replace("_", " "),
        "per_kg": d.get("cost_per_kg_gbp"),
        "width_mm": d.get("width_mm"),
        "height_mm": d.get("height_mm"),
        "depth_mm": d.get("depth_mm"),
        "image": image,
        "image_source": d.get("image_source_url"),
        "seller": d.get("seller", "Systempak pots"),
        "source_url": d.get("for_sale_url") or d.get("pot_cost_details", {}).get("price_source_url"),
        "availability": d.get("availability", "Not recorded"),
        "date": d.get("research_date") or d.get("pot_cost_details", {}).get("checked_date"),
        "data": d,
    }


def select_rows(records, args):
    rows = [row for record in records if (row := comparison_row(record)) is not None]
    total = len(rows)
    kind = args.get("kind", "all")
    capacity = args.get("capacity", "all")
    query = args.get("q", "").strip().lower()
    samples = args.get("samples") == "1"
    rows = [r for r in rows if samples or not r["sample"]]
    if kind in {"Printed", "Purchased"}:
        rows = [r for r in rows if r["kind"] == kind]
    if capacity == "small":
        rows = [r for r in rows if r["capacity_ml"] and 200 <= r["capacity_ml"] <= 300]
    elif capacity in {"100", "550"}:
        rows = [r for r in rows if r["capacity_ml"] == int(capacity)]
    if query:
        rows = [r for r in rows if query in (r["name"] + " " + r["id"]).lower()]
    sort = args.get("sort", "per_drawer")
    if sort not in SORT_FIELDS:
        sort = "per_drawer"
    direction = "desc" if args.get("direction") == "desc" else "asc"
    # Unknown values always sort last, even for descending numeric sorts.
    present = [r for r in rows if r[sort] is not None]
    missing = [r for r in rows if r[sort] is None]
    present.sort(key=lambda r: r[sort].casefold() if isinstance(r[sort], str) else r[sort], reverse=direction == "desc")
    return present + missing, total, sort, direction
