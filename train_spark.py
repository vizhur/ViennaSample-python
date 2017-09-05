import pyspark
from pyspark.ml.classification import LogisticRegression

import mmlspark
from mmlspark.TrainClassifier import TrainClassifier
from mmlspark.ComputeModelStatistics import ComputeModelStatistics

from azureml.logging import get_azureml_logger

dataFile = 'mydata.csv'

# Start Spark application
spark = pyspark.sql.SparkSession.builder.appName("MyApp").getOrCreate()

# initialize the logger
run_logger = get_azureml_logger()

# Create a Spark dataframe out of the csv file.
data = spark.createDataFrame(pd.read_csv(dataFile, dtype={"feature1": np.float64, "feature2": string, "label": string}))

# Split data into train and test.
train, test = data.randomSplit([0.75, 0.25], seed=123)

# Train a model
model = TrainClassifier(model=LogisticRegression(), labelCol="label").fit(train)

# Evaluate the model
metrics = ComputeModelStatistics().transform(prediction)
print("******** MODEL METRICS ************")
print("Accuracy is {}.".format(metrics.collect()[0]['accuracy']))
print("Precision is {}.".format(metrics.collect()[0]['precision']))
print("Recall is {}.".format(metrics.collect()[0]['recall']))
print("AUC is {}.".format(metrics.collect()[0]['AUC']))

# log accuracy and AUC
run_logger.log("Accuracy", metrics.collect()[0]['accuracy'])
run_logger.log("AUC", metrics.collect()[0]['AUC'])

######## Persist the Model ######
model.write().overwrite().save("mySparkMLModel.mml")
