# **Laboratory 6**
Build a classification model using the **Heart Disease UCI dataset**, perform data cleaning, visualize key relationships, and evaluate model performance using metrics like accuracy, precision, recall, and F1 score. You can get the dataset [here](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

Submit the visualizations in a document. Include reflection text documenting your process and understanding.

Heart Disease UCI Dataset on Kaggle (*Alternatively, upload a CSV version directly to Colab*)

1. **Import Libraries & Load Data**
>* Read the CSV file into a DataFrame
Display data structure and summary
2. **Preprocessing**
>* Handle missing values (if any)
>* Convert categorical variables into numerical (using label encoding or one-hot encoding)
>* Normalize or scale numerical features if needed
3. **Exploratory Data Visualization**
>* Create at least three visualizations to explore:
>>* Distribution of target variable
>>* Correlation heatmap
>>* Comparison of features across the target (e.g., chest pain vs. target)
4. **Build a Predictive Model**
>* Split the data into training and testing sets
>* Train a **Logistic Regression** or **Random Forest Classifier**
>* Evaluate using accuracy, precision, recall, and F1 score
5. **Visualize Results**
>* Plot the **confusion matrix** using Seaborn
>* Create a **bar chart comparing all the evaluation metrics**
