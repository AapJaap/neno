import sys, re, time, os
counts={}
last=0
def dehex(s):
    if re.fullmatch(r"[0-9A-Fa-f]+", s) and len(s)%2==0:
        try: return bytes.fromhex(s).decode('utf-8','replace')
        except: return s
    return s

for line in sys.stdin:
    parts=line.rstrip("\n").split("\t")
    if len(parts)<2: continue
    ssid=dehex(parts[1]).strip("\x00") or "<hidden>"
    counts[ssid]=counts.get(ssid,0)+1
    if time.time()-last>1:   # refresh elke seconde
        os.system("clear")
        print("SSID (gegroepeerd)  —  total probe req/resp gezien")
        for k,v in sorted(counts.items(), key=lambda kv:(-kv[1], kv[0]))[:40]:
            print(f"{v:6}  {k}")
        last=time.time()
