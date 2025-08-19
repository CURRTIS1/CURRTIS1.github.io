## IOT

A start-up firm has deployed IoT sensors across various cities to capture environmental data. This data needs to be captured and analyzed before publishing it to the website. The processed time-series data from these sensors should be stored in an optimized way so that queries can be run on these data sets in the future.

- Collect sensor data using Amazon Kinesis Data Streams. Use Amazon Kinesis Analytics to perform analytics on the sensor datawrong
- `Collect sensor data using Amazon Kinesis Data Streams. Use AWS Lambda to send data from AWS Kinesis Data Streams to AWS IoT data channel and to AWS IoT Analytics. Use Amazon IoT Analytics to perform analytics on the sensor data`

!!! note
    Look for IOT services in the answer

___

An engineering firm is planning to deploy IoT sensors across its multiple factories. The deployment will be performed using ready-to-use simple devices. Users in the project deployment group need to access these IoT devices using mobile devices as well from the AWS console. Once deployment is complete, the Operations team needs to proactively determine the state of these IoT devices to perform maintenance activities.
What solution can be designed to meet these requirements?

- `Use AWS IoT 1-Click to access devices remotely using mobile devices. Use AWS IoT Events to ingest data from IoT devices to detect the state of the devices and alert the Operations team`
- Use AWS IoT 1-Click to access devices remotely using mobile devices. Use AWS IoT Device Management to ingest data from these devices to detect the state of the devices and alert the Operations team

!!! note
    AWS IoT Events is a service used to detect and respond to events from IoT sensors.  It monitors IoT sensors for operational changes and initiates actions to alert users.

___

An automotive company has deployed IoT sensors across its factory locations. Designers are looking for the digital twins of the vehicles manufactured at these locations to address any anomalies in the design and resolve design issues efficiently. They need to have a 3D scene viewer and dashboard templates once digital twins are created. AWS IoT SiteWise is used to pull data together from multiple data sources in its factory locations.

- `Use AWS IoT TwinMaker to create digital twin graphs from connected data sources. To build dashboards, create a web-based digital twin application using AWS IoT TwinMaker plug-in for Amazon Managed Grafana`

!!! note
    AWS IoT TwinMaker is a service to create digital twins. Digital Twins are the virtual representation of the physical system which gets updated regularly.

___

A large engineering firm has deployed IoT sensors in multiple factories to collect equipment metrics. Analysts in the head office need to query equipment metrics in these locations to get the health status of the equipment and visualize metrics in near-real time. In the future, there would be thousands of sensors added in new factory locations which should be provisioned automatically for data ingestion and performance insights of the equipment .

- Ingest data from IoT Core via MQTT protocol to AWS IoT SiteWise. Use the AWS IoT SiteWise plugin for Grafana to get near-real-time visualization of the equipment’s data. Use the Amazon CloudFormation template to automate the creation of AWS IoT SiteWise resources
