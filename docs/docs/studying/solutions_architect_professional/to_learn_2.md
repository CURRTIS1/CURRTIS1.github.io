# To Learn 2

## Design Solutions for Organizational Complexity

- If you set Consolidated Billing then 'all features' is not enabled, as such you can't use SCPs etc. Even though “All Features” is enabled by default, this will be overridden if you enable only the “Consolidated Billing” feature
- User-based policy maps the access to a certain IAM user and not to a certain AWS resource.
- For some AWS services, you can grant cross-account access to your resources. To do this, you attach a policy directly to the resource that you want to share, instead of using a role as a proxy.
- Reserved concurrency – Reserved concurrency creates a pool of requests that can only be used by its function, and also prevents its function from using unreserved concurrency.
- SCPs specify the maximum permissions for an organization, organizational unit (OU), or account. When you attach an SCP to your organization root or an OU, the SCP limits permissions for entities in member accounts. Even if a user is granted full administrator permissions with an IAM permission policy, any access that is not explicitly allowed or that is explicitly denied by the SCPs affecting that account is blocked.
- AWS Config can be used to audit for example EC2 instances without tags, but to restrict users to only create instances with tags you'd need to set up an SCP.
- AWSServiceRoleForOrganizations service-linked role is primarily used to only allow AWS Organizations to create service-linked roles for other AWS services. This service-linked role is present in all organizations and not just in a specific OU.
    - For example AWS CloudTrail requires trusted access with AWS Organizations to work with organization trails. If you disable trusted access using AWS Organizations while you're using AWS CloudTrail for organization trails, the trails stop functioning for member accounts because CloudTrail can't access the organization
- In the payer account, you can turn off Reserved Instance discount sharing on the Preferences page on the Billing and Cost Management console.
- AWS FSx - There is no option to Dynamically Allocate the file system size. You can manually adjust the file system size using the Amazon FSx console, the Amazon FSx API, or the AWS CLI.
- IPSec tunnel uses the Internet to transfer data from your VPC to a specified destination
- AWS Generated tags are set in the master account in billing and cost management, not the member
- PowerUserAccess - Provides full access to AWS services and resources, but does not allow management of Users and groups.
- SystemAdministrator - Grants full access permissions necessary for resources required for application and development operations.
- AdministratorAccess - Provides full access to AWS services and resources.

## Design for New Solutions

- OpsWorks lets you use Chef and Puppet to automate how servers are configured, deployed, and managed across your Amazon EC2 instances or on-premises compute environments.
- Redshift DR - only has cross region snapshot copy, not cross region replication
- You can use CloudFront with the on-premises website as the origin.
- Amazon GuardDuty is primarily used as a threat detection service that continuously monitors for malicious or unauthorized behavior to help you protect your AWS accounts and workloads.
- Amazon CloudSearch - you can quickly add rich search capabilities to your website or application. You don’t need to become a search expert or worry about hardware provisioning, setup, and maintenance.

## Accelerate Workload Migration and Modernization

- Lambda only allows functions to run up to 15 minutes
- Oracle RAC is not supported by RDS
- The first setup step for Application Migration Service is creating the Replication Settings template. Add source servers to Application Migration Service by installing the AWS Replication Agent (also referred to as “the Agent”) on them.
- Application Migration Service is a migration tool, it is used to replicate or mirror your on-premises VMs to the AWS cloud
- AWS Migration Hub simply provides a single location to track the progress of application migrations across multiple AWS and partner solutions
- AWS Application Discovery Service helps enterprise customers plan migration projects by gathering information about their on-premises data centers.
- Replatform - 'lift and shift' ie Mysql Database into RDS
- Refactor - rearchitect - more work to make it more cloud native for example MySQL into Aurora or DynamoDB
- aws s3 sync - Syncs directories and S3 prefixes. Recursively copies new and updated files from the source directory to the destination. Only creates folders in the destination if they contain one or more files.
- Route 53 - For ELB, Cloudfront, and S3, always use a Type A Record with an Alias
- Route 53 - For RDS, always use the CNAME Record with no Alias.
- AWS IAM Identity Center supports single sign-on to business applications through web browsers only not mobile apps.

## Continuous Improvement for Existing Solutions

- Cloudfront - Field-level encryption allows you to securely upload user-submitted sensitive information to your web servers.
- ECS Anywhere is a feature of Amazon ECS that lets you run and manage container workloads on your infrastructure.
- AWS Fargate is not available on AWS Outposts
- You can set up an origin failover by creating an origin group with two origins with one as the primary origin and the other as the second origin which CloudFront automatically switches to when the primary origin fails.
- Wildcard certificates cannot consist of multiple domains
- Lambda@Edge is an extension of AWS Lambda, a compute service that lets you execute functions that customize the content that CloudFront delivers.
- S3 is preferable over EFS due to cost
