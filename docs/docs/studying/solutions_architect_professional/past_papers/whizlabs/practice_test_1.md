## Practice Test 1

An engineering firm has deployed a critical application on the web servers of an Amazon EC2 instance launched in a VPC. The Operations Team is looking for a detailed analysis of the traffic from these web servers. They have enabled VPC flow logs on the VPC. Logs should be analyzed using open-source tools in near-real time and should be visualized to create dashboards.

What solution can be proposed for this requirement?

- `Ingest VPC flow logs to Amazon Kinesis Data Firehose which will deliver these logs to Amazon OpenSearch Service for analyzing and visualizing logs in near-real time`

!!! note
    Amazon OpenSearch Service (OpenSearch Service) makes it easy to deploy, operate, and scale OpenSearch Service for log analytics, full text search, application monitoring, and more.

___

You are an AWS Solutions Architect in a financial company. The company recently started working on migrating legacy applications to AWS. You planned to use a new AWS Organization to manage all AWS accounts so that you can easily configure accounts, assign organizational units, configure security policies, etc. Which methods are valid for you to add accounts to the Organization? (Select TWO)

- `In the AWS Organization console, create accounts within your organization`
- `In the management account of the Organization, create invitations to other accounts and wait for them to accept the invitations`

!!! note
    Accounts cannot request to join an organisation, it has to be invited or created from the org.

___

You have signed in to an AWS Organization's management account using an admin IAM user. You need to move accounts to this Organization from one OU (Organizational Unit) to another or back to the root from an OU. However, the operation was disallowed due to a lack of permissions. So you started looking at the IAM policies attached to this user. Which permissions do you need to move accounts among OUs? (Select TWO)

- `organizations:DescribeOrganization`
- `organizations:MoveAccount`

___

In an AWS Organization, the Root is attached to a default SCP that allows all actions on all resources. And other OUs or AWS accounts are attached with SCPs that contain Deny lists. For example, an SCP that denies cloudtrail:StopLogging is attached to an OU. However, you think that the Deny lists can be improved to contain more services such as those that are not used. How would you find out the AWS services that are allowed by the SCP but are never used?

- `In the IAM console, click the Organization activity and check the last accessed data to identify services that are never used`
- In the AWS Config console, list the AWS services that are not used by IAM userswrong

!!! note
    service report in Organization Activity can be used to identify the AWS services to be included in the Deny lists.

![orgreport](../../../../assets/images/orgreport.png "orgreport.png")

___

You were hired as an AWS Architect in a company to help migrate legacy applications from on-premises to AWS. The team is trying to use AWS Migration Hub to visualize the migrating process. The first step is using discovery tools to get valuable server data such as performance summary and performance time series. The team has good SQL experience, so they hope that AWS Athena can be used to analyze the imported data. Given that the legacy applications are installed in Linux CentOS 7 or above physical servers, which discovery tool is the best for you to use?

- `Install AWS Discovery Agent on the servers which transmit data to AWS Application Discovery Service. Then in Migration Hub, enable the Data Exploration in Amazon Athena`
- Install AWS Discovery Agent on the physical servers and configure the agent to send data to an S3 bucket. Create related tables in AWS Athena to analyze the server data

!!! note
    Discovery Agent can transfer data securely to Application Discovery Service instead of S3.

___

Your company owns a large number of on-premises virtual machines managed in VMware vCenter. To plan the migration from local servers to AWS, you have installed AWS Discovery Connector in the VMware vCenter Server that helps collect information about the virtual machines. The Discovery Connector has already registered with the Application Discovery Service successfully. Which data can be discovered by the Discovery Connector? (Select TWO.)

- 
- 
- 
