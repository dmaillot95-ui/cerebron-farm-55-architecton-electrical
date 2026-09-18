import json,math,pathlib
V=12.0; R1=100.0; R2=200.0; Rt=R1+R2; I=V/Rt; Psource=V*I; Pres=I*I*Rt; residual=Psource-Pres
passed=math.isclose(I,0.04,rel_tol=1e-12) and math.isclose(residual,0.0,abs_tol=1e-12)
out={"benchmark":"dc_series_power_balance","engine":"PY-ELECTRICAL-MVP","voltage_v":V,"current_a":I,"power_source_w":Psource,"power_resistors_w":Pres,"power_residual_w":residual,"passed":passed,"evidence_level":"E2","limitations":["closed-form DC benchmark","not SPICE","not hardware test"]}
pathlib.Path("artifacts").mkdir(exist_ok=True); pathlib.Path("artifacts/electrical_mvp.json").write_text(json.dumps(out,indent=2),encoding="utf-8"); print(json.dumps(out,indent=2)); raise SystemExit(0 if passed else 1)
