# VAR example
from statsmodels.tsa.vector_ar.var_model import VAR
from random import random
# contrived dataset with dependency
data_hospital_1 = list()
data_hospital_2 = list()
data_hospital_3 = list()
for i in range(100):
    hospital_1_v1 = 300 + random()
    hospital_1_v2 = 500 + random()
    hospital_2_v1 = 1000 + random()
    hospital_2_v2 = 700 + random()
    hospital_3_v1 = 650 + random()
    hospital_3_v2 = 1400 + random()
    row_hospital_1 = [hospital_1_v1,hospital_1_v2]
    row_hospital_2 = [hospital_2_v1,hospital_2_v2]
    row_hospital_3 = [hospital_3_v1,hospital_3_v2]
    data_hospital_1.append(row_hospital_1)
    data_hospital_2.append(row_hospital_2)
    data_hospital_3.append(row_hospital_3)

# fit model

# Hospital 1
hospital_1_model = VAR(data_hospital_1)
hospital_1_model_fit = hospital_1_model.fit()
# make prediction
hospital_1_yhat = hospital_1_model_fit.forecast(hospital_1_model_fit.y, steps=1)


# Hospital 2
hospital_2_model = VAR(data_hospital_2)
hospital_2_model_fit = hospital_2_model.fit()
# make prediction
hospital_2_yhat = hospital_2_model_fit.forecast(hospital_2_model_fit.y, steps=1)

# Hospital 2
hospital_3_model = VAR(data_hospital_3)
hospital_3_model_fit = hospital_3_model.fit()
# make prediction
hospital_3_yhat = hospital_3_model_fit.forecast(hospital_3_model_fit.y, steps=1)
