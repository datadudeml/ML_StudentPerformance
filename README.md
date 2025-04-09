## End to End Machine learning project on Student Performance

This projects aims to understand how  the students performance (test scores) is affected by other variables such as Gender, Ethnicity, Parental education, lunch and test preparation courses

 DataSet Information
- gender : sex of students  -> (Male/female)
- race/ethnicity : ethnicity of students -> (Group A, B,C, D,E)
- parental level of education : parents' final education ->(bachelor's degree,some college,master's degree,associate's degree,high school)
- lunch : having lunch before test (standard or free/reduced) 
- test preparation course : complete or not complete before test
- math score
- reading score
- writing score

## Approach for the project
Data Ingestion :

In Data Ingestion phase the data is first read as csv.
Then the data is split into training and testing and saved as csv file.

Data Transformation :

In this phase a ColumnTransformer Pipeline is created.
for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
This preprocessor is saved as pickle file.

Model Training :

In this phase base model is tested . The best model found was LinearRegressor.
After this hyperparameter tuning is performed.
This model is saved as pickle file.

Prediction Pipeline :

This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

Flask App creation :

Flask app is created with User Interface to predict the student exam performance
