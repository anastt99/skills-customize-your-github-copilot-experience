# 📘 Assignment: File I/O and Automation

## 🎯 Objective

Learn how to read from and write to files in Python, parse structured data, and automate a simple report-generation workflow.

## 📝 Tasks

### 🛠️ Load and Analyze File Data

#### Description
Open the sample CSV file and analyze its contents to calculate totals and revenue.

#### Requirements
Completed program should:

- Read `sales-data.csv` from the assignment folder.
- Parse the file data to calculate the total number of items sold and the total revenue.
- Print a summary with the number of records processed, total quantity, and total revenue.

### 🛠️ Write a Report to a File

#### Description
Create a report file that stores the summary results from the data analysis.

#### Requirements
Completed program should:

- Create or overwrite a file named `sales-report.txt`.
- Write a clear summary of the sales totals and revenue into the file.
- Close the file properly so the data is saved.

### 🛠️ Automate the Workflow

#### Description
Implement a reusable function that reads the CSV file and writes the summary report automatically.

#### Requirements
Completed program should:

- Use a function named `generate_sales_report()`.
- Use `with open(...)` for both reading and writing files.
- Call the function so the report is generated when the program runs.
- Example output printed to the console:
  ```text
  Processed 5 sales records.
  Total quantity sold: 39
  Total revenue: $68.10
  Report saved to sales-report.txt
  ```
