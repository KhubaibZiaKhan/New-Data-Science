import scipy.stats as stats

prob = 1 - stats.binom.cdf(6, 10, 0.5)

print("The Probabilty of getting more then 6 head in 10 coin flips is :", prob)