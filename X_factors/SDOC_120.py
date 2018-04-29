#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':120}
    if not param:
        param = defult_param

    SDOC_120 = dv.add_formula('SDOC_120',
        'StdDev((Delay((open*close)^0.5, %s)/((open*close)^0.5)), %s)'%(param['t'], param['t'])
        ,is_quarterly=False)
    return SDOC_120

# def run_formula(dv, param = None):
#     defult_param = {'t':120}
#     if not param:
#         param = defult_param
        
#     SDOC_120 = dv.add_formula('SDOC_120',
#         'Delay(volume/close, %s)/(volume/close)'%(param['t']),
#         is_quarterly=False)
#     return VC_60
