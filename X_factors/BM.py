#------------------------------------------------------------------------------    
#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv):
    import pandas as pd
    from jaqs_fxdayu.data.dataservice import LocalDataService
    dataview_folder = r'../data'
    ds = LocalDataService(fp = dataview_folder)

    dv.add_field('tot_assets', ds)
    dv.add_field('total_liab', ds)
    dv.add_field('total_mv', ds)

    BM = dv.add_formula('BM',
        '(tot_assets-total_liab)/total_mv',
              is_quarterly=False)
    return BM  
