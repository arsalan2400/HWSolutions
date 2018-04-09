import HW7.CalibrationSettings as CalibSets
import HW7.CalibrationClasses as CalibCls

# create a calibration object
calibration = CalibCls.Calibration()

# sample the posterior of the mortality probability
calibration.sample_posterior()

# estimate of annal mortality probability and the 95% credible interval
print('Estimate of annual mortality probability ({:.{prec}%} credible interval):'.format(1-CalibSets.ALPHA, prec=0),
      calibration.get_mortality_estimate_credible_interval(CalibSets.ALPHA, 4))  # return with 4 decimals
