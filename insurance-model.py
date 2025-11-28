import pycaret
from pycaret.datasets import get_data
data = get_data('insurance')

from pycaret.regression import *
s = setup(data, target='charges', session_id=123,
          normalize=True,
          polynomial_features=True,
          trigonometry_features=True,
          feature_interaction=True,
          bin_numeric_features=['age', 'bmi'])
lr = create_model('lr')
save_model(lr, 'insurance-lr-model')
print("Model saved successfully.")
# To load the model later, use:
# loaded_model = load_model('insurance-lr-model')
print("Loaded model", load_model('insurance-lr-model'))
