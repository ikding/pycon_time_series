air_passengers.rolling(window = 20).apply(lambda x: acf(x, nlags = 10)[10]).plot()
