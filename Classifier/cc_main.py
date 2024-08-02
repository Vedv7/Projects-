import pickle
import warnings
warnings.filterwarnings("ignore")

# C classifier function
def classify_c(features):
    # path of OUR encoder file in your google drive
    path_encoder = r'C:\Users\vedas\Downloads\s24_fp_Veda\s24_fp_Veda\G2\encoder_c.pkl'

    # path of OUR scaler file in your google drive
    path_scaler = r'C:\Users\vedas\Downloads\s24_fp_Veda\s24_fp_Veda\G2\scaler_c.pkl'

    # path of OUR model file in your google drive
    path_model = r'C:\Users\vedas\Downloads\s24_fp_Veda\s24_fp_Veda\G2\model_c.pkl'
    
    # Load encoder
    with open(path_encoder, 'rb') as f:
        encoder = pickle.load(f)

    # Load model
    with open(path_model, 'rb') as f:
        model = pickle.load(f)

    # Load scaler
    with open(path_scaler, 'rb') as f:
        scaler = pickle.load(f)

    res = []
    for feature in features:
        feature_scaled = scaler.transform([[feature]])
        pred = model.predict(feature_scaled)
        res.append(encoder.inverse_transform(pred)[0])

    return res