# Web App Automation 

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Scope of Tests](#scope)
- [Installation](#installation)
  - [Running Tests](#running-tests)
  - [Example report](#example-test)
- [Contact](#contact)

## Introduction
`web automation` is a Python-based repository designed for automated testing of https://www.saucedemo.com/. It provides a framework to write and execute test cases that verify the functionality, reliability, and performance of your API endpoints.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.7 or higher installed on your system.
- `pip` for managing Python packages.

## scope of tests
- 1:Verify page title
- 2:Verify products are listed
- 3:Add product to the cart and verify the cart badge
- 4:Verify sorting of products (if sorting feature exists)
- 5:Verify item can be removed from cart
- 6:Test to check login with invalid credentials
- 7:Test to check login with valid credentials
- 8:Test to check whehter customer is successfully checking out and placing order
- 9:Test to check whether error name is displayed without entering delivery details
- 10:Test to check the disability of continue button without entering credentials

## Installation
1. **Extract the Repository**
   ```bash
   cd Test-Automation
   pip install -r requirements.txt
   
## Running Tests
1. **Run command to run all tests.**
    ```bash
    pytest
   
## Example report
See the report.html file to see the reports. It has all the test results.
The failed tests indicate failure in the UI/API.

## contact
- chaitanya
- phone:9885064363
- linkedin: https://www.linkedin.com/in/chaitanya-bonagiri-798b3899/
- github:https://github.com/chaitu418