def run_formula(dv, param = None):
    import pandas as pd
    from jaqs_fxdayu.data.dataservice import LocalDataService
    dataview_folder = r'../data'
    ds = LocalDataService(fp = dataview_folder)

    dv.add_field('VOL10', ds)
    dv.add_field('VOL20', ds)
    dv.add_field('VOL120', ds)
    dv.add_field('VOL240', ds)

    VOL_T = dv.add_formula('VOL_T',
              '(VOL10*VOL20*VOL240*VOL120)^(1/4)',
               is_quarterly=False)
    return VOL_T
