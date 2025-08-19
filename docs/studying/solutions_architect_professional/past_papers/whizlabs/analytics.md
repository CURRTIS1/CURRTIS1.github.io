## Analytics

A healthcare company has terabytes size clinical research data. This third-party data needs to be shared with multiple pharma companies having infrastructure deployed in the AWS cloud. Any revision in the clinical research data should be instantly available to all the pharma companies. Healthcare company is looking for a cost-effective solution that will enable data sharing with thousands of its customers in the future. This solution should be deployed with least-efforts.

What solution can be proposed for this requirement?

- `Use AWS Data exchange to share data with pharma companies`
- Share data with pharma companies using AWS Transfer family

!!! note
    Using Transfer Family will require a lot of effort to manage permissions for each customer.<br>
    AWS Data Exchange is a service for securely sharing and using third-party data on AWS. With AWS Data Exchange, data is stored in an Amazon S3 bucket and is securely shared with the subscribers as a product. Subscribers can browse and subscribe to any data set from the AWS Data Exchange catalog in AWS Marketplace. This helps customers to avoid building a separate data delivery mechanism for sharing data sets with multiple consumers.

___

An IT firm is building a streaming financial application using open-source tools. Large volumes of data will be captured from multiple sources and processed by the consumers. These streaming data need to be retained in encrypted format for a six-month period for processing by the consumers. Clusters created in the AWS cloud should be optimally sized for supporting these large volumes of data streams. As an AWS architect, they are seeking your guidance to help with this deployment in the most efficient way.

What solution can be best suited for this requirement?

- Capture and process streaming data using Amazon Kinesis Data Streams. Use provisioned capacity mode for data streams
- `Deploy Amazon Managed Streaming for Apache Kafka (Amazon MSK) clusters using Amazon EC2 instance. Use Amazon EBS volumes for storage purposes`

!!! note
    Amazon Kinesis Data Streams has a default data retention period of 24 hours which can be extended to 7 days<br>
    Amazon MSK makes it easy to ingest and process streaming data in real time with fully managed Apache Kafka.

___

A banking firm has deployed its financial application using Amazon EC2 instance. Logs from this application should be captured on a daily basis and stored for further analysis. On a weekly basis, analysis should be performed on the stored logs to generate detailed reports. Due to inconsistencies in application usage, logs generated may be of different sizes and need to be captured at flexible times. The proposed solution should be cost-effective and scalable for analyzing massive amounts of logs.

- `Use AWS Data pipeline to create a daily task of copying logs from Amazon EC2 to Amazon S3. Create a weekly task with AWS Data Pipeline to launch Amazon EMR clusters which will perform an analysis of the logs stored in the Amazon S3 bucket`
- Create a daily cron job to schedule copying of logs from Amazon EC2 instance to Amazon S3. Create another weekly cron job to schedule the copying of logs from Amazon S3 to Amazon EMR clusters. Perform analysis of the logs with Amazon EMR clusters

!!! note
    AWS Data Pipeline is managed ETL (Extract Transform and Load) service. It automates data movement and transformation between AWS compute and storage services. With AWS Data Pipeline, a data-driven workflow can be created which helps to create data movement tasks that are dependent on the successful completion of previous tasks.<br>
    AWS Data Pipeline can be used to schedule and start the EMR clusters which will create traffic reports. It will start the EMR clusters only if weekly data is available in the Amazon S3 bucket.

___

A large enterprise company has created a data lake that is managed by a single account. Databases in the data lake need to be accessed by other accounts within the company. Amazon Redshift Spectrum will be used by other accounts on this shared database. The account managing the data lakes should provide access permissions to only selected tables of the database to users in other accounts. After the permissions are granted, other accounts should be able to run Amazon Redshift Spectrum queries on the shared tables in the databases.

- `Share selected tables in the databases using Lake Formation tag-based access control (LF-TBAC). Create a resource link for tables to enable Amazon Redshift Spectrum to run queries on the shared tables`

!!! note
    data location permissions are required by the AWS Glue Crawlers to access data in data lakes from other accounts. For integrated services like Amazon Athena and Amazon Redshift Spectrum, a resource link is required.<br>
    Lake Formation tag-based access control (LF-TBAC): This defines lake formation permission using attributes. In lake formation, tags are called LF-tags which grant permission to access databases with external principals, accounts, and AWS Organization. This is a recommended option for sharing databases with external accounts.
