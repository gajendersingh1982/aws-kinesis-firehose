# aws-kinesis-firehose
 
## Create setting in Glue
- Create Glue Database
- Create Table in this database (manually)
	- Add S3 bucket path (s3://***/)
	- Add Classification as Parquet
	- Add Data Columns (According to application any type)
	- Add partition columns (YYYY-DD-MM-HH) all int

## Crreate Firehose	
- Create Data Firehose Stream (Select Name)
	- Source (Direct PUT)
    - Transform source records with AWS Lambda (Add Lambda for transformation)
	- Convert record format - Enabled (Select DB created in steps above)
	- Select Bucket Path same as in Glue (s3://***/)
		- Select this as S3 Prefix for partitioning --> [AWS Link for study](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html)\
		raw/year=!{timestamp:YYYY}/month=!{timestamp:MM}/day=!{timestamp:DD}/hour=!{timestamp:HH}/
		- Select this in error bucket (Mandatory when we give s3 Prefix)\
		error/!{firehose:error-output-type}/year=!{timestamp:YYYY}/month=!{timestamp:MM}/day=!{timestamp:DD}/hour=!{timestamp:HH}/
	- Select S3 backup if required (According to service data retention policy)
	- S3 buffer conditions (for parquet select maximum values)
	- S3 compression and encryption (If required select KMS)

## Use Athena to Query this S3 Bucket
    - Load Partitions ( MSCK REPAIR TABLE 'tableName'; )
    - Query Athena table to see the results

## Edit Sample code to send test put messages to stream according to your DB Table
