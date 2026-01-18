import os
import sys
from dotenv import load_dotenv
import pyspark

def setup_pyspark_env():
    """
    Loads environment variables from .env, sets Hadoop bin on PATH (Windows),
    and prints key environment info for debugging.
    """
    load_dotenv()
    if "HADOOP_BIN" in os.environ:
        os.environ["PATH"] = os.environ["HADOOP_BIN"] + ";" + os.environ["PATH"]
    print("Python executable:", sys.executable)
    print("HADOOP_HOME:", os.environ.get("HADOOP_HOME", "Not set"))
    print("JAVA_HOME:", os.environ.get("JAVA_HOME", "Not set"))
    print("PySpark version:", pyspark.__version__)
