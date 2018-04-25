#type2  -  only use add_formula function with parameter

def run_formula(dv, param = None):
    defult_param = {'t1':1,'t2':1,'t3':1,'t4':1, 't5':12,'t6':1,'t7':1,'t8':1,'t9':1,'t10':12,'t11':1,'t12':1,'t13':1,'t14':1,'t15':12}
    if not param:
        param = defult_param

    alpha51 = dv.add_formula('alpha51', 
                         '''Ts_Sum(If((high+low)<=(Delay(high, %s)+Delay(low, %s)),0, Max(Abs(high-Delay(high,%s)),Abs(low-Delay(low,%s)))), %s)/(Ts_Sum(If((high+low)<=(Delay(high,%s)+Delay(low,%s)),0,Max(Abs(high-Delay(high,%s)),Abs(low-Delay(low,%s)))),%s)+Ts_Sum(If((high+low)>=(Delay(high,%s)+Delay(low,%s)),0,Max(Abs(high-Delay(high,%s)),Abs(low-Delay(low,%s)))),%s))'''%(param['t1'],param['t2'],param['t3'],param['t4'],param['t5'],param['t6'],param['t7'],param['t8'],param['t9'],param['t10'],param['t11'],param['t12'],param['t13'],param['t14'],param['t15']),
                         is_quarterly=False, add_data=True)
    return alpha51