import time
import requests

# count = 0
while True:
    time.sleep(10)
    with open('slider.log', 'r') as f:
        lines = f.readlines()
        last_line = lines[-1].split()
        DATA = {"avg_v_effective": last_line[0], "avg_eff_acc": last_line[1], "avg_pwr_rtio": last_line[2]}
        # print(last_line)
        r = requests.post(url="http://localhost:5000/json", json=DATA)
        print(r.text, file=open('write.json'))
