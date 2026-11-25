"""Compatibility entry point for the V8 make-all pipeline."""
from action_make_all import cli
from working import run


def main(**kwargs):
    run(**dict(kwargs, generate_stl=False))


if __name__ == "__main__":
    cli(default_stl=False)
