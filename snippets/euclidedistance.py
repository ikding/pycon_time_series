def EuclidDistance(s1, s2):
    sum_squares = 0
    for i in range(len(s1)):
        sum_squares = sum_squares + (s1[i] - s2[i])**2
    return sqrt(sum_squares)