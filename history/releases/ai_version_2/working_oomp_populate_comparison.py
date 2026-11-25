"""Editable comparison inputs, applied by ordinary population (never edit output YAML).

CAD mass assumes solid PLA at 1.24 g/cm3, including adhesion ears. It is not
a slicer estimate. Pot prices include 20% VAT, exclude shipping, and allocate
a single 500-piece carton; lids are purchased but are not used or weighed.
"""
import hashlib
import json
from pathlib import Path

from oomp_populate_helper import build_oomp_id

ROOT = Path(__file__).resolve().parent
FILAMENT_GBP_PER_GRAM = 0.01
PLA_DENSITY_G_PER_CM3 = 1.24

POTS = {
    "209": {
        "manufacturer": "Systempak",
        "part_number": "209",
        "capacity_ml": 100,
        "pack_quantity": 500,
        "pack_price_ex_vat_gbp": 60.95,
        "vat_rate": 0.20,
        "weight_g": 8.0,
        "price_source_url": "https://systempak.net/product/100ml-rectangular-tamper-evident-containers-and-lids/",
        "weight_source_url": "https://systempak.net/wp-content/uploads/2024/03/TDS-209-100ML.pdf",
        "checked_date": "2026-10-18",
        "availability": "On backorder",
        "price_basis": "Single carton of 500 pots and lids; lids unused; delivery excluded",
    },
    "214": {
        "manufacturer": "Systempak",
        "part_number": "214",
        "capacity_ml": 550,
        "pack_quantity": 500,
        "pack_price_ex_vat_gbp": 80.95,
        "vat_rate": 0.20,
        "weight_g": 16.0,
        "price_source_url": "https://systempak.net/product/550ml-rectangular-tamper-evident-containers-and-lids/",
        "weight_source_url": "https://systempak.net/wp-content/uploads/2024/03/TDS-214-550ML.pdf",
        "checked_date": "2026-10-18",
        "availability": "On backorder",
        "price_basis": "Single carton of 500 pots and lids; lids unused; delivery excluded",
    },
}


def geometry_fingerprint(part):
    digest = hashlib.sha256(json.dumps(part["oobb_details"], sort_keys=True).encode())
    for filename in ["working_scad.py", "working_scad_container_cutout.py", "scad_help.py"]:
        digest.update((ROOT / filename).read_bytes())
    return digest.hexdigest()


def enrich(extras):
    cache_path = ROOT / "drawer_comparison" / "cad_measurements.json"
    measurements = json.loads(cache_path.read_text()) if cache_path.exists() else {}
    for part in extras:
        if not part.get("oobb_details"):
            continue
        code = part["container"].rsplit("_", 1)[-1]
        pot = dict(POTS[code])
        # Prefer explicit price data on a local container record when available.
        # The container record is separate from the generated frame record.
        import yaml
        for directory in [ROOT / "parts", Path("C:/gh/oomlout_oomp_version_5/parts")]:
            path = directory / part["container"] / "working.yaml"
            if path.exists():
                data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
                if data.get("price_gbp") is not None and data.get("price_includes_vat") is True:
                    pot["unit_price_gbp"] = data["price_gbp"] / data.get("price_quantity", 1)
                    pot["price_basis"] = "Existing container working.yaml; VAT-inclusive price / price_quantity"
                    pot["price_source_url"] = data.get("for_sale_url", pot["price_source_url"])
                    break
        pot.setdefault("unit_price_gbp", pot["pack_price_ex_vat_gbp"] * (1 + pot["vat_rate"]) / pot["pack_quantity"])
        role = part.get("part_role", "frame")
        count = part["column"] * part["row"] * (2 if role == "bank_layout" else 1)
        component = part.get("assembly_half") in ["front", "back"]
        joint_trial = "joint_test_depth" in part
        part.update({
            "record_type": "printed_drawer_unit",
            "product_name": f"Printed {part['column']} × {part['row']} · Systempak {code} · {part['style'].replace('_', ' ')}" + (f" · {part['variant'].replace('_', ' ')}" if part.get("variant") else ""),
            "manufacturer": "oomlout",
            "drawer_count": count,
            "drawer_capacity_ml": pot["capacity_ml"],
            "drawer_capacity_basis": "manufacturer_nominal",
            "comparison_sample": role != "frame" or component or joint_trial,
            "assembly_component": component,
            "pot_quantity": 0 if component or joint_trial else count,
            "print_instruction": ("3dpr.scad contains both halves flat. Use front.scad and back.scad for separate plates; assembled.scad shows the assembly."
                                  if part.get("style") == "ai_version_2" and role == "frame" and not component
                                  else "Print outer face on bed, joint facing up." if component else ""),
            "hardware_cost_basis": "M3 screws and nuts excluded; hardware price not supplied" if part.get("style") == "ai_version_2" and role == "frame" else "No assembly hardware",
            "pot_cost_details": pot,
            "filament_gbp_per_gram": FILAMENT_GBP_PER_GRAM,
            "filament_density_g_per_cm3": PLA_DENSITY_G_PER_CM3,
            "filament_mass_basis": "Solid CAD volume × assumed PLA density; includes adhesion ears; excludes purge/supports",
            "price_includes_vat": True,
            "price_excludes_delivery": True,
            "availability": "Print yourself; pots on backorder at research date",
            "comparison_image": "comparison.png",
        })
        record = measurements.get(build_oomp_id(part), {})
        if record.get("fingerprint") != geometry_fingerprint(part):
            part["comparison_measurement_status"] = "Run action_prepare_drawer_comparison.py to refresh CAD measurements"
            continue
        mass = record["volume_mm3"] / 1000 * PLA_DENSITY_G_PER_CM3
        filament = mass * FILAMENT_GBP_PER_GRAM
        pots = 0 if component or joint_trial else count * pot["unit_price_gbp"]
        total = filament + pots
        weight = (mass + (0 if component or joint_trial else count * pot["weight_g"])) / 1000
        part.update({
            "cad_volume_mm3": record["volume_mm3"],
            "filament_mass_g": round(mass, 3),
            "filament_cost_gbp": round(filament, 4),
            "pots_cost_gbp": round(pots, 4),
            "price_gbp": round(total, 4),
            "cost_per_drawer_gbp": round(total / count, 4),
            "weight_kg": round(weight, 6),
            "weight_basis": ("estimated_joint_fit_pair_no_pots_or_hardware" if joint_trial else
                             "estimated_solid_PLA_half_including_ears_no_pots_or_hardware" if component else
                             "estimated_solid_PLA_frame_including_ears_plus_lidless_pots_excluding_hardware"),
            "cost_per_kg_gbp": round(total / weight, 4),
            "cost_per_kg_basis": "Estimated empty assembled unit including pots and adhesion ears",
            "width_mm": record["finished_envelope_mm"][0],
            "height_mm": record["finished_envelope_mm"][1],
            "depth_mm": record["finished_envelope_mm"][2],
            "comparison_measurement_status": "current",
        })
