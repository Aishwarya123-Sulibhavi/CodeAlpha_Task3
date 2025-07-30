import re

# Input and output file paths
input_file = "input.txt"
output_file = "emails.txt"

# Read content from the input file
with open(input_file, 'r') as file:
    content = file.read()

# Regular expression to find emails
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)

# Remove duplicates (optional)
unique_emails = list(set(emails))

# Write extracted emails to output file
with open(output_file, 'w') as file:
    for email in unique_emails:
        file.write(email + '\n')

print(f"{len(unique_emails)} email(s) extracted and saved to '{output_file}'.")
