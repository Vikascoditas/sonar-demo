# A Python project to demonstrate SonarQube

## Run the following commands

```shell
# Create virtual environment
python -m venv sonar

# Activate the virtual environment
source ./sonar/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the python script
python src/main.py

# Run tests
python -m unittest

# Generate Coverage xml file as per Cobertura standards
coverage run -m unittest tests/test_main.py
coverage xml
```
