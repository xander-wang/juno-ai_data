from data_faker import run_data
import datetime
import random
from flask import Flask, jsonify
import pprint
import threading
import time

app = Flask("data_service")

result = []

threadLock = threading.Lock()

def fake_data():
    # load fake data
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
    return data_dict

def fill_data(table, column, value, time):
    item = {
        "pool": table,
        "column": column,
        "value": value,
        "time": time
    }
    return item

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

    # don't delete:
    # data_tables = ["INTAKE_inlet_pump", "INTAKE_pump", "INTAKE_ssw_agc",
    #     "OUTFLOW_pump", "POST_cbr_blower", "POST_densadeg", "POST_dosing_1", "POST_filter",
    #     "POST_ocr_cbr", "POST_ozonator", "POST_pump", "POST_water_reuse", "PRE_aerobic_1",
    #     "PRE_aerobic_2", "PRE_anaerobic", "PRE_anoxic_1", "PRE_anoxic_2", "PRE_anoxic_3",
    #     "PRE_biotank_blower", "PRE_deodor", "PRE_deox", "PRE_dosing_2", "PRE_mbbr", "PRE_pre_anoxic",
    #     "PRE_sst_sludge_pump", "SLUDGE_aerobic_sludge", "SLUDGE_dehydr", "SLUDGE_storage"]

    # fields = ["flow", "pressure_changer", "level", "temp", "do", "ph", "cond", "toc", "bod5", "cod", "ss", "nh3_n", "no3_n", "tn", "tp", "chroma", "turb", "water_content", "mlss", "mlvss", "sv30", "alka", "total_hardness", "vfa", "vss", "resi_chlorine"]

    table_fields = {
        "INTAKE_inlet_pump": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "120": ['M_120__flow', 'M_120__pressure_changer', 'M_120__level', 'M_120__temp', 'M_120__do', 'M_120__ph', 'M_120__cond', 'M_120__toc', 'M_120__bod5', 'M_120__cod', 'M_120__ss', 'M_120__nh3_n', 'M_120__no3_n', 'M_120__tn', 'M_120__tp', 'M_120__chroma', 'M_120__turb', 'M_120__water_content', 'M_120__mlss', 'M_120__mlvss', 'M_120__sv30', 'M_120__alka', 'M_120__total_hardness', 'M_120__vfa', 'M_120__vss', 'M_120__resi_chlorine']
        },
        "INTAKE_ssw_agc": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "120": ['M_120__flow', 'M_120__pressure_changer', 'M_120__level', 'M_120__temp', 'M_120__do', 'M_120__ph', 'M_120__cond', 'M_120__toc', 'M_120__bod5', 'M_120__cod', 'M_120__ss', 'M_120__nh3_n', 'M_120__no3_n', 'M_120__tn', 'M_120__tp', 'M_120__chroma', 'M_120__turb', 'M_120__water_content', 'M_120__mlss', 'M_120__mlvss', 'M_120__sv30', 'M_120__alka', 'M_120__total_hardness', 'M_120__vfa', 'M_120__vss', 'M_120__resi_chlorine'],
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "INTAKE_pump": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "PRE_pre_anoxic": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine']
        },
        "PRE_anaerobic": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "PRE_anoxic_1": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "PRE_anoxic_2": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "PRE_anoxic_3": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "PRE_aerobic_1": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "PRE_aerobic_2": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "PRE_deox": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine']
        },
        "PRE_dosing_2": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine']             
        },
        "PRE_biotank_blower": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine']
        },
        "PRE_deodor": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine']
        },
        "PRE_sst_sludge_pump": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "POST_pump": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "120": ['M_120__flow', 'M_120__pressure_changer', 'M_120__level', 'M_120__temp', 'M_120__do', 'M_120__ph', 'M_120__cond', 'M_120__toc', 'M_120__bod5', 'M_120__cod', 'M_120__ss', 'M_120__nh3_n', 'M_120__no3_n', 'M_120__tn', 'M_120__tp', 'M_120__chroma', 'M_120__turb', 'M_120__water_content', 'M_120__mlss', 'M_120__mlvss', 'M_120__sv30', 'M_120__alka', 'M_120__total_hardness', 'M_120__vfa', 'M_120__vss', 'M_120__resi_chlorine'],
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']            
        },
        "POST_densadeg": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "120": ['M_120__flow', 'M_120__pressure_changer', 'M_120__level', 'M_120__temp', 'M_120__do', 'M_120__ph', 'M_120__cond', 'M_120__toc', 'M_120__bod5', 'M_120__cod', 'M_120__ss', 'M_120__nh3_n', 'M_120__no3_n', 'M_120__tn', 'M_120__tp', 'M_120__chroma', 'M_120__turb', 'M_120__water_content', 'M_120__mlss', 'M_120__mlvss', 'M_120__sv30', 'M_120__alka', 'M_120__total_hardness', 'M_120__vfa', 'M_120__vss', 'M_120__resi_chlorine'],
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "POST_ozonator": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine']
        },
        "POST_ocr_cbr": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "120": ['M_120__flow', 'M_120__pressure_changer', 'M_120__level', 'M_120__temp', 'M_120__do', 'M_120__ph', 'M_120__cond', 'M_120__toc', 'M_120__bod5', 'M_120__cod', 'M_120__ss', 'M_120__nh3_n', 'M_120__no3_n', 'M_120__tn', 'M_120__tp', 'M_120__chroma', 'M_120__turb', 'M_120__water_content', 'M_120__mlss', 'M_120__mlvss', 'M_120__sv30', 'M_120__alka', 'M_120__total_hardness', 'M_120__vfa', 'M_120__vss', 'M_120__resi_chlorine'],
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "POST_filter": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "POST_cbr_blower": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine']
        },
        "POST_dosing_1": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine']
        },
        "POST_water_reuse": {
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "OUTFLOW_pump": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine'],
            "120": ['M_120__flow', 'M_120__pressure_changer', 'M_120__level', 'M_120__temp', 'M_120__do', 'M_120__ph', 'M_120__cond', 'M_120__toc', 'M_120__bod5', 'M_120__cod', 'M_120__ss', 'M_120__nh3_n', 'M_120__no3_n', 'M_120__tn', 'M_120__tp', 'M_120__chroma', 'M_120__turb', 'M_120__water_content', 'M_120__mlss', 'M_120__mlvss', 'M_120__sv30', 'M_120__alka', 'M_120__total_hardness', 'M_120__vfa', 'M_120__vss', 'M_120__resi_chlorine'],
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "SLUDGE_storage": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine']
        },
        "SLUDGE_dehyd": {
            "720": ['M_720__flow', 'M_720__pressure_changer', 'M_720__level', 'M_720__temp', 'M_720__do', 'M_720__ph', 'M_720__cond', 'M_720__toc', 'M_720__bod5', 'M_720__cod', 'M_720__ss', 'M_720__nh3_n', 'M_720__no3_n', 'M_720__tn', 'M_720__tp', 'M_720__chroma', 'M_720__turb', 'M_720__water_content', 'M_720__mlss', 'M_720__mlvss', 'M_720__sv30', 'M_720__alka', 'M_720__total_hardness', 'M_720__vfa', 'M_720__vss', 'M_720__resi_chlorine']
        },
        "SLUDGE_aerobic_sludge": {
            "5": ['M_5__flow', 'M_5__pressure_changer', 'M_5__level', 'M_5__temp', 'M_5__do', 'M_5__ph', 'M_5__cond', 'M_5__toc', 'M_5__bod5', 'M_5__cod', 'M_5__ss', 'M_5__nh3_n', 'M_5__no3_n', 'M_5__tn', 'M_5__tp', 'M_5__chroma', 'M_5__turb', 'M_5__water_content', 'M_5__mlss', 'M_5__mlvss', 'M_5__sv30', 'M_5__alka', 'M_5__total_hardness', 'M_5__vfa', 'M_5__vss', 'M_5__resi_chlorine']
        }
    }

    time_now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    res = []
    for table in table_fields:
        for interval_column in table_fields[table]:
            if interval_column == str(interval):
                for column in table_fields[table][interval_column]:
                    column_name = column.split("__")[1]
                    res.append(fill_data(table, column, fake_data().get(column_name), time_now))
    threadLock.acquire()
    result = res
    threadLock.release()

def loop_5():
    while(True):
        src_gen(5)
        time.sleep(5)
        

# def loop_120():
#     return src_gen(120)

# def loop_720():
#     return src_gen(720)

def main():
    while(True):
        time.sleep(6)
        pprint.pprint(result)


t0 = threading.Thread(target=main)
t1 = threading.Thread(target=loop_5)
threads = [t0, t1]

if __name__ == "__main__":
    t0.start()
    t1.start()
    


# @app.route('/')
# def data_service():
#     return src_gen(1)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=15980, debug=True)

