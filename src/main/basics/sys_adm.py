import subprocess
# Run a shell command and capture the output
result = subprocess.run(['echo', 'Hello, Python!'], capture_output=True, text=True, shell=True)
print(result.stdout) # Output: Hello, Python!
