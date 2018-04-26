def run_formula(dv, param = None):
    import pandas as pd
    from jaqs_fxdayu.data.dataservice import LocalDataService
    dataview_folder = r'../data'
    ds = LocalDataService(fp = dataview_folder)

    defult_param = {'t1':1,'t2':1,'t3':20,'t4':20, 't5':20, 't6':20, 't7':20}
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
    numerator = pd.rolling_sum((close/close.shift(param['t1'])-1)-pd.rolling_mean((close/close.shift(param['t2'])-1), param['t3'])-(benchmark-pd.rolling_mean(benchmark, param['t4']))**2, param['t5'])
    # denominator
    denominator = pd.rolling_sum((benchmark-pd.rolling_mean(benchmark, param['t6']))**3, param['t7'])

    alpha181 = numerator/denominator
    dv.append_df(alpha181, 'alpha181')

    return dv.get_ts('alpha181')