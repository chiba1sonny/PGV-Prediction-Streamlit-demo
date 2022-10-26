# A Streamlit demo for PFV prediction
Created a demo for PGV prediction. PGV means peak ground velocity and it is an earthquake intensity. PGV is widely used in both deterministic and probabilistic seismic hazard analyses. 

PGV depends on source characteristics (e.g., earthquake magnitude), the propagation path (e.g., the shortest distance from the fault), and the local site conditions. Basiclly, PGV had been obtained by empirical equation until the machine learning and big data booming. As the development of statistical analysis methods and more ground motion records are obtained, the research of attenuation relationship of PGV has been greatly developed.

So in this repo, firstly, a XGBoost model for PGV prediction is constructed and the model is saved as json data. Then created a simple application for PGV prediction using Streamlit.

## 1.Requirements
- xgboost
- pandas
- matplotlib
- seaborn
- sklearn
- pathlib
- streamlit

## 2.Data
This repo used ground motion data obtained by K-NET (Kyoshin network) and KiK-net (Kiban Kyoshin network), which are strong-motion seismograph networks constructed by the National Research Institute for Earth Science and Disaster prevention (NIED), Japan. 6,944 ground motion records at 1,184 K-NET and KiK-net seismic observation stations which were observed during the 32 earthquakes are employed.
- PGV is used as the objective variable
- the moment magnitude (Mw), the shortest distance from the fault (Distance), the earthquake source depth (Depth) are used as the explanatory variables

## 3.Model
As a simple example, I used XGBoost Regressor to deal with the data and obtained the model, which is available in ml.py.

## 4.App
We have our model and we can use it to predict the PGV (I have attached the model as model.json). Then we can build a simple app using streamlit. It is very easy and readble. Have a look at main.py. After building it, just run main.py to get the app in action like below.

![Screenshot from 2022-10-26 18-03-24](https://user-images.githubusercontent.com/68838083/197983860-d89e74eb-409e-44fc-beb9-a24432cda24e.png)

