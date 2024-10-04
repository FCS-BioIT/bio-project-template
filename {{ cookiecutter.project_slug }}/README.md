# {{ cookiecutter.description }}

Lead analyst: {{ cookiecutter.author }}

## Short description of the project

## Reproducibility and how to run the project

1. Primary analysis

2. Statistical analysis results

3. Downstream analysis

- Create a conda environment

```bash
conda env create --file=envs/main.yaml
conda activate {{ cookiecutter.project_slug }}
```

- Run the project

```bash
bash run.sh
```
