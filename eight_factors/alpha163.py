#type2  -  only use add_formula function with parameter

def run_formula(dv, param = None):
    defult_param = {'t1':1,'t2':20}
    if not param:
        param = defult_param

    alpha163 = dv.add_formula('alpha163',
                         'Rank(((((-Return(close,%s))*Ts_Mean(volume, %s))*vwap)*(high - close)))'%(param['t1'],param['t2']),
                         is_quarterly=False)
    return alpha163