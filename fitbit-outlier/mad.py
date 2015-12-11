import numpy as np
data = np.array([83,72,74,79,96,60,82,92,50,86,94,86,73,74,85,86,77,68,95,75,95],dtype=float)
median = np.median(data, axis=0)
diff = np.sum((data - median)**2, axis=-1)
diff = np.sqrt(diff)
med_abs_deviation = np.median(diff)
modified_z_score = 0.6745 * diff / med_abs_deviation
data_without_outliers = data[modified_z_score < 3.5]

print data_without_outliers