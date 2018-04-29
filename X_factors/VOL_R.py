def run_formula(dv, param = None):
    import pandas as pd
    from jaqs_fxdayu.data.dataservice import LocalDataService
    dataview_folder = r'../data'
    ds = LocalDataService(fp = dataview_folder)

    dv.add_field('VOL10', ds)
    dv.add_field('VOL20', ds)
    dv.add_field('VOL120', ds)
    dv.add_field('VOL240', ds)

    VOL_R = dv.add_formula('VOL_R',
              '(VOL10/VOL120)*(VOL20/VOL120)', 
               is_quarterly=False)
    return VOL_R
