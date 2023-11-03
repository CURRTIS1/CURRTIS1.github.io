## Cost Management

### Design Solutions for Organisational Complexity

- Cost and usage monitoring tools
- Purchasing options (savings plans, reserved instances, stpo instances)
- Rightsizing tools

### Design for new solutions

- Storage tiering
- Data transfer costs
- Managed service options

### Continuous Improvement for Existing Solutions

- Network and data transfer costs
- Cost management, alerting and reporting

### Accelerate Workload Migration and Modernisation

- Total cost of ownership

## Cost Management Overview

Capex - Capital Expenses - Money spent on long term assets like buildings and equipment
Opex - Operational Expenses - Money spent on ongoing costs for running the business, usually variable expenses.

Examples of CapEx include physical assets, such as buildings, equipment, machinery, and vehicles.
Examples of OpEx include employee salaries, rent, utilities, and property taxes.

## Cost Optimisation Strategies

- Appropriate provisioning
- Right-sizing
- Purchase options
- Geographic selection
- Managed services
- Optimised data transfer

### Appropriate provisioning

Provision only what you need, don't leave temporary instances running

Consolidate where possible, perhaps one larger RDS instance than multiple smaller ones

Cloudwatch monitor utilisation

### Rightsizing

Use lowest cost resource that still meets technical requirements

### Purchase options

Reserved instances provide the best cost advantage
Spot instances are good for temporary horizontal scaling

EC2 fleets is a mix of on demand, reserved and spot instances.

### Geographic selection

AWS priving varies from region to region

If it's cheaper in another region and doesn't need to be local then it might be worth hosting in another region

### Managed services

Leverage RDS over database on EC2 for example

Serverless, fargate means you don't need to manage or pay for the infrastructure

### Optimised data transfer

Moving data in to AWS doesn't cost anything, but moving data out or cross-region does.

## Resource groups

Are grouping of AWS assets defined by tags

Can create custom consoles to consolidate metrics, alarm and config details around given tags

EG - Dev, Test, Prod

## Cross account

### Cost and usage reports

Consolidated billing track spending across your organisation

Generate CSV files to track costs
Store the reports in S3 and analyse or visualise with Athena, redshift and quicksight.

### Centralised budget alerts

Create a budget on a specific account or a number of them.

## Reserved instances

- Purchase or agree to purchase usage of EC2 instances in advance for a significant discount
- Provides guaranteed capacity reservation when used in a specific AZ
- Can be shared across multiple accounts with consolidated billing
- If you no longer need RIs you can try and sell them on the reserved instance marketplace

Two types, can be Standard or Convertible

Standard is a higher saving than Convertible

For Convertible you can change the instance family, OS tenancy or payment options

Convertible benefit from price redunctions

Only standard is available to sell on the RI marketplace

## Spot instances

Customer creats a spot request and specifies AMI, instance type and other key information

Dependant on EC2 capacity that AWS tries to sell on a market exchange basis

Define the highest price you'll pay for the instance, it gets terminated it someone pays higher

## Dedicated Instances and Hosts

Dedicated Instances:

- Virtualised instances on hardware
- May share hardware with other non dedicated instances
- Available as On-demand, reserved and spot
- Cost an extra $2 per hour

Dedicated Hosts:

- Physical servers dedicated to just your use
- You have control over which instances are deployed on that host
- Available as On-demand or Dedicated host reservation
- Useful if you have server-bound software licenses that use per-core, per-socker or per-vm
- Each dedicated host can only run one EC2 instance size and type

## Quiz

Which statement is true about Dedicated Instances and Dedicated Hosts?

- Dedicated Hosts reserve capacity.
- Dedicated Instances can run as spot instances.

!!! note
    Unlike Reserved Instances, Dedicated Instances do not provide capacity reservation and merely ensure that your instance runs on hardware that's dedicated to a single customer.<br>
    AWS allows for running Dedicated Instances as spot instances, providing a way to further reduce costs in exchange for the possibility that these instances can be terminated with short notice.
