from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Create Spark session
spark = SparkSession.builder \
    .appName("KafkaSparkIntegration") \
    .getOrCreate()

# Define Kafka source
kafka_brokers = "localhost:9092"
kafka_topic = "api_trial"  # Replace with your Kafka topic

# Read data from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_brokers) \
    .option("subscribe", kafka_topic) \
    .load()

# Cast the value column to String
df = df.selectExpr("CAST(value AS STRING)")

# Perform any processing you want (for example, just print the data)
query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Await termination of the streaming query
query.awaitTermination()
