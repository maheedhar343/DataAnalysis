import subprocess
import sys

def run_script(script_name):
    print(f"Running {script_name}...")
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    if result.returncode != 0:
        print(f"Script {script_name} failed with exit code {result.returncode}")
        sys.exit(1)

# Run all scripts sequentially
scripts = ['data_preprocessing.py', 'data_analysis.py', 'data_modeling.py']
for script in scripts:
    run_script(script)

print("All steps completed successfully!")