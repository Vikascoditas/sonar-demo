# A python project to demonstrate SonarQube

## Run the following commands

```shell
python -m venv sonar
source ./sonar/bin/activate
pip install -r requirements.txt

# Run the python script
python src/main.py

# Run tests
python -m unittest

# Generate Coverage xml file as per Cobertura standards
coverage run -m unittest tests/test_main.py
coverage xml
```
