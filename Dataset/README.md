
# Fire Detection Model [Machine Learning code](forestModel.py)

## Overview

This Python script builds a machine learning model for fire detection using satellite data. The dataset includes various features related to satellite observations, and the target variable is the confidence level of fire occurrences.

## Author

- [Khaled Salama](https://www.linkedin.com/in/5aledsalama/)

## Dataset

The dataset used in this project is loaded from the 'fire_archive.csv' file. It contains information about various satellite observations related to fire incidents.

## Dependencies

Make sure to install the required Python libraries:

```bash
pip install pandas numpy seaborn matplotlib scikit-learn
```

## Exploratory Data Analysis (EDA)

- Load the dataset and perform initial exploratory data analysis.
- Check for missing values and handle them appropriately.
- Visualize the correlation matrix to understand feature relationships.


## Data Preprocessing

- Drop unnecessary columns ('track', 'instrument', 'version').
- Handle categorical variables ('daynight', 'satellite', 'type') using one-hot encoding.
- Bin the 'scan' column and create a new feature 'scan_binned'.
- Extract year, month, and day from the 'acq_date' column.

## Model Building

- Split the dataset into training and testing sets.
- Build a Random Forest Regressor model.
- Evaluate the model's performance on the test set.
- Save the trained model using pickle.

## Hyperparameter Tuning

- Conduct hyperparameter tuning using RandomizedSearchCV to find optimal model parameters.
- Build a new Random Forest Regressor model with the best parameters.
- Evaluate the tuned model's performance on the test set.
- Save the tuned model using pickle.

## Results

- Display the accuracy scores for both the initial and tuned models.

## Future Improvements

- Explore more advanced feature engineering techniques.
- Experiment with different machine learning algorithms.
- Collect more data for training and testing.

## License

This project is licensed under the [MIT License](LICENSE).

