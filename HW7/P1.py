import HW7.SurvivalModelClasses as Cls
import HW7.CalibrationSettings as CalibSets

# create a cohort
cohort = Cls.Cohort(id=1, pop_size=CalibSets.SIM_POP_SIZE, mortality_prob=0.1)
# simulate teh cohort
outcome = cohort.simulate(CalibSets.TIME_STEPS)
# print outcomes
print('Problem 1: Percentage of patients survived beyond 5 years:', outcome.get_prob_5_year_survival())