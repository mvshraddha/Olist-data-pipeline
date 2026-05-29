import sys
from datetime import datetime

from pyspark.context import SparkContext
from pyspark.sql.functions import to_timestamp
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame

# Today's date folder
today = datetime.now().strftime("%Y-%m-%d")

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read CSV
datasource0 = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={
        "paths": [
            "s3://olist-raw-ap-south-1/raw-data/2026-05-06/olist_orders_dataset.csv"
        ]
    },
    format="csv",
    format_options={
        "withHeader": True,
        "separator": ","
    }
)

# Convert DynamicFrame to Spark DataFrame
df = datasource0.toDF()

# Convert date column
df = df.withColumn(
    "order_purchase_timestamp",
    to_timestamp(
        "order_purchase_timestamp",
        "yyyy-MM-dd HH:mm:ss"
    )
)

# Convert back to DynamicFrame
final_dyf = DynamicFrame.fromDF(df, glueContext, "final_dyf")

# Write parquet
glueContext.write_dynamic_frame.from_options(
    frame=final_dyf,
    connection_type="s3",
    connection_options={
        "path": f"s3://olist-raw-ap-south-1/cleansed-data/{today}/"
    },
    format="parquet"
)

job.commit()