# --------------
# Importing header files
import numpy as np
import warnings
warnings.filterwarnings('ignore')
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#step 1
census = np.concatenate((new_record,data),axis=0)
print(census)
data_shape = data.reshape(1000,8)
data_census = census.reshape(1001,8)
#print(data_shape)
#print(data_census)
#Code starts here
#STEP 2
age = np.array(census[:,0])
print(age)
max_age = np.max(age)
min_age = np.min(age)
print(max_age)
print(min_age)
age_min = np.mean(age)
print(age_min)
age_std = np.std(age)
print(age_std)
#step 3
# Generic method for extracting rows of given raceId
def extractRace(raceId):
    return census[:,2]==raceId

# Extract different races
race_0 = census[extractRace(0), :]
race_1 = census[extractRace(1), :]
race_2 = census[extractRace(2), :]
race_3 = census[extractRace(3), :]
race_4 = census[extractRace(4), :]

# length of each nd-array created
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
races = np.array([len_0, len_1 ,len_2, len_3, len_4])

# finding the smallest array
minority_race_number = np.min(races)

# Fetching the index of the array with the smallest length
minority_race = list(races).index(minority_race_number)
print(minority_race)

#step 4
# Applying boolean filter for all values in age column at index 0 and
# extracting the data for senior citizens
senior_citizens = census[census[:,0]>60,:]
# Calculating the average working hours for senior citizens 
working_hours_sum = np.sum(senior_citizens[:,6])
senior_citizens_len = len(senior_citizens)
print(working_hours_sum)
avg_working_hours = working_hours_sum /senior_citizens_len
print(avg_working_hours)
#step 5
# Data where education years > 10
high = census[census[:,1]>10]
# Data where education years < 10
low = census[census[:,1]<10]
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.around(np.mean(low[:,7]),decimals = 2) + 0.01
print(avg_pay_high)
print(avg_pay_low)
avg_pay_high > avg_pay_low




