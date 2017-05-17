lagged = f.shift(1)
sum((f - lagged)['Open'] > 0)
f['DayGain'] = f['Open'] - lagged['Open']
sum(f['DayGain'] > 0)/len(f['DayGain'])