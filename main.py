fields = ["flow", "pressure_changer", "level", "temp", "do", "ph", "cond", "toc", "bod5", "cod", "ss", "nh3_n", "no3_n", "tn", "tp", "chroma", "turb", "water_content", "mlss", "mlvss", "sv30", "alka", "total_hardness", "vfa", "vss", "resi_chlorine"]

recom = []

for i in fields:
    recom.append("M_720_" + i)

print(recom)