import yaml
import sys
print(sys.path.append(('..')))
from pythoncode.calc import Calculator
import pytest


calc=Calculator()
with open("../data/calc.yml") as f:
    datas=yaml.safe_load(f)
    myids=datas.keys()
    mydatas = datas.values()

def get_steps():
    with open("../steps/add_step.yaml") as f:
        steps = yaml.safe_load(f)
    return steps

def step(a,b,result):
    steps=get_steps()
    for step in steps:
        if step == 'add':
            assert result == calc.add(a, b)
        elif step == 'add1':
            assert result == calc.add1(a, b)
        elif step == 'add2':
            assert result == calc.add2(a, b)




class Testcalc:
    @pytest.mark.parametrize('a,b,result',mydatas,ids=myids)
    def test_calc_add(self,a,b,result):
        step(a,b,result)

