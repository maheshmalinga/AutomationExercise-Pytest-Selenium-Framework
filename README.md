# AutomationExercise Pytest Selenium Framework

## Project Overview
This project is an automated UI testing framework developed for the
[AutomationExercise](https://automationexercise.com/) e-commerce website.

The framework validates critical functionalities such as:
- Home page header elements visibility
- Login functionality with valid and invalid credentials

## Tech Stack
- Python
- Selenium WebDriver
- Pytest
- Pytest Parametrization & Markers

## Features
- Page Object Model (POM) design
- Reusable pytest fixtures
- Parametrized test cases for better coverage
- Custom pytest markers (smoke, regression)
- Clean and scalable test structure

## Test Scenarios Covered
- Verify home page header elements visibility
- Verify login with invalid credentials
- Verify login page navigation and UI elements

## How to Run Tests
```bash
pip install -r requirements.txt
pytest -v
