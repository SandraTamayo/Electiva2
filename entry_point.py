import os
import joblib
def model_fn(model_path):
    return joblib.load(os.path.join(model_path,'modelrf.joblib'))
