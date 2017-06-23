def init():
    from pyspark.ml import PipelineModel
    global m
    m = PipelineModel.load("myModel.mml")
    
def run(inputString):
    import json
    from pyspark.ml import PipelineModel
    from pyspark.sql.functions import col

    inputJson = json.loads(inputString)
    df = spark.createDataFrame(sc.parallelize(inputJson))
    df = df.select(col("_1").alias("col1"), col("_2").alias("col2")))

    score = m.transform(df).collect()[0]['prediction']   
    return score