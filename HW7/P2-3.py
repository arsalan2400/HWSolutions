import scipy.stats as stat


# problem 2
print('P2: If the probability of 5-year survival is q,'
      'the number of patients that survived beyond 5 years in a cohort of 𝑁 participants',
      'follows a binomial distribution ',
      'with q being the probability of success and N being the number of trials.')
print('')

# Problem 3
weight = stat.binom.pmf(k=400, n=573, p=0.5, loc=0)
print('P3: The likelihood of the observed data:', weight)
