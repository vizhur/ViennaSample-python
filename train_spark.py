import pyspark
from pyspark.ml.classification import LogisticRegression

import mmlspark
from mmlspark.TrainClassifier import TrainClassifier
from mmlspark.ComputeModelStatistics import ComputeModelStatistics

from azureml_sdk import data_collector

dataFile = 'mydata.csv'

# Initialize the logger
run_logger = data_collector.current_run() 

# Start Spark application
spark = pyspark.sql.SparkSession.builder.appName("MyApp").getOrCreate()

# initialize the logger
run_logger = data_collector.current_run()

######## Load Data ##############
# TO DO: load data
# Create a Spark dataframe out of the csv file.
data = spark.createDataFrame(pd.read_csv(dataFile, dtype={"col1": np.float64, "col2": string}))

# Split data into train and test.
train, test = data.randomSplit([0.75, 0.25], seed=123)

######## Train a Model ##########
model = TrainClassifier(model=LogisticRegression(), labelCol="col2").fit(train)

######## Evaluate the Model #####
metrics = ComputeModelStatistics().transform(prediction)
print("******** MODEL METRICS ************")
print("Accuracy is {}.".format(metrics.collect()[0]['accuracy']))
print("Precision is {}.".format(metrics.collect()[0]['precision']))
print("Recall is {}.".format(metrics.collect()[0]['recall']))
print("AUC is {}.".format(metrics.collect()[0]['AUC']))

run_logger.log("Accuracy", metrics.collect()[0]['accuracy'])
run_logger.log("AUC", metrics.collect()[0]['AUC'])

######## Persist the Model ######
model.write().overwrite().save("myModel.mml")