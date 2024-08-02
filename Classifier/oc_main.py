import pickle
import warnings
warnings.filterwarnings("ignore")

# B classifier function
def classify_o(features):
    # path of OUR encoder file in your google drive
    path_encoder = r'C:\Users\vedas\Downloads\s24_fp_Veda\s24_fp_Veda\G2\encoder_o.pkl'

    # path of OUR model file in your google drive
    path_model = r'C:\Users\vedas\Downloads\s24_fp_Veda\s24_fp_Veda\G2\model_o.pkl'
    
    # Load encoder
    with open(path_encoder, 'rb') as f:
        encoder = pickle.load(f)

    # Load model
    with open(path_model, 'rb') as f:
        model = pickle.load(f)

    pred = model.predict([features])
    return encoder.inverse_transform(pred)[0]