## Condensed notes

## IOT

- AWS IoT FleetWise makes it easier for you to collect, transform, and transfer vehicle data to the cloud in near real time and use that data to improve vehicle quality, safety, and autonomy.
- AWS IoT Rules give your devices the ability to interact with AWS services. Rules are analyzed and actions are performed based on the MQTT topic stream
- AWS IoT SiteWise is a managed service that makes it easy to collect, store, organize and monitor data from industrial equipment at scale to help you make better, data-driven decisions. You can use AWS IoT SiteWise to monitor operations across facilities, quickly compute common industrial performance metrics, and create applications that analyze industrial equipment data to prevent costly equipment issues and reduce gaps in production.
- AWS IoT TwinMaker makes it easier for developers to create digital twins of real-world systems such as buildings, factories, industrial equipment, and production lines
- AWS IoT Device Management can be used to update and reboot devices
- AWS IoT Device Defender can be used for the security management of IoT devices. It can perform tasks such as audit configurations, authenticate devices, detect anomalies, and receive alerts from the IoT sensor fleet.
- AWS IoT Device management is not a suitable service to access IoT devices via mobile devices.
- AWS IoT Events is a service used to detect and respond to events from IoT sensors

## To sort

- When you purchase a Reserved Instance, you determine the scope of the Reserved Instance. The scope is either regional or zonal.
    - Regional: When you purchase a Reserved Instance for a Region, it's referred to as a regional Reserved Instance.
    - Zonal: When you purchase a Reserved Instance for a specific Availability Zone, it's referred to as a zonal Reserved Instance.
- Amazon Fraud Detector needs training on historical datasets as model inputs
- Kinesis firehose sends data in near real-time and not in real-time.
- For Lambda max memory you can get this from Cloudwatch Logs, not metrics. You can get invocations from metrics.
- AWS Wavelength zones use Transit Gateway to communicate. Each zone must have a VPC
- AWS Blockchain proposals are approved by current members, not an administator in the network.
- In AWS Blockchain you need a single VPC Privatelink endpoint for all members
- AWS PrivateLink provides private connectivity between virtual private clouds (VPCs), supported AWS services, and your on-premises networks without exposing your traffic to the public internet.
- AWS PrivateLink allows VPCs with overlapping CIDRs to connect.
- AWS Storage Gateway seamlessly connects on-premises applications to cloud storage, it's not used in a DR situation.
- Timestream stores and organizes your time series data to optimize query processing time and to reduce storage costs. It offers data storage tiering and supports two storage tiers: a memory store and a magnetic store.
    - The memory store is optimized for high throughput data writes and fast point-in-time queries.
    - The magnetic store is optimized for lower throughput late-arriving data writes, long term data storage, and fast analytical queries.
- AWS Application Migration Service requires a USER with the predefined IAM policy “AWSApplicationDiscoveryAgentAccess”.
- AWS Config is a pre-requisite on member accounts for organisationalAWS Firewall Manager
- AWS Glue (ETL) - AWS Glue is a serverless data integration service that makes data preparation simpler, faster, and cheaper. You can discover and connect to over 70 diverse data sources, manage your data in a centralized data catalog, and visually create, run, and monitor ETL pipelines to load data into your data lakes.

## API Gateway

- Request parameter-based Lambda authorizers are supported only for WebSocket API and not REST APIs.
- In Lambda proxy integration, API Gateway passes the raw request to the integrated Lambda function as it is. You can not configure the property mapping for a proxy integration.

## Datastores

### Data Exchange

- Allows data providers to distribute the data and data subscribers to consume that data

### Redshift

- You cannot disable manual snapshots

### DMS

- The mapping rule should be put in the source endpoint configuration rather than the task settings if S3 is the source for DMS.

## EC2

- If you stop an instance in a placement group and then start it again, it still runs in the placement group. However, the start fails if there isn't enough capacity for the instance.
- If you receive a capacity error when launching an instance in a placement group that already has running instances, stop and start all of the instances in the placement group, and try the launch again.

## Security

- AWS Shield protects against DDOS
- AWS WAF is a web application firewall that lets you monitor the HTTP and HTTPS requests that are forwarded to your protected web application resources.
- AWS WAF you can protect against SQL injections
