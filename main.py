
from cnn_Classifier import logger
from cnn_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnn_Classifier.pipeline.stage_02_base_model import PrepareBaseModelTrainingPipeLine
from cnn_Classifier.pipeline.stage_03_model_trainer import ModelTrainingPipeLine

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>> stage {STAGE_NAME} start <<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} complete <<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"

try:
    logger.info(f"**************")
    logger.info(f">>>> stage {STAGE_NAME} started <<<")
    obj = PrepareBaseModelTrainingPipeLine()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} complete <<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"

try:
    logger.info(f">>> Stage {STAGE_NAME} started <<<")
    obj = ModelTrainingPipeLine()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} complete <<<")
except Exception as e:
    logger.exception(e)
    raise e