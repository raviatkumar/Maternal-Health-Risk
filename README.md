# Maternal Health Risk

![Alt text](https://raw.githubusercontent.com/raviatkumar/Maternal-Health-Risk/main/Image/Meternal.jpg)

## Output
![Alt text](https://raw.githubusercontent.com/raviatkumar/Maternal-Health-Risk/main/Output/maternal.PNG)

#### Installation

To install the required packages for this project, use the following command after creating a virtual environment:

```bash
pip install -r requirements.txt
```

*Note: The model was trained on Google Colab with GPU support.*

#### How to Run the App

After installing the necessary packages, run the following command from the project root directory to start the app:

```bash
pip install Flask
```

```bash
python app.py
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) from your browser to access Swagger. You can upload an image through the predict endpoint and receive a JSON response. Use the `--reload` argument to see immediate effects when changing code.

#### How to Run the App with Docker

Ensure you are in the project root directory and Docker is running. Use the following command to create a Docker image:

```bash
docker build -t image-classifier-api .
```

Once the image is built successfully, run the container with the following commands:

```bash
docker run -p 5000 image-classifier-api
```

Visit http://127.0.0.1:5000/docs from your browser to access Swagger. You can upload an image through the predict endpoint and receive a JSON response.


## Problem Description

Pregnancy is a pivotal phase in a woman's life, demanding meticulous monitoring of maternal health to ensure the well-being of both the expecting mother and the unborn child. Complications during pregnancy can pose serious risks, necessitating early detection and intervention. This notebook is dedicated to leveraging machine learning methods to forecast the risk levels of pregnant women by analyzing essential health attributes.

The primary objective is to develop a predictive model that assesses the potential risks associated with pregnancy based on a set of crucial health indicators. These indicators may include maternal age, medical history, lifestyle factors, and various physiological parameters. The model aims to provide healthcare professionals with a tool to identify high-risk pregnancies early on, allowing for timely interventions and personalized care plans.

The analysis will involve exploring diverse datasets containing information on pregnant women, encompassing variables such as blood pressure, glucose levels, BMI, and genetic factors. The machine learning algorithms employed will be trained to recognize patterns and relationships within the data, enabling the model to make accurate predictions regarding the likelihood of complications during pregnancy.

Key challenges include handling missing or incomplete data, ensuring the model's interpretability for healthcare professionals, and addressing ethical considerations associated with predictive analytics in maternal health. The ultimate goal is to create a reliable and interpretable tool that assists healthcare providers in making informed decisions about maternal care, contributing to the overall improvement of pregnancy outcomes.

This notebook endeavors to conduct a thorough analysis of various algorithms to assess their efficacy in predicting pregnancy risk levels using the provided health attributes. The findings from this analysis aim to enhance maternal health monitoring and facilitate personalized healthcare interventions during pregnancy.

## Data Description

Age: Represents the age of pregnant women in years. Any ages are considered during pregnancy.

Systolic Blood Pressure (SystolicBP): The upper value of Blood Pressure measured in millimeters of mercury (mmHg). Systolic blood pressure is a significant attribute during pregnancy.

Diastolic Blood Pressure (DiastolicBP): The lower value of Blood Pressure measured in millimeters of mercury (mmHg). Diastolic blood pressure is another significant attribute during pregnancy.

Blood Glucose Levels (BS): Blood glucose levels expressed in terms of a molar concentration, measured in millimoles per liter (mmol/L).

Body Temperature (BodyTemp): Represents the body temperature of pregnant women, measured in degrees Fahrenheit (F).

Heart Rate: A normal resting heart rate of pregnant women, measured in beats per minute (bpm).

Risk Level: Predicted Risk Intensity Level during pregnancy, considering the previous health attributes. This is the target variable for risk prediction.

## Conclusion

Age and Risk Level:
The high-risk group tends to be older, with a median age around 50, while the low-risk group has a median age of around 30.
There's a positive correlation between age and risk level, but it's not absolute; younger people can also be at high risk.

Blood Sugar Levels and Risk:
High-risk individuals generally have higher blood sugar levels than those with low risk.
The median blood sugar level is higher for the high-risk group, and there's more variability in blood sugar levels within the high-risk group.

Heart Rate and Risk:
There's a positive correlation between heart rate and risk level, with higher risk individuals having higher heart rates.
High-risk individuals exhibit the highest heart rates, as indicated by the data points in the top right corner of the plot.

Risk Level Distribution:
The most frequent risk level is "low risk," followed by "mid risk" and then "high risk."
Majority of data points fall under the lower risk categories.

Body Temperature and Risk:
People with high risk tend to have higher body temperatures than those with low risk.
There's some overlap in body temperatures between risk groups.

Memory and Risk:
There appears to be a positive correlation between memory scores and risk level.
Memory scores range from 0 to 100, with higher scores associated with lower risk levels.

Blood Glucose Levels and Age:
There's a positive correlation between age and blood glucose levels for all risk levels.
The difference in blood glucose levels between risk levels appears to increase with age.

Diastolic Blood Pressure and Risk:
There's a positive correlation between diastolic blood pressure and risk level.
High-risk individuals tend to have the highest diastolic blood pressure readings.

Systolic Blood Pressure and Age:
Younger people tend to have lower systolic blood pressure than older people, regardless of risk level.
High-risk individuals generally have higher systolic blood pressure at all ages.

Risk Level and Memory (Heatmap):
There seems to be a positive correlation between memory and risk level, with higher memory scores associated with lower risk levels.

Best Model for Deployment:
Considering overall accuracy, balanced performance, and class-wise metrics, the Catboost model emerges as the most suitable for deployment. It achieves the highest overall accuracy, maintains strong precision and recall across classes, and exhibits slightly better performance than LGBM. Deploying the Catboost model would likely result in a robust and accurate classification system for the given task.
