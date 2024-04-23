# MLOPS work Flow

### ML model notebook

Apply data handling and preprocessing on loan approval dataset.

Then train DecisionTreeRegressor on data set and get the resuls. 

> results are not important right now as accuracy is not the focus.

serilization of model using joblib

```py
# Serialization of model
import joblib as jb
jb.dump(<MODEL>, "<NAME_OF_MODEL>.pkl")

# Decerializing the model
model = jb.load("<NAME_OF_MODEL>.pkl")
```

To save installed environment use `pip freeze > requirment.txt`

## Modulirization

Notebook are good for testing purposes but not sutable for development and projuction environments.

To module any python code. you must put `__init__.py` file in that foulder or sub-foulder.


