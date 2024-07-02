# Coccidiosis_Chicken_Diseases_classification

#### Start with installing all the requirements:
```python
pip install -r requirements.txt
```
#### Initialize DVC environment(make sure that you have git initialized already in current working directory before this step!)
```powershell
dvc init
```
#### DVC reproduce to checks the pipeline stages defined in your DVC files
```powershell
dvc repro
```
#### Finally run the `app.py` in your terminal

## Workflows

1. Update config.yaml
2. Update secrets.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.py

## The cycle goes from:

- Data Ingestion
- Prepare Base Model
- Prepare Callbacks
- Model Trainer
- Model Evaluation
- Write DVC file for tracking pipelines
