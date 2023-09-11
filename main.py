Commit: Optimize Python script

- Moved the import statements to the top of the script for better organization and readability.
- Used list comprehensions in the scraping functions for improved readability and performance.
- Replaced regular expressions with the `replace()` function in the `clean_text()` function for removing special characters and extra whitespace.
- Recommended the use of vectorization for sentiment analysis and categorization instead of iterating over each text separately.
- Combined the CSV file saving operations into a single function to reduce code duplication.
- Suggested moving the Flask app code into a separate file to improve modularity.

Please review the updated code and let me know if you need further assistance.
