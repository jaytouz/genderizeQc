# genderizeQc
infer gender based on first name with 400k names between 1980-2020 from donneesquebec's database

# data source
https://www.donneesquebec.ca/recherche/dataset/banque-de-prenoms-garcons
https://www.donneesquebec.ca/recherche/dataset/banque-de-prenoms-filles

# installl
```bash
pip install genderizerQc
```
# How to use
```py
from genderizeQc import GenderizerQc

g = GenderizerQc()
listName = ["maxime", "claude", "jeremie", "danielle", "vanessa"]
print(g.genderize(listName))
```
output 
```bash
[{'name': 'maxime', 'gender': 'male', 'probability': 0.9682529502308876, 'count': 31184, 'country_id': 'Qc'}, {'name': 'claude', 'gender': 'male', 'probability': 0.7751004016064257, 'count': 1245, 'country_id': 'Qc'}, {'name': 'jeremie', 'gender': 'male', 'probability': 0.9925055356838699, 'count': 5871, 'country_id': 'Qc'}, {'name': 'danielle', 'gender': 'female', 'probability': 0.9888663967611336, 'count': 988, 'country_id': 'Qc'}, {'name': 'vanessa', 'gender': 'female', 'probability': 0.9978930010993038, 'count': 10916, 'country_id': 'Qc'}]
```
