#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':60}
    if not param:
        param = defult_param
        
    AR_60 = dv.add_formula('AR_60',
              'Ts_Sum(high-open, %s)/Ts_Sum(open-low, %s)'%(param['t'], param['t']),
              is_quarterly=False)
    return AR_60
