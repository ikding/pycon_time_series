# 1
# method = 'None'
# do this perhaps to join to other temporal data

# 2
# asfreq is more rigid

# 3
converted.asfreq('10Min', method = None).fillna(method = 'ffill', limit =3)

# 4
# It's basically like a groupby operation
