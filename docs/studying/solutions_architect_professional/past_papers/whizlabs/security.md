## Security.md

A company has deployed a web application using AWS resources across multiple regions. There is an external audit scheduled. The operations team will be using the AWS Audit manager to collect all assessment reports. The team needs to upload physical records which are generated outside of AWS Cloud and should be part of the evidence. The final assessment report should be shared with external auditors securely.

What solution can be designed for this requirement?

- `Upload manual evidence to Amazon S3 bucket. Retrieve evidence data in each region from AWS Audit Manager storage. Generate Assessment reports from AWS Audit Manager and store them in Amazon S3 to share with external auditors`

!!! note
    AWS Audit Manager can be used to continually audit AWS usage helping to manage risk and compliance with regulations and industry standards. For uploading manual evidence, files must be stored in an Amazon S3 bucket and then uploaded to AWS Audit manager assessments.

___

A company has multiple AWS accounts. Recently there was a misconfiguration in one of the accounts leading to the outage. Further investigation found that there was an AWS IAM cross-account role that made the configuration changes. The issue is resolved, but Operations Head is looking for a solution that will help to analyze and monitor changes done by cross-account roles in the most efficient way. Activities done by cross-account roles should be tracked.

What solution can be suggested for this purpose?

- `Enable Amazon GuardDuty and use GuardDuty findings with Amazon Detective to determine specific cross-account roles which perform the activity`
- Use AWS CloudTrail event history to search events. Analyze events to determine specific cross-account roles which perform the activity

!!! note
    Analysing Cloudtrail event history isn't efficient.<br>
    Amazon Detective helps to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities. It can analyze data from sources such as Amazon VPC flow logs, AWS CloudTrail logs, Amazon EKS audit logs, and Amazon GuardDuty findings. <br>
    Amazon Detective has a role session analysis feature that can provide visibility to role usage, cross-account role assumptions, and any role-chaining activities performed across multiple AWS accounts. It quickly determines who has assumed the role, for what duration, and what activities were performed by the role in the resource configurations.

___

An engineering firm has deployed a critical web application in AWS Cloud. Application and database servers will be deployed on Amazon EC2 instances. Security Head is looking for network security controls at the application layer. All traffic between application and database servers should be inspected and traffic filtering should be implemented for secure communication. As an AWS Architect, you will need to design a solution for deploying fine-grained traffic control between these servers in an efficient way.

How can a solution be designed for this requirement?

- `Launch servers in two separate subnets in the same VPC. Provision an AWS Network Firewall in a separate subnet in the same VPC. Modify route table entries for each subnet with the destination as VPC CIDR and target as firewall endpoint instead of local. Firewall subnet will have a route table with the destination as VPC CIDR and the target as local`

!!! note
    AWS Network Firewall can be used to inspect and control traffic between VPCs or between subnets in the same VPC. With VPC routing enhancements, AWS Network Firewall can be inserted between 2 subnets in the same VPC.<br>
