"""
Autocorrelation, also known as serial correlation, is the correlation of a signal with itself at different points in time. Informally, it is the similarity between observations as a function of the time lag between them.
"""

pd.Series(acf(air_passengers.Passengers, nlags = 36)).plot()
