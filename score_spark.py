def init():
    from pyspark.ml import PipelineModel
    global m
    # deserialize the Spark ML pipeline
    m = PipelineModel.load("mySparkMLModel.mml")
    
def run(inputString):
    import json
    from pyspark.ml import PipelineModel
    from pyspark.sql.functions import col

    inputJson = json.loads(inputString)
    df = spark.createDataFrame(sc.parallelize(inputJson))
    # add schema back
    df = df.select(col("_1").alias("feature1"), col("_2").alias("feature2"), col("_3").alias("label")))

    # score the model
    score = m.transform(df).collect()[0]['prediction']   
    return score

if __name__ == '__main__':
    init()
    import json
    print (run(json.dumps([[42, "red", 999]])))