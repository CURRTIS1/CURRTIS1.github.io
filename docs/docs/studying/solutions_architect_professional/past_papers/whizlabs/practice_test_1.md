## Practice Test 1

An engineering firm has deployed a critical application on the web servers of an Amazon EC2 instance launched in a VPC. The Operations Team is looking for a detailed analysis of the traffic from these web servers. They have enabled VPC flow logs on the VPC. Logs should be analyzed using open-source tools in near-real time and should be visualized to create dashboards.

What solution can be proposed for this requirement?

-  `Ingest VPC flow logs to Amazon Kinesis Data Firehose which will deliver these logs to Amazon OpenSearch Service for analyzing and visualizing logs in near-real time`

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

