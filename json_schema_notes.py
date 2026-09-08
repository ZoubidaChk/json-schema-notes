"""Validate basic JSON data against a JSON-Schema-style document."""
import argparse, json
from dataclasses import dataclass, asdict
@dataclass
class Error: path:str; message:str
def validate(data,schema,path="$"):
    types={"object":dict,"array":list,"string":str,"number":(int,float),"integer":int,"boolean":bool}; out=[]; typ=schema.get("type")
    if typ in types and (not isinstance(data,types[typ]) or (typ in ("number","integer") and isinstance(data,bool))): return [Error(path,f"expected {typ}")]
    if isinstance(data,dict):
        out += [Error(f"{path}.{k}","is required") for k in schema.get("required",[]) if k not in data]
        for k,s in schema.get("properties",{}).items():
            if k in data: out += validate(data[k],s,f"{path}.{k}")
    if isinstance(data,str) and len(data)<schema.get("minLength",0): out.append(Error(path,"is too short"))
    return out
def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("data"); p.add_argument("schema"); a=p.parse_args()
    with open(a.data,encoding="utf-8") as f: data=json.load(f)
    with open(a.schema,encoding="utf-8") as f: schema=json.load(f)
    errors=[asdict(e) for e in validate(data,schema)]; print(json.dumps({"valid":not errors,"errors":errors},indent=2)); return 0 if not errors else 1
if __name__=="__main__": raise SystemExit(main())
