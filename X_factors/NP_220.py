#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':220}
    if not param:
        param = defult_param
        
    NP_220 = dv.add_formula("NP_220",
        '(net_profit-Delay(net_profit, %s))/Delay(net_profit, %s)'%(param['t'], param['t']),
           is_quarterly=False)
    return NP_220
