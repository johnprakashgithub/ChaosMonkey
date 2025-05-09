import pandas as pd
from test_communication import TestCommunication

# Load the Excel file
file_path = 'Ports_requirements.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Generate pytest tests based on the data in the Excel file
def generate_pytest_tests(df):
    tests = []
    for index, row in df.iterrows():
        test_class = TestCommunication(row['Source'], row['Destination'], row['Port'], row['Protocol'])
        tests.append(test_class)
    return tests

# Generate the tests
pytest_tests = generate_pytest_tests(df)

# Run the tests
for test in pytest_tests:
    test.test_disable_communication()
    test.test_enable_communication()
