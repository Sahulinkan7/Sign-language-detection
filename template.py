import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s')

list_of_files=[
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_validation.py",
    f"src/components/model_trainer.py",
    f"src/components/model_pusher.py",
    f"src/entity/__init__.py",
    f"src/configuration/__init__.py",
    f"src/configuration/s3_operation.py",
    f"src/constant/__init__.py",
    f"src/constant/training_pipeline/__init__.py",
    f"src/constant/application.py",
    f"src/entity/config_entity.py",
    f"src/entity/artifacts_entity.py",
    f"src/utils/__init__.py",
    f"src/utils/main_utils.py",
    f"src/pipeline/__init__.py",
    f"src/pipeline/training_pipeline.py",
    f"src/exception.py",
    f"src/logger.py",
    "setup.py",
    "requirements.txt",
        
]

for filepath in list_of_files:
    filepath= Path(filepath)
    
    filedir, filename = os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory : {filedir} for the file {filename}")
        
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file : {filename}")
            
    else:
        logging.info(f"{filename} is already created")