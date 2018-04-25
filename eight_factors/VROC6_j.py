#type2  -  only use add_formula function with parameter
def run_formula(dv, param=None):
    default_param = {'t':6}
    if not param:
        param = default_param

    VROC6_j = dv.add_formula('VROC6_j',
                          '((volume/Delay(volume, %s))-1)*100'%param['t'],
                           is_quarterly=False)
    return VROC6_j