# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  
# path        [File location variable]
data =pd.read_csv(path)
#Code starts here
data_sample = data.sample(n=sample_size, random_state=0)
sample_mean = data_sample['installment'].mean()
sample_std = data_sample['installment'].std()

#find margin of error
margin_of_error = z_critical * (sample_std/math.sqrt(sample_size))
print('Margin of error is: ',margin_of_error)

#find the confidence interval
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
print(confidence_interval)

true_mean=data['installment'].mean()
print('True mean is {}', format(true_mean))




# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig, axes = plt.subplots(3, 1, figsize=(10, 20))

#Running loop to iterate throuh rows
for i in range(len(sample_size)):

    m=[]
    #loop to implement the number of samples
    for j in range(1000):
        #finding mean of random sample
        mean = data['installment'].sample(sample_size[i]).mean()
        m.append(mean)
    
    #convert 'm' into a series called 'mean_series'
    mean_series = pd.Series(m)

    #plot the corresponding histogram for mean_series
    axes[i].hist(mean_series, normed=True)

plt.show()



# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here

#Remove last character of string from int.rate column
data['int.rate'] = data['int.rate'].map(lambda x: str(x)[:-1])

#Dividing column values by 100
data['int.rate'] = data['int.rate'].astype(float)/100

#Aply z test for the hypothesis
z_statistic, p_value = ztest(x1=data[data['purpose']=='small_business']['int.rate'], value= data['int.rate'].mean(), alternative='larger')

print(z_statistic)
print(p_value)

if(p_value < 0.05):
    print('Reject null hypothesis')
else:
    print('Accept null hypothesis')




# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic, p_value = ztest(x1= data[data['paid.back.loan']=='No']['installment'],
x2 = data[data['paid.back.loan']=='Yes']['installment'] )

print(z_statistic)
print(p_value)

if(p_value < 0.05):
    print('We can Reject null hypothesis')
else:
    print('We cant reject hypothesis')


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data[data['paid.back.loan'] == 'Yes']['purpose'].value_counts()
no = data[data['paid.back.loan'] == 'No']['purpose'].value_counts()

observed = pd.concat([yes.transpose(), no.transpose()], 1, keys= ['Yes','No'])
print(observed)

#Apply "chi2_contingency()" on 'observed'
chi2, p, dof, ex = chi2_contingency(observed)

print(chi2)
print(critical_value)

if(chi2 > critical_value):
    print("Reject null hypothesis")
else:
    print("Null hypothesis can not be rejected")




