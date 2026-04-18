<img width="1024" height="1536" alt="ChatGPT Image Apr 18, 2026, 05_05_02 PM" src="https://github.com/user-attachments/assets/1393812a-2258-4d94-98aa-35ee31e0bd79" /># RailSense : Smart Passenger Boarding Predictor for Indian Railways
We predict passenger no-show probability using features like delay, distance, departure time, and congestion.
Data is processed and models are trained in Databricks, with a Decision Tree used for interpretable predictions.
A Streamlit app takes user inputs and outputs the no-show probability in real time.

**Live Link** 
https://railsense.streamlit.app/#train-boarding-expecation-predictor 

**Data used** : https://drive.google.com/file/d/1rKhPqcbpdbproUSpVQoKqCCosiz-ckzE/view?usp=sharing 
We have used publicly available datasets and concatenated them to fit to our problem statement.

**Diagram**



**Databricks Tech Used**
Databricks Lakehouse Platform
Apache Spark (PySpark) — data processing & feature engineering
Delta Lake — structured storage and efficient data handling

**Open-Source Models Used**
-Scikit-learn
-Decision Tree Classifier
-Logistic Regression (baseline)

