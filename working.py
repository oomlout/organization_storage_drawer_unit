"""Run the V8 population, OOMP and SCAD stages in order."""
from contextlib import chdir
from pathlib import Path


def run(*, output_dir=None, part=None, run_oomp_populate=True, run_oomp=True,
        run_scad=True, generate_stl=True, **kwargs):
    import working_oomp_populate as population
    import working_oomp
    import working_scad

    project = Path(__file__).resolve().parent
    root = Path(output_dir).resolve() if output_dir is not None else project
    if root.is_relative_to(project / "history"):
        raise ValueError("Choose an output directory outside the historical archive")
    population.selected_options(part)  # Reject unknown parts before writing.
    root.mkdir(parents=True, exist_ok=True)
    with chdir(root):
        if run_oomp_populate:
            population.main(part=part)
        if run_oomp:
            working_oomp.main(part=part)
        if run_scad:
            working_scad.main(part=part, generate_stl=generate_stl)


main = run

if __name__ == "__main__":
    from action_make_all import cli
    cli()
