#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':60}
    if not param:
        param = defult_param
        
    VDC_60 = dv.add_formula('VDC_60',
           '(volume/Delay(close, %s))/(volume/close)'%(param['t']),
          is_quarterly=False)
    return VDC_60