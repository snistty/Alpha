#type1  -  simplest type,only use add_formula function without parameter

def run_formula(dv, param = None):
	# NP
	dv.add_field('net_profit')
	# TOR
	dv.add_field('total_oper_rev')
	NPToTOR_j = dv.add_formula('NPToTOR_j',
	                           'net_profit/total_oper_rev', is_quarterly=True)
	return NPToTOR_j