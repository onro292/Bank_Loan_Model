# Bank_Loan_Model
The complete project comprises of using Python to extract data from the csv file cleaning and analyzing it. As well as training and deploying a machine learning model through an API created with Flask and Waitress.


Bank_Loan_Project.ipynb is the most recent jupyter notebook. The actual workbook has markdown text that walks you through the project. However, in a nutshell the workflow used within the Bank_Loan_Project.ipynb is:
* Clean and manipulate data using Pandas 
* Plot data using seaborn/matplotlib 
* Train a machine learning model using scikit-learn
* Package the model as a pickle file


The class_deploy.py file is the flask app API that hosts the model.pkl machine learning model.
requests.py is a test to make sure the API was up and running.
