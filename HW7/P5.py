import HW7.CalibrationSettings as CalibSets
import HW7.CalibrationClasses as CalibCls

# initialize and simulate a calibrated model
calibrated_model = CalibCls.CalibratedModel('CalibrationResults.csv')
calibrated_model.simulate(CalibSets.NUM_SIM_COHORTS, CalibSets.SIM_POP_SIZE, CalibSets.TIME_STEPS)

# report mean and PI
print('P5: Mean survival time and {:.{prec}%} projection interval:'.format(1 - CalibSets.ALPHA, prec=0),
      calibrated_model.get_mean_survival_time_proj_interval(CalibSets.ALPHA, deci=2))
