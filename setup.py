from setuptools import setup, find_packages

setup(
    name="Nessus Solution Tool",
    version="0.0.1a",
    description="Pulls the solution from Nessus for a given issue",
    author="Ed Cradock",
    license="MIT",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "nessus-solution-tool=nessus_solution_tool:main"
        ]
    }
)
