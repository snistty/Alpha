# #type2  -  only use add_formula function with parameter

def run_formula(dv, param = None):
    defult_param = {'t1':20,'t2':7,'t3':60,'t4':7}
    if not param:
        param = defult_param
    
    alpha180 = dv.add_formula('alpha180',
                         '(If(Ts_Mean(volume, %s)<volume, ((-Ts_Rank(Abs(Delta(close, %s)), %s))*Sign(Delta(close, %s))), -volume))'%(param['t1'], param['t2'], param['t3'], param['t4']),
                         is_quarterly=False, add_data=True)
    
    return alpha180
