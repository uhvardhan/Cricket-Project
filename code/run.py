import re
import requests

# Read the webpage
response = requests.get('https://www.espncricinfo.com/series/indian-premier-league-2024-1410320/delhi-capitals-vs-kolkata-knight-riders-16th-match-1422134/full-scorecard')
content = response.text

# Use regular expressions to find lines starting with "Over""
pattern = r'Over .*'
over_lines = [line.strip() for line in content.split('\n') if re.match(pattern, line)]


# Print the matching lines
for line in over_lines:
    print(line)