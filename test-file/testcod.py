import yaml

with open('../data/calc.yml') as f:
    mydatas =  yaml.safe_load(f)
    print(mydatas)
    print(type(mydatas))
    mydatas1 = mydatas.values()