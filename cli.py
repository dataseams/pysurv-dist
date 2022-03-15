"""Run the package_name functions in terminal."""
import click

import pysurv_dist


@click.group()
def cli():
    """Provide a terminal interface to the package."""
    pass


@click.command()
@click.argument()
def run(file_path):
    """Generate feature distances based on a given data file."""
    print("Done")


cli.add_command(run)

if __name__ == "__main__":
    cli()
