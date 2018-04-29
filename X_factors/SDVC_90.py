#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t1':1, 't2':90}
    if not param:
        param = defult_param

    SDVC_90 = dv.add_formula('SDVC_90', 
        'StdDev(Delay(volume/close, %s)/(volume/close), %s)'%(param['t1'], param['t2']),
        is_quarterly=False)
    return SDVC_90
