 Allen Solly Sales Forecasting project focuses on analyzing and predicting sales performance using data from the "AS_SALES.csv" file. The process begins with importing essential libraries such as pandas for data manipulation and matplotlib and seaborn for visualizations.

The sales data is cleaned by filtering invalid entries in the 'Bill Date' column and converting it to a datetime format, followed by extracting year and month information for detailed monthly analysis. The data is then grouped by product type and year-month to aggregate total sales values, allowing for the identification of top product types each month.

Additionally, sales performance is examined by individual salespersons through various visualizations, highlighting total sales by salesperson and product classes. For predictive modeling, the dataset is preprocessed to define target and feature variables, and categorical variables are handled with one-hot encoding.

A linear regression model is initially employed, achieving an accuracy of 86%, while further exploration includes Lasso and Ridge regression models along with hyperparameter tuning. The project also integrates XGBoost and Random Forest models, achieving accuracy levels of 87% and 86%, respectively, providing comprehensive insights into sales performance and showcasing the effectiveness of different modeling approaches.






