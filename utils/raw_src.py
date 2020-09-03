from data_faker import run_data
import datetime
import random
from flask import Flask, jsonify

app = Flask("data_service")

def src_gen(interval):
    '''
    data example:
    [
        {
            "pool": "pool0",
            "column": "col0",
            "value": 903,
            "time": "..."
        },
        {
            "pool": "pool0",
            "column": "col1",
            "value": 903,
            "time": "..."
        },
        {
            "pool": "pool0",
            "column": "col2",
            "value": 903,
            "time": "..."
        },
        {
            "pool": "pool0",
            "column": "col3",
            "value": 903,
            "time": "..."
        }
    ]
    '''

    data_tables = ["INTAKE_inlet_pump", "INTAKE_pump", "INTAKE_ssw_agc",
        "OUTFLOW_pump", "POST_cbr_blower", "POST_densadeg", "POST_dosing_1", "POST_filter",
        "POST_ocr_cbr", "POST_ozonator", "POST_pump", "POST_water_reuse", "PRE_aerobic_1",
        "PRE_aerobic_2", "PRE_anaerobic", "PRE_anoxic_1", "PRE_anoxic_2", "PRE_anoxic_3",
        "PRE_biotank_blower", "PRE_deodor", "PRE_deox", "PRE_dosing_2", "PRE_mbbr", "PRE_pre_anoxic",
        "PRE_sst_sludge_pump", "SLUDGE_aerobic_sludge", "SLUDGE_dehydr", "SLUDGE_storage"]

    fields = ["flow", "pressure_changer", "level", "temp", "do", "ph", "cond", "toc", "bod5", "cod", "ss", "nh3_n", "no3_n", "tn", "tp", "chroma", "turb", "water_content", "mlss", "mlvss", "sv30", "alka", "total_hardness", "vfa", "vss", "resi_chlorine"]

    result = []

    for table in data_tables:
        for field in fields:
            # dictify data
            data = run_data()
            data_dict = {
                "flow": data[1],
                "pressure_changer": data[2],
                "level": data[3],
                "temp": data[4],
                "do": data[5],
                "ph": data[6],
                "cond": data[7],
                "toc": data[8],
                "bod5": data[9],
                "cod": data[10],
                "ss": data[11],
                "nh3_n": data[12],
                "no3_n": data[13],
                "tn": data[14],
                "tp": data[15],
                "chroma": data[16],
                "turb": data[17],
                "water_content": data[18],
                "mlss": data[19],
                "mlvss": data[20],
                "sv30": data[21],
                "alka": data[22],
                "total_hardness": data[23],
                "vfa": data[24],
                "vss": data[25],
                "resi_chlorine": data[26]
            }

            # randomize time
            offset = random.randint(1, interval)
            time = (datetime.datetime.now() + datetime.timedelta(minutes=offset)).strftime("%Y/%m/%d %H:%M:%S")
            
            item = {
                "pool": table,
                "column": field,
                "value": data_dict.get(field),
                "time": time
            }

            result.append(item)

    return jsonify(
        {
            "data": result
        }
    )

@app.route('/')
def data_service():
    return src_gen(1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=15980, debug=True)