#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv, param = None):
    # TS
    dv.add_field('capital_stk')
    # TSEP
    dv.add_field('tot_compreh_inc_parent_comp')

    NetAssetPS = dv.add_formula('NetAssetPS',
                               'tot_compreh_inc_parent_comp/capital_stk',is_quarterly=False)
    return NetAssetPS