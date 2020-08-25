import csv
import time
import random
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

# DB
db = mysql.connector.connect(
    host="192.168.211.197",
    user="root",
    passwd="12345678",
    auth_plugin="mysql_native_password",
    database="juno"
)

#骰子算法
''' 
local:  平均值
scal:   正态分布宽度
size:   数据切片个数 默认为1
low:    最小值      默认为0
high:   最大值
number: 当size =1 时，number不可调整数值，当size>1时，number可设置为（0~ size-1）
'''
def Dice_algorithm(local,scal,high,low =0, size = 1,number = 0):
    random_number = random.random()
    #print("random_number"+str(random_number))
    normal_number = np.clip(np.random.normal(local,scal,size)[number], low, high)
    #print("normal_number"+str(normal_number))
    uniform_number = np.random.uniform(low,high,size)[number]
    #print("uniform_number"+str(uniform_number))
    Dice_algorithm_data = random_number*normal_number+(1-random_number)*uniform_number

    return round(Dice_algorithm_data,4)

excel_sheet_list = [
    [
        [4167,2000,6000],[1,1,2],[3,2,4],[25,5,32],[2.5,3,5],[7,1,8,6],[3200,50,3300,3200],[24,2,60],[0,0,0],[240,100,1000],
        [16,10,30],[0.4,2,5],[0,0,0],[8.5,5,15],[0.3,0.5,2],[8,2,30],[3,2,5],[98,1,99.9],[0,0,0],[0,0,0],[0,0,0],[0,0,0],
        [0,0,0],[0,0,0],[0,0,0],[0,0,0]
    ],

    [
        [4167, 2000, 6000], [1, 1, 2], [3, 2, 4], [25, 5, 32], [2.5, 3, 5], [7, 1, 8, 6], [3200, 50, 3300, 3200],
        [24, 2, 60], [0, 0, 0], [240, 100, 1000],[16, 10, 30], [0.4, 2, 5], [0, 0, 0], [8.5, 5, 15], [0.3, 0.5, 2],
        [8, 2, 30], [3, 2, 5], [98, 1, 99.9],[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],[0, 0, 0], [0, 0, 0],
        [0, 0, 0], [0, 0, 0]
    ]
]

def run_data():
    
    time_data = time.strftime("%Y/%m/%d %H:%M:%S",time.localtime())
    # 流量
    Q_data = Dice_algorithm(local= 4167,scal=2000,high=6000)

    # 压力变送
    pressure_data = Dice_algorithm(local= 1,scal=1,high=2)

    # 液位
    liquid_level = Dice_algorithm(local= 3,scal=2,high=4)

    # 温度
    temperature_data = Dice_algorithm(local= 25,scal=5,high=32)

    # DO
    DO_data = Dice_algorithm(local= 2.5,scal=3,high=5)

    # pH
    pH_data = Dice_algorithm(local=7,scal=1,high=8,low=6)

    # Cond
    Cond_data = Dice_algorithm(local= 3200,scal=50,high=3300,low = 3200)

    # TOC
    TOC_data = Dice_algorithm(local= 24,scal=2,high=60)

    # BOD5
    # 该指标目前处于未激活状态
    # 设置改值为负值，用于算法数据清洗
    BOD5 = -1024

    # COD
    COD_data = Dice_algorithm(local= 240,scal=100,high=1000)

    # print('----------------------------------------------------------')
    # COD_data = Dice_algorithm(240,100,1000)
    # print('COD_data',str(COD_data))
    # print('----------------------------------------------------------')

    # SS
    SS_data = Dice_algorithm(local= 16,scal=10,high=30)

    # NH3-N
    NH3_N_data = Dice_algorithm(local= 0.4,scal=2,high=5)

    #NO3-N
    NO3_N_data = -1024

    # TN
    TN_data = Dice_algorithm(local= 8.5,scal=5,high=15)

    # TP
    TP_data = Dice_algorithm(local= 0.3,scal=0.5,high=2)

    # 色度
    chroma_data = Dice_algorithm(local= 8,scal=2,high=30)

    # 浊度
    muddy_data = Dice_algorithm(local= 3,scal=2,high=5)

    # 含水率
    moisture_content_data = Dice_algorithm(local= 98,scal=1,high=99.9)

    # MLSS
    MLSS_data = -1024

    # MLVSS
    MLVSS_data = -1024

    # SV30
    SV30_data = -1024

    # 碱度
    basicity_data = -1024

    # 总硬度
    Total_hardness_data = -1024

    # VFA
    VFA_data = -1024

    # VSS
    VSS_data = -1024

    # 余氯
    residual_chlorine_data = -1024
    excel_key_list = [time_data, Q_data, pressure_data, liquid_level, temperature_data, DO_data, pH_data, Cond_data,
                      TOC_data, BOD5,
                      COD_data, SS_data, NH3_N_data, NO3_N_data, TN_data, TP_data, chroma_data, muddy_data,
                      moisture_content_data,
                      MLSS_data, MLVSS_data, SV30_data, basicity_data, Total_hardness_data, VFA_data, VSS_data,
                      residual_chlorine_data]

    return excel_key_list

def writer(second):
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
        
writer(5)