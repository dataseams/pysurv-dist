"""Module to get required pip packages from conda environment.yml file."""
import re


def get(tags=[]):
    """Compile requirements by tag from conda's environment.yml file."""
    with open("environment.yml", "r") as f:
        conda_env_yml = f.readlines()
        pip_idx = conda_env_yml.index("  - pip:\n")
        requirements = conda_env_yml[pip_idx + 1 :]

        if tags:
            requirements = [r for r in requirements for t in tags if t in r]

        requirements = [re.sub("^[ ]*[- ]", "", r) for r in requirements]
        requirements = [
            re.sub(r"[ ]*[#][a-z]*\n$", "", r) for r in requirements
        ]

    return requirements


def get_ssv(tags=[]):
    """Combile pip requirements by tag from conda's environment.yml file."""
    requirements = get(tags=tags)

    return " ".join(requirements)
