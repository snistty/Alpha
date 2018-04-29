#------------------------------------------------------------------------------    
#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv):
    HLV = dv.add_formula('HLV', 
        '((high*low*vwap)^(1/3) * volume)',
            is_quarterly=False)

# IC=-0.03， IR=-0.27
    return HLV 
