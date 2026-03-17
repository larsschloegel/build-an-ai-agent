# Motivation for this project

Currently, I am programming more in Python in my spare time and would like to delve deeper into the programming language and about Agentic AI tools.

# What include this project

As part of the Boot.dev learning platform, there is a small project where I build a “Claude Code” clone using Google's Gemini API, which helped me achieve my goal. So this CLI tool:

1. Accepts a coding task
2. Chooses from a set of predefined functions to work on the task, for example:
- Scan the files in a directory
- Read a file's contents
- Overwrite a file's contents
- Execute the Python interpreter on a file
3. Repeats step 2 until the task is complete (or it fails miserably, which is possible)


For example, I have a buggy calculator app, so I used my agent to fix the code:

> uv run main.py "fix my calculator app, it's not starting correctly"
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly. The output shows the expression and the result in a formatted way.
