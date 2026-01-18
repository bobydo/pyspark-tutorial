# This script activates the virtual environment and sets PYSPARK_PYTHON, then runs the given PySpark script
# Usage: .\run_pyspark.ps1 q1_lazy_execution.py

param(
    [string]$script = ""
)

# Activate the virtual environment
. "D:\pyspark-tutorial\pysparkenv\Scripts\Activate.ps1"

# Set the PYSPARK_PYTHON environment variable
$env:PYSPARK_PYTHON = "D:\pyspark-tutorial\pysparkenv\Scripts\python.exe"

if ($script -ne "") {
    Write-Host "Running $script with PYSPARK_PYTHON set to $env:PYSPARK_PYTHON"
    python $script
} else {
    Write-Host "Virtual environment activated and PYSPARK_PYTHON set. Run your PySpark script now."
}
