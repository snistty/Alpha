def run_formula(dv, param = None):
    import pandas as pd
    from jaqs_fxdayu.data.dataservice import LocalDataService
    dataview_folder = r'../data'
    ds = LocalDataService(fp = dataview_folder)

    defult_param = {'t1':1, 't2':250, 't3':1, 't4':1, 't5':250, 't6':1, 't7':250, 't8':60}
    if not param:
        param = defult_param

    # benchmark_close
    bench_close = ds.index_daily(['000300.SH'],20160101,20180101, 'trade_date,close')[0].set_index('trade_date')
    benchmark = pd.DataFrame(index=dv.get_ts('open').index)
    for label in dv.get_ts('open').columns:
        benchmark[label] = bench_close['close']
    # close
    close = dv.get_ts('close')

    # numerator
    numerator = (pd.rolling_mean(close.pct_change(param['t1']), param['t2'])*250-0.03)
    # denominator
    beta = pd.rolling_cov(arg1=close.pct_change(param['t3']), arg2=benchmark.pct_change(param['t4']), window=param['t5'])/pd.rolling_var(benchmark.pct_change(param['t6']), param['t7'])

    TR60 = pd.rolling_mean(numerator/beta, param['t8'])
    dv.append_df(TR60, 'TR60'),
    return dv.get_ts('TR60')