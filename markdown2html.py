import sys
import os

# Check if the correct number of arguments is provided
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

# Get the input Markdown file and output HTML file names
markdown_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the Markdown file exists
if not os.path.exists(markdown_file):
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# If no errors, exit with code 0
sys.exit(0)
