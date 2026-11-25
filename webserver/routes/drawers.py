from flask import Blueprint, current_app, render_template, request, url_for

from webserver.services.drawer_comparison import SORT_FIELDS, select_rows

drawers_blueprint = Blueprint("drawers", __name__)


@drawers_blueprint.get("/drawers")
@drawers_blueprint.get("/compare")
def catalog():
    cache = current_app.config["PARTS_CACHE"]
    rows, total, sort, direction = select_rows(cache.get_parts(), request.args)
    table = request.path == "/compare"
    columns = []
    for key, label in SORT_FIELDS.items():
        args = request.args.to_dict()
        args.update(sort=key, direction="desc" if sort == key and direction == "asc" else "asc")
        from urllib.parse import urlencode
        columns.append({"key": key, "label": label, "url": "/compare?" + urlencode(args)})
    for row in rows:
        row["detail_url"] = url_for("parts.part_detail", part_id=row["id"])
        if row["image"]:
            row["image_url"] = url_for("parts.part_image", part_id=row["id"], relative_path=row["image"]) if row["printed"] else url_for("static", filename=row["image"])
    return render_template("drawers.html", rows=rows, total=total, table=table, columns=columns, sort=sort, direction=direction, sort_fields=SORT_FIELDS)
