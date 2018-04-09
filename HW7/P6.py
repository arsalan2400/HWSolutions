import HW7.CalibrationSettings as CalibSets
import HW7.CalibrationClasses as CalibCls

CalibSets.OBS_N = 1146
CalibSets.OBS_5YEAR_ALIVE = 800

# create a calibration object
calibration = CalibCls.Calibration()

# sample the posterior of the mortality probability
calibration.sample_posterior()

# estimate of annal mortality probability and the 95% credible interval
print('Estimate of annual mortality probability ({:.{prec}%} credible interval):'.format(1-CalibSets.ALPHA, prec=0),
      calibration.get_mortality_estimate_credible_interval(CalibSets.ALPHA, 4))  # return with 4 decimals

# initialize and simulate a calibrated model
calibrated_model = CalibCls.CalibratedModel('CalibrationResults.csv')
calibrated_model.simulate(CalibSets.NUM_SIM_COHORTS, CalibSets.SIM_POP_SIZE, CalibSets.TIME_STEPS)

# report mean and PI
print('P5: Mean survival time and {:.{prec}%} projection interval:'.format(1 - CalibSets.ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(CalibSets.ALPHA, deci=2))