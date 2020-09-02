import mysql.connector
from data_faker import run_data

# DB
db = mysql.connector.connect(
    host="192.168.211.197",
    user="root",
    passwd="12345678",
    auth_plugin="mysql_native_password",
    database="juno"
)

def raw_sql_writer(second):
    tables = ["INTAKE_inlet_pump", "INTAKE_pump", "INTAKE_ssw_agc",
    "OUTFLOW_pump", "POST_cbr_blower", "POST_densadeg", "POST_dosing_1", "POST_filter",
    "POST_ocr_cbr", "POST_ozonator", "POST_pump", "POST_water_reuse", "PRE_aerobic_1",
    "PRE_aerobic_2", "PRE_anaerobic", "PRE_anoxic_1", "PRE_anoxic_2", "PRE_anoxic_3",
    "PRE_biotank_blower", "PRE_deodor", "PRE_deox", "PRE_dosing_2", "PRE_mbbr", "PRE_pre_anoxic",
    "PRE_sst_sludge_pump", "SLUDGE_aerobic_sludge", "SLUDGE_dehydr", "SLUDGE_storage", "BUSINESS_removal_rate", 
    "BUSINESS_water_consumption"]

    fields = "(time, flow, pressure_changer, level, temp, do, ph, cond, toc, bod5, cod, ss, nh3_n, no3_n, tn, tp, chroma, turb, water_content, mlss, mlvss, sv30, alka, total_hardness, vfa, vss, resi_chlorine)"
    
    cursor = db.cursor()

    while(True):
        for item in tables:
            row = run_data()
            sql = "INSERT INTO " + item + " " + fields + " VALUES " + str(tuple(row)) 
            cursor.execute(sql)
            db.commit()
        print("Loop completed, resume in " + str(second) + " second(s).")
        time.sleep(second)