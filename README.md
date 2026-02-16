# FakeStore API Automation Framework

Python-based API automation framework built with:

- pytest
- requests
- GitHub Actions (CI)

## Project Overview

This project demonstrates automated API testing for the FakeStore API.

It includes:

- Authentication testing (positive and negative scenarios)
- Product endpoint validation
- Schema validation using custom assertions
- Test parametrization
- Session-based token fixture
- CI pipeline with GitHub Actions

---

## Tech Stack

- Python 3.12
- pytest
- requests

---

## Project Structure

api/  
tests/  
utils/  
.github/workflows/  

---

## How to Run Locally

```bash
pip install -r requirements.txt
pytest -q
