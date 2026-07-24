Module 1 — Introduction to AWS Lambda & Serverless Basics (Detailed Notes)
1. What is AWS Lambda?

Amazon Web Services Lambda is a serverless compute service provided by AWS where you can run code without creating or managing servers.

In simple words:

You write the code, upload it, and AWS runs it automatically whenever an event occurs.

Example:

You upload a file to S3 → Lambda automatically starts → processes file → loads data into database.

You do not need to:

Create EC2 server
Install operating system
Patch server
Scale infrastructure
Manage CPU/RAM manually

AWS handles everything.

2. Real World Meaning of Lambda

Suppose you work in a Data Engineering project.

Daily CSV file arrives in S3.

Without Lambda:

Server Running 24 Hours
        ↓
Cron Job Checks Folder
        ↓
Reads File
        ↓
Processes Data

Problem:

Server cost is always running
Maintenance required
Scaling issue

With Lambda:

CSV File Uploaded to S3
          ↓
S3 Event Trigger
          ↓
Lambda Starts Automatically
          ↓
Validate + Process File
          ↓
Load into Redshift

Benefits:

No server management
Auto scaling
Pay only when used
Event driven

This is why Lambda is heavily used in data engineering pipelines.

3. What is Serverless?

Many people misunderstand serverless.

Wrong understanding:

“Serverless means no servers.”

This is incorrect.

Correct meaning:

Servers exist, but AWS manages them for you.

You do not see:

Server provisioning
Patching
Scaling
Maintenance

AWS hides infrastructure.

Example:

Traditional restaurant:

You cook food yourself.

Serverless restaurant:

You order food and receive it.

You don’t care:

Who cooks
Kitchen size
Gas
Equipment

You only care about output.

Same in Lambda.

You only write code.

AWS handles infrastructure.

4. Traditional Server vs Serverless
Feature	Traditional Server	Lambda (Serverless)
Server management	Yes	No
Auto scaling	Manual	Automatic
Cost	Always running	Pay per execution
Maintenance	High	Very low
Provisioning	Required	Not required
Idle cost	Yes	No

Example:

EC2

You launch server.

24 hours running

Even if no requests come:

You pay.

Lambda

No request:

No cost

Triggered only when needed.

5. Why AWS Created Lambda?

Before Lambda:

People used EC2 for everything.

Problems:

1. Idle Infrastructure Cost

Even when no processing happens:

Server ON = Money charged

Example:

Daily job runs only 5 minutes.

Still:

You pay for 24 hours.

Bad optimization.

2. Scaling Problem

Suppose traffic suddenly increases.

Traditional system:

100 users
↓
10000 users

Server crashes.

Need:

Auto Scaling Group
Load balancer
More EC2 instances

Complex setup.

Lambda solves this automatically.

3. Infrastructure Management

Teams wasted time on:

OS updates
Patch management
Security fixes
Capacity planning

Instead of coding business logic.

AWS solved this with Lambda.

6. Why Use Lambda?

Common reasons:

1. Cost Efficient

You pay only for:

Execution time

Example:

Function runs for 3 seconds.

Pay for:

3 seconds

Not 24 hours.

2. Auto Scaling

100 requests:

Lambda creates multiple instances.

1000 requests:

Lambda automatically scales.

No manual work.

Example:

100 files uploaded

AWS may run:

100 Lambda executions in parallel
3. Event Driven

Lambda starts automatically.

Events can come from:

S3
API Gateway
SQS
SNS
DynamoDB
EventBridge
CloudWatch

Example:

File upload

Immediately processing starts.

4. Faster Development

Focus only on business logic.

Example:

Instead of building:

Server
OS
Scaling
Security

You only write:

validate_file()
load_to_redshift()
7. When Should We Use Lambda?

Good use cases:

Short-running tasks

Example:

File processing
API backend
Data transformation
Notifications
Event-based systems

Example:

S3 Upload
↓
Lambda
↓
ETL Processing
APIs

Example:

API Gateway
↓
Lambda
↓
Database
Automation

Example:

Daily report generation.

8. When NOT to Use Lambda?

Very important interview topic.

Do NOT use Lambda for:

Long Running Jobs

Lambda max timeout:

15 minutes

Bad example:

Huge Spark ETL taking 2 hours.

Better:

EMR
Glue
ECS
EC2
Heavy Memory/CPU Workloads

Example:

Training ML model.

Bad for Lambda.

Better:

SageMaker
EC2 GPU
Stateful Applications

Lambda is stateless.

Bad:

Chat session storage in memory.

9. AWS Lambda Architecture

Basic flow:

User/Event
      ↓
Trigger
      ↓
AWS Lambda
      ↓
Execution Environment
      ↓
Business Logic
      ↓
Response

Real example:

S3 File Upload
        ↓
S3 Event Trigger
        ↓
Lambda
        ↓
Read CSV
        ↓
Validate Data
        ↓
Load Redshift
        ↓
Store Logs
10. Lambda Internal Working (Very Important)

What happens internally?

Suppose S3 uploads file.

Step 1

Event generated.

New file uploaded
Step 2

AWS detects trigger.

Step 3

Lambda execution environment created.

AWS allocates:

CPU
Memory
Runtime

Example:

Python 3.11 runtime
Step 4

Code loaded.

Step 5

Function executes.

Step 6

Response returned.

Step 7

Environment may stay warm.

This improves performance.

This leads to:

Cold Start

New container creation.

Slower.

Warm Start

Reused environment.

Faster.

11. Important Lambda Terminologies
Function

Your actual code.

Example:

def lambda_handler(event, context):
    return "Hello"
Trigger

Starts Lambda.

Example:

S3 upload.

Event

Input data.

Example:

Bucket name + filename.

Context

Runtime metadata.

Contains:

Function name
Remaining time
Memory limit
Runtime

Programming language environment.

Examples:

Python
Java
Node.js
Go
Timeout

Maximum execution time.

Max:

15 minutes
Memory

RAM allocated.

Example:

512 MB

Higher memory often means better CPU performance too.

12. Real Data Engineering Example

Your current type of use case:

Monthly Excel File
        ↓
S3 Bucket
        ↓
Lambda Trigger
        ↓
Read XLSX
        ↓
Column Mapping
        ↓
Validation
        ↓
CSV Conversion
        ↓
COPY to Redshift
        ↓
Archive File
        ↓
CloudWatch Logs

This is a practical Lambda pipeline.