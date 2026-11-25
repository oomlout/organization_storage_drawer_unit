"""User-authorized catalogue removals, without rewriting release manifests.

On 2026-10-19 the user retired the three clearance-fit variants from ALL
versions. Their frozen geometry remains in the release archives. This is only
an exception to the active model set; every retained model still must match.
"""

RETIRED_CLEARANCE_VARIANTS = frozenset({
    "fit_clearance_0d75", "fit_clearance_1d5", "fit_clearance_2d25",
})


def active_release_parts(parts):
    active = {}
    retired = []
    for name, expected in parts.items():
        inputs = expected["oobb_details"]
        if inputs.get("part_role") == "fit" and inputs.get("variant") in RETIRED_CLEARANCE_VARIANTS:
            retired.append(name)
        else:
            active[name] = expected
    return active, retired
