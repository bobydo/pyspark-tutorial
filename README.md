# PySpark Tutorial for Beginners - VS Code Edition

## Introduction

This repository provides a hands-on PySpark tutorial using VS Code as the primary development environment. It covers Spark installation, SparkContext, SparkSession, RDD transformations and actions, Spark DataFrames, Spark SQL, and more. The included notebooks and scripts allow you to follow along, experiment, and practice your PySpark skills.

## Environment & Setup

**Recommended Environment:**

✅ Java 17  
✅ Python 3.11 venv  
✅ Spark 4.1.1  
✅ winutils configured  
✅ Stable local[1]  
✅ VS Code interpreter + runtime aligned  

### Quick Start

1. Clone this repository:

   ```bash
   git clone https://github.com/bobydo/pyspark-tutorial
   ```

2. Create a Python 3.11 virtual environment:

   ```bash
   python -m venv pysparkenv
   ```

3. Activate the environment and install dependencies:

   ```bash
   pysparkenv\Scripts\activate
   pip install -r requirements.txt
   pip install pyspark==4.1.1 findspark
   ```

4. Configure all environment variables and paths in the `.env` file at the project root.
5. Open VS Code and select the correct Python interpreter:
   - Load the project folder in VS Code.
   - Press Ctrl + Shift + P and search for "Python: Select Interpreter".
   - Choose: Python 3.11.x (pysparkenv)
   - Confirm the physical path: `\pyspark-tutorial\pysparkenv\Scripts\python.exe`
   - Press Ctrl + Shift + P and select "Reload Window" to apply changes.

## Python Environment & Libraries

The following key Python packages are required and already listed in requirements.txt:

- pyspark==4.1.1
- findspark==2.0.1
- python-dotenv==1.2.1

Other libraries commonly present in the environment (for notebook and VS Code compatibility):
- ipykernel
- jupyter
- traitlets
- tornado
- pygments
- stack_data
- nest_asyncio
- setuptools
- six
- typing_extensions
- decorator
- zmq

These are typically installed automatically when using Jupyter or VS Code Python extensions, and are not required to be listed in requirements.txt for basic PySpark functionality.

## Notebook Descriptions

- **01-PySpark-Get-Started**: PySpark environment setup and configuration.
- **02-Create-SparkContext**: Creating SparkContext objects in different PySpark versions.
- **03-Create-SparkSession**: Creating SparkSession objects in PySpark.
- **04-RDD-Operations**: RDD transformations and actions.
- **05-DataFrame-Intro**: Introduction to Spark DataFrames and differences compared to RDD.
- **06-DataFrame-from-various-data-source**: Creating Spark DataFrame from various data sources.
- **07-DataFrame-Operations**: DataFrame operations like filtering, aggregation, etc.
- **08-Spark-SQL**: Using Spark SQL for DataFrame queries.

Feel free to explore and run these notebooks/scripts at your own pace in VS Code.

## Prerequisites

- Basic knowledge of Python programming.
- Understanding of data processing concepts (no prior PySpark experience required).

## Usage

These notebooks/scripts are meant for self-learning and practice. Follow along with the [tutorial video](https://youtu.be/EB8lfdxpirM) to gain a deeper understanding of PySpark concepts. Experiment with the code, modify it, and try additional exercises to solidify your skills.

## License

This project is licensed under the [MIT License](LICENSE).
