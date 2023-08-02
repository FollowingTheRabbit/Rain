# Rain
Calibration of a mechanical rain sensor

This project is a solution to the FielPro case. It is a public repository with a free software license. You can clone and run *requirements.txt* to test it on your own computer.

The codes are in the *./src directory
- The *analyse.ipynb* is a notebook with the descriptive analysis and model building.
- *main.py* contains the implementation of the model in *streamlite*.
- The file *Rain.py* contains the class with the final model and some other functions for handling the data.

The data used to train the model is in *./data/FieldPRO Data Challenge* also with the case
- *Sensor_FieldPRO.csv* the sensor data.
- *Station_Conventional.csv* a nearby weather station.
- *desafio.pdf* the case is in Portuguese.

The models are saved in pickle format to be used in the deployment in the directory *./model*
- *Rain_Clas.pkl* the classification model distinguishes between rain and no rain.
- Rain_Reg.pkl* the regression model predicts rainfall values.
- Both models create the class *Rain.pkl* which is the model used as *calibrator*.

The implemented model can be found at https://nnivqptu4cphbiiubulut7.streamlit.app/. The model can be used by giving it an input such as *data/FieldPRO/Sensor_FieldPRO.csv*.

The image stored in the *./img* directory gives some visual information to help add the correct file. It will be updated in a future update.