# {{ cookiecutter.description }}

Lead analyst: {{ cookiecutter.author }}

## Short description of the project

{{ cookiecutter.description }}

## Reproducibility and how to run the project

1. Primary analysis

Upcoming - this part will be executed by a standardised pipeline.

2. Statistical analysis results

Upcoming - this part will be executed by a standardised pipeline.

3. Downstream analysis

- Create the conda environment

```bash
mamba env create --file=envs/main.yaml
mamba activate {{ cookiecutter.project_slug }}
```

- Run the project

```bash
bash run.sh
```

## Local execution

To run the project locally, you would need access to a slurm simulator. Follow [this link](https://github.com/csf-petr/slurm-simulator) to start a local slurm slurm cluster on Docker.
