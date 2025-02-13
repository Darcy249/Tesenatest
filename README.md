This repository contains an automated test created using Selenium WebDriver. The test verifies whether it is possible to search for a product on automationexercise.com and open its product page.

Before running the test, ensure that you have Python 3.13+, Google Chrome with the correct ChromeDriver, and all required libraries installed from the requirements.txt file.

To install the dependencies, first clone the repository using git clone https://github.com/Darcy249/Tesenatest.git and navigate to the folder with cd Tesenatest. Then, create and activate a virtual environment using python -m venv .venv, and activate it with source .venv\Scripts\activate on Windows or source .venv/bin/activate on Mac/Linux. Next, install all dependencies by running pip install -r requirements.txt.

You can run the test using pytest -v test.py. The test results will be displayed in the console, and screenshots will be saved in the screenshots folder.

File Structure:
The Tesenatest folder contains:

test.py (the automated test)
requirements.txt (list of dependencies)
README.md (this file)
screenshots (folder for saved screenshots)
If the test does not run, check the ChromeDriver and Google Chrome versions. XPath locators can be adjusted according to the current website structure.
