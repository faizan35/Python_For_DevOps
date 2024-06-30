# Python For DevOps <img src="./Img/python.png" width="35">

Welcome to the "Learning Python for DevOps" repository! This repository is designed to guide you through the process of learning Python and applying it to various DevOps practices. Whether you are a beginner or have some experience, this resource aims to provide you with practical exercises and projects to strengthen your Python skills in the context of DevOps.

## Table of Contents

### 0. [Introduction to Python and DevOps](./00-Module/0.1-introduction-to-python.md)

- Overview of Python
- Understanding the role of Python in DevOps
- Setting up your Python environment

### [1. Python Basics](./01-Module/1.1-Python-Basics.md)

- **Topics**:

  - Python syntax and semantics
  - Data types, variables, and operators
  - Control flow (if statements, loops)
  - Functions and modules

- **Exercises**:

  - Write a script to automate a simple task (e.g., renaming files in a directory)
  - Create a module for common utility functions

### Week 2: Advanced Python Concepts

- **Topics**:
  - File handling (reading/writing files)
  - Error handling and exceptions
  - Working with dates and times
  - Regular expressions
- **Exercises**:
  - Develop a script to parse and process log files
  - Write a script that extracts specific data from a text file using regular expressions

### Week 3: Python and Cloud Services (AWS)

- **Topics**:
  - Introduction to Boto3 (AWS SDK for Python)
  - Interacting with AWS services: S3, EC2, Lambda
  - IAM roles and permissions
- **Exercises**:
  - Write a script to upload/download files from S3
  - Automate the creation and termination of EC2 instances
  - Deploy a simple Lambda function using Python

### Week 4: Python and Cloud Services (Azure and GCP)

- **Topics**:
  - Azure SDK for Python (Azure Storage, Azure VM, Azure Functions)
  - Google Cloud SDK for Python (GCS, Compute Engine, Cloud Functions)
- **Exercises**:
  - Create scripts to manage storage in Azure and GCP
  - Automate VM creation and deletion in both Azure and GCP
  - Deploy Python-based serverless functions on Azure Functions and GCP Cloud Functions

### Week 5: Automation and Orchestration with Python

- **Topics**:
  - Introduction to Infrastructure as Code (IaC)
  - Using Python with Terraform
  - Automating cloud infrastructure deployment
- **Exercises**:
  - Write Terraform scripts to deploy a simple cloud environment and automate them with Python
  - Create a Python script to manage Terraform state and deployments

### Week 6: Configuration Management with Python

- **Topics**:
  - Introduction to Ansible
  - Writing Ansible playbooks with Python
  - Using Python for custom Ansible modules
- **Exercises**:
  - Automate the configuration of servers using Ansible playbooks
  - Develop custom Ansible modules in Python for specific tasks

### Week 7: Continuous Integration/Continuous Deployment (CI/CD)

- **Topics**:
  - Introduction to CI/CD concepts
  - Using Python with Jenkins, GitLab CI, or GitHub Actions
  - Automating build and deployment pipelines
- **Exercises**:
  - Create a Python script to trigger CI/CD pipelines
  - Automate testing and deployment of a sample application using a CI/CD tool

### Week 8: Monitoring and Logging with Python

- **Topics**:
  - Integrating Python with monitoring tools (Prometheus, CloudWatch, Stackdriver)
  - Collecting and analyzing logs with Python
  - Setting up alerts and notifications
- **Exercises**:
  - Develop a script to monitor the health of cloud resources and send alerts
  - Automate log collection and analysis from different cloud services

### Week 9: Advanced Scripting and Tool Development

- **Topics**:
  - Writing efficient and scalable Python code
  - Best practices for Python in DevOps
  - Packaging and distributing Python tools
- **Exercises**:
  - Optimize an existing Python script for performance
  - Package a Python automation tool and distribute it as a library or executable

### Week 10: Capstone Project

- **Project**:
  - Develop a comprehensive automation solution that integrates multiple cloud services and DevOps practices using Python. This could involve setting up an automated deployment pipeline, configuring cloud resources, monitoring and logging, and implementing a feedback loop for continuous improvement.

Each week, make sure to document your scripts and solutions, explaining your approach and any challenges you faced. This documentation will be valuable for future reference and as part of your portfolio.

---

## How to Use This Repository

- Each module contains theoretical content and practical exercises.
- Follow the exercises to reinforce your understanding of Python for DevOps.
- The `code` directory contains code snippets and scripts related to each module.

## Getting Started

1. Clone this repository:

   ```bash
   git clone <repo link>
   cd <into the dir>
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate # On Linux: source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start learning and coding! Navigate to each module's directory to access the relevant content.

## Contributing

**Contributions are welcome!** If you find an issue or have suggestions for improvement, please open an issue or submit a pull request.

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.

## License

This project is licensed under the [MIT License](LICENSE).

Happy coding and enjoy your journey into Python for DevOps!
