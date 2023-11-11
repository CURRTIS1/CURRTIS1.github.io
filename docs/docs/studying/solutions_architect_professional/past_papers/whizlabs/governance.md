## Governance

A telecom firm is deploying EKS based web applications across hundreds of the different AWS accounts. The Central IT team will be using AWS Service Catalog to create the portfolio of the approved products. End users should be able to perform troubleshooting on the deployed products but should not make any parameter changes in the configuration of the products. End users should not have full access to the EKS clusters.
What solution can be suggested for this requirement?

- Create portfolios with AWS Service Catalog using launch constraints. Use AWS IAM permissions to define service actions
- Create portfolios with AWS Service Catalog using launch constraints. Use AWS Systems Manager documents to define service actions
- Create portfolios with AWS Service Catalog using template constraints. Use AWS IAM permissions to define service actionswrong
- `Create portfolios with AWS Service Catalog using template constraints. Use AWS Systems Manager documents to define service actions`

!!! note
    Template constraints restrict the parameters the end user can use, Service actions are managed by Systems Manager documents.
___

A large company has deployed several applications in AWS cloud with multiple accounts in AWS Organizations. The Central Operations team is planning to deploy compliance requirements for all resources along with remediation actions for any deviation observed in device configuration. They are using AWS IAM to centrally manage access to resources in all the accounts. Configuration and compliance data should be centrally collected for viewing the status of resources in the entire organization. The proposed solution should be scalable and cost-effective.

What solution can be proposed for this requirement?

- Use conformance packs to deploy a pack of Config rules and remediation actions in all accounts within AWS Organizations. For AWS IAM, create config rules in each region. Create an organizations-based aggregator to aggregate AWS Config data from your entire organization
- `Use conformance packs to deploy a pack of Config rules and remediation actions in all accounts within AWS Organizations. For AWS IAM, create config rules only in a single region. Create an organizations-based aggregator to aggregate AWS Config data from your entire organization`

!!! note
    For global services like IAM you wouldn't create rules in multiple regions as you'll get duplicate compliance reports

___

A large enterprise has deployed different environments for their container-based applications across multiple AWS Accounts. The platform team manages the infrastructure for the application while the developer team works on the application delivery in various environments. The platform team needs to ensure security and regulatory guidelines are implemented for all AWS resources when developers deploy applications in various environments. For AWS IAM policies, the Platform team needs to enforce the principle of least privilege among these accounts. The platform team is looking for the most efficient way of implementing both requirements.

What solution can be designed for this requirement?

- Create portfolios with AWS Service Catalog for the developer team to deploy resources in AWS Cloud. Create AWS IAM permissions using AWS-managed policieswrong
- `Create environment templates and service templates using AWS Proton. IAM service roles can be provided in the AWS proton templates`

!!! note
    With AWS Proton, the AWS IAM role is supplied along with the templates which consist of the permissions required to provision resources. This helps to enforce the principle of least privilege across all accounts instead of managing custom permissions for individual developers or groups.
