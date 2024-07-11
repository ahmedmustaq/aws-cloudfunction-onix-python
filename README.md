
# AWS Cloud Function for ISBN

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The AWS Cloud Function for ISBN project is designed to manage and process ISBN-related data using serverless architecture. This project leverages AWS Lambda, S3, SNS, and SES to provide a scalable and efficient solution for ISBN data handling.

## Features

- AWS Lambda functions for processing ISBN data.
- Integration with AWS S3 for storing and retrieving data files.
- Notifications using AWS SNS.
- Email notifications using AWS SES.

## Technologies Used

- Python
- AWS Lambda
- AWS S3
- AWS SNS
- AWS SES
- Pydantic
- Boto3
- Serverless Framework

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- pip
- AWS CLI configured with your credentials
- Serverless Framework (`npm install -g serverless`)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ahmedmustaq/aws-cloudfunction-isbn.git
cd aws-cloudfunction-isbn
```

2. Set up the virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r mbs-service/requirements.txt
```

### Deploying the Application

Deploy the application using the Serverless Framework:

```bash
cd mbs-service
serverless deploy
```

## Configuration

The configuration files are located in the `mbs-service` directory. Key configuration files include:

- `serverless.yml`: Configuration for deploying the application using the Serverless Framework.

## Usage

### Basic Usage

This project provides a Lambda function for handling ISBN data. The function is triggered by S3 events, processes the data, converts it to CSV format, and sends an email with the CSV attachment. It also publishes a notification to an SNS topic.

### Custom Data Models

The project includes comprehensive data models for ISBN data, located in the `onix-schema/model.py` file. These models define the structure and validation rules for the data processed by the application.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
