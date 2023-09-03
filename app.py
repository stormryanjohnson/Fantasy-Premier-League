import pickle
from flask import Flask,request,app, jsonify, render_template
import pandas as pd
from pathlib import Path
from modelling.helper import *

__version__ = 'v0.0.1'
BASE_DIR = Path(__file__).resolve(strict=True).parent
columns = ['minutes', 'goals_scored', 'assists', 'previous_start_value', 
           'delta_value', 'bps', 'selected_by_percent',
            'position_DEF', 'position_FWD', 'position_GK',
            'position_MID', 'teams_chelsea',
            'teams_liverpool', 'teams_manchestercity', 'teams_manchesterunited',
            'teams_newcastleunited', 'teams_tottenhamhotspur']

app = Flask(__name__)

# load the model
model = pickle.load(open(f'{BASE_DIR}/models/rf_{__version__}.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict_api():

    # process input to correct format for prediction
    data_dict = request.json
    teams_key = f'teams_{data_dict["team"]}'
    position_key = f'position_{data_dict["position"]}'
    data_dict[teams_key] = 1
    data_dict[position_key] = 1
    data_dict['previous_end_value'] = float(data_dict['previous_end_value'])*10
    data_dict['previous_start_value'] = float(data_dict['previous_start_value'])*10
    data_dict['delta_value'] = data_dict['previous_end_value'] - data_dict['previous_start_value']
    data_dict.pop("team")
    data_dict.pop("position")
    data_dict.pop("previous_end_value")
    data_df = pd.DataFrame(columns=columns)
    for key in data_dict:
        data_df[key] = [data_dict[key]]
    data_df = data_df.fillna(0)
    data_df = data_df[columns]
    print(data_df.columns)
    
    # perform prediction and round to nearest 5 (consistent with real-world FPL pricing)
    prediction = round(model.predict(data_df)[0]/10, 3)  #round_to_nearest_5(model.predict(data_df)[0])/10
    
    return jsonify(prediction)


if __name__ == "__main__":
    app.run(debug=True)
   