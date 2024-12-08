from statistics import median, correlation

import pandas as pd
import numpy as np

df = pd.read_csv("student_statistics_data.csv")
#print(df.head)

#calculate the mean of the "Test_Score" column
mean_score = df["Test_Score"].mean()
print(f"The mean number of Test Score is: {mean_score}")


#calculate the mean of the "Hours_studied" column
mean_hours = df["Hours_Studied"].mean()
print(f"The mean number of hours is: {mean_hours}")


#calculate the mode of the "Hours_studied" column
mode_hours = df["Hours_Studied"].mode()[0]
print(f"The mode number of hours is: {mode_hours}")


#calculate the median of the "Hours_studied" column
median_hours = df["Hours_Studied"].median()
print(f"The median number of hours is: {median_hours}")


#calculate the variance
variance=np.var(df["Satisfaction_Score"])
print("The variance is:", variance)

#Correlation
if "Social_Media_Hours" in df.columns and "Quiz_Score" in df.columns:
    correlation = df["Social_Media_Hours"].corr(df["Quiz_Score"])
    print(f"The correlation between Social Media Hours and Quiz Score is:{correlation}")
else:
    print("Error")

#Z_Score
std_dev = df["Test_Score"].std()
print(f"Standard deviation of Test Score: {std_dev}")
score = 85
z_score = (score - mean_score)/std_dev
print(f"The z-score is:{z_score}")

#Z-score -1.5
z_score2= -1.5
score2 = (std_dev*z_score2) + mean_score
print(score2)

#Correlation between Hours Studied and Test Scores:
correlation = df["Hours_Studied"].corr(df["Test_Score"])
print(f"The correlation between hours studied and test scores is:{correlation}")

#Correlation between Sleep Hours and Test Scores:
correlation = df["Hours_Slept"].corr(df["Test_Score"])
print(f"The correlation between sleep hours and test scores is:{correlation}")



