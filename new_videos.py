import os
all_existing = []
with open("accident_times.txt", "r") as f:
    for line in f.readlines():
        try:
            vid, duration = line.strip().split(" ")
            all_existing.append(vid)
        except:
            continue
total = 0
for candidate in os.listdir("/home/dd/arcelormittalvideos/"):
    if not "mp4" in candidate: continue
    cn = candidate.replace("accident","")
    if cn not in all_existing:
        print("http://youtube.com/watch?v={}".format(cn.split(".mp4")[0]), cn)
        total = total + 1
    if total >= 10: break
