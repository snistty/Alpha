def run_formula(dv, param = None):
    import pandas as pd
    from jaqs_fxdayu.data.dataservice import LocalDataService
    dataview_folder = r'../data'
    ds = LocalDataService(fp = dataview_folder)

    dv.add_field('BearPower', ds)
    dv.add_field('BullPower', ds)

    BB = dv.add_formula('BB',
              'BearPower-BullPower', 
               is_quarterly=False)
    return BB
