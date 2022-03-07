from azureml.core import Run

run = Run.get_context()

run.parent.log("this is app log")