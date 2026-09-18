import subprocess,sys,json,pathlib
r=subprocess.run([sys.executable,"worker/electrical_mvp.py"],check=False); assert r.returncode==0
x=json.loads(pathlib.Path("artifacts/electrical_mvp.json").read_text()); assert x["passed"] is True
