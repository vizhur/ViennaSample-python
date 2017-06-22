import numpy
import pandas as pd
import sklearn

from azureml_sdk import data_collector

# initialize the logger
run_logger = data_collector.current_run()

######## Load Data ##############
# TO DO: load data


######## Train a Model ##########
# TO DO: train model


######## Evaluate the Model #####
# TO DO: evaluate model
run_logger.log('Magic Number', 42)


######## Persist the Model ######
# TO DO: persist model