t1 = pd.to_datetime('2016-06-18 12:15pm', dayfirst = True).strftime(format = '%Y/%M/%D')

t2 = pd.Timestamp('2016-06-18 12:15pm').strftime(format = '%Y/%M/%D')