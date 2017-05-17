df['A'].plot(color = 'gray')
df.rolling(window = 10, center = False)['A'].apply(lambda x: x[1]/x[2]).plot(color = 'red')
