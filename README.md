
# AWS Serverless Resume API (Lambda, DynamoDB, API Gateway, S3)

A fully serverless web application that serves my a resume summary via an API and tracks visitor count in real-time.

## Project Overview
This project demonstrates how to build a scalable, cost-efficient backend using serverless technologies. It exposes a REST API that retrieves resume data and dynamically increments a visitor counter stored in a NoSQL database.

## Architecture
This application is built using a serverless architecture on Amazon Web Services:

- Amazon API Gateway – exposes a public REST API endpoint
- AWS Lambda – handles backend logic and request processing
- Amazon DynamoDB – stores resume data and tracks visitor count
- Amazon S3 – hosts the frontend static website
[![aws-serverless-resume-api.png](https://i.postimg.cc/x8nkFwnK/aws-serverless-resume-api.png)](https://postimg.cc/VrZLJHS6)

## ⚙️ How It Works
1. A user visits the frontend hosted on S3
2. JavaScript sends a GET request to the API Gateway endpoint
3. API Gateway triggers the Lambda function
4. Lambda:
- Increments the Views counter in DynamoDB
- Retrieves resume data
5. The API returns the response in JSON format
6. The frontend displays the updated view count

## 🌐 Live Demo
http://sam-gh-cloud-resume.s3-website-us-east-1.amazonaws.com

## 🛠️ Implementation Steps
🔹 Step 1: Set Up DynamoDB (Database Layer)

- Created a table named CloudResumeTable
- Configured partition key: ID (String)
- Added an item with resume data:
    - Name, Skills, Experience, Education
    - Views initialized to 0

[![Dynamo-DBtable.png](https://i.postimg.cc/BQQk5BXX/Dynamo-DBtable.png)](https://postimg.cc/s1qTsSPr)


🔹 Step 2: Build Lambda Function (Backend Logic)
- Created a Lambda function using Python (Boto3)
- Implemented logic to:
    - Increment the Views count using UpdateItem
    - Retrieve resume data using GetItem
- Handled DynamoDB reserved keyword issue (Views) using ExpressionAttributeNames
- Fixed JSON serialization issue by converting Decimal values to integers

[![Get-Resume-Lambda-Function.png](https://i.postimg.cc/hPdx5Hzg/Get-Resume-Lambda-Function.png)](https://postimg.cc/vcGc12tS)


🔹 Step 3: Configure IAM Permissions
- Attached AmazonDynamoDBFullAccess policy to Lambda execution role
- Enabled Lambda to interact with DynamoDB securely
[![IAM-Permissions.png](https://i.postimg.cc/02VQZnnc/IAM-Permissions.png)](https://postimg.cc/BX14nxdK)

🔹 Step 4: Create API Gateway (Public Endpoint)
- Created a REST API using API Gateway
- Defined a resource /resume
- Created a GET method integrated with Lambda
- Enabled CORS for browser-based requests
- Deployed API to a prod stage

[![api-gateway.png](https://i.postimg.cc/kMfqd4St/api-gateway.png)](https://postimg.cc/hhzHLKpS)


🔹 Step 5: Test the API
- Invoked the API endpoint via browser
- Verified:
    - JSON response returned correctly
    - Views count increments on each refresh
[![api-endpoint-output.png](https://i.postimg.cc/R0Rbn34s/api-endpoint-output.png)](https://postimg.cc/rdD9Bwdx)


🔹 Step 6: Build Frontend (S3 Static Website)
- Created a static HTML page (index.html)
- Used JavaScript (Fetch API) to call the API endpoint
- Displayed resume data and live visitor count
[![index-html-with-javascript.png](https://i.postimg.cc/ZK6k55BM/index-html-with-javascript.png)](https://postimg.cc/kBMYj9yQ)

🔹 Step 7: Host Frontend on S3
- Created an S3 bucket
- Enabled static website hosting
- Uploaded frontend files
- Configured bucket policy for public access
[![S3-bucket.png](https://i.postimg.cc/sDmcckbk/S3-bucket.png)](https://postimg.cc/jLWPqFxc)

[![s3-serving-static-website.png](https://i.postimg.cc/Wb1r2hfW/s3-serving-static-website.png)](https://postimg.cc/yW2WjYKc)

🔹 Step 8: Debugging & Optimization
- Used CloudWatch logs to debug Lambda errors:
    - Fixed reserved keyword issue (Views)
    - Resolved Decimal JSON serialization error
- Verified end-to-end integration across all services

[![Cloud-Front-error-logs.png](https://i.postimg.cc/Y0GvWWKc/Cloud-Front-error-logs.png)](https://postimg.cc/8fGk8szw)

















## Authors

- [@bigsam233](https://www.github.com/bigsam233)




## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/samuel-tettey-fio/)


