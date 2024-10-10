import subprocess

# Run the first Python file and wait for its completion
subprocess.run(["python", "B1.py"], check=True)

# Once the first script has completed, run the IPython Notebook file
subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "B2.ipynb"], check=True)

