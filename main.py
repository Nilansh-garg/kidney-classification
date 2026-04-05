from src.cnnClassifier.config.configurartion import ConfigurationManager
from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_model import PrepareBaseModelPipeline
from src.cnnClassifier.pipeline.stage_03_training_model import ModelTrainingPipeline

STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f">>>>>>>>>>>>stage {STAGE_NAME} started<<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "PREPARING MODEL"


try:
    logger.info(f"*******************")
    logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = " MODEL TRAINING " 

if __name__ == '__main__':
    try:
        print("--- DEBUG CHECKPOINT 1: Starting script execution. ---")
        
        print("--- DEBUG CHECKPOINT 2: All imports successful. ---")
        
        config = ConfigurationManager()
        print("--- DEBUG CHECKPOINT 3: ConfigurationManager instantiated. ---")

        obj = ModelTrainingPipeline(config=config)
        print("--- DEBUG CHECKPOINT 4: ModelTrainingPipeline instantiated. ---")

        obj.run()
        
    except Exception as e:
        print(f"--- FATAL ERROR: Script crashed during initialization! Exception: {e} ---")
        logger.exception(e)
        raise e


    