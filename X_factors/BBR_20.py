def run_formula(dv, param = None):
    import pandas as pd
    from jaqs_fxdayu.data.dataservice import LocalDataService
    dataview_folder = r'../data'
    ds = LocalDataService(fp = dataview_folder)

    defult_param = {'t':20}
    if not param:
        param = defult_param

    dv.add_field('BearPower', ds)
    dv.add_field('BullPower', ds)

    BBR_20 = dv.add_formula('BBR_20',
              'Correlation(BearPower, BullPower, %s)'%(param['t']),
              is_quarterly=False)
    return BBR_20
