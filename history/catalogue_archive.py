"""Locate locked historical geometry after the user-requested catalogue cleanup."""
from pathlib import Path


def historical_parts(root):
    root=Path(root)
    archive=root/'parts_old_1'
    return archive if archive.is_dir() else root/'parts'
