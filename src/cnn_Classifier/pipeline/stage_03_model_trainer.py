from cnn_Classifier.config.configuration import ConfigurationManager
from cnn_Classifier.components.model_trainer import Training
from cnn_Classifier import logger

STAGE_NAME = "Training"


class ModelTrainingPipeLine:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == "__main__":
    try:
        logger.info(f">>> Stage {STAGE_NAME} started <<<")
        obj = ModelTrainingPipeLine()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} complete <<<")
    except Exception as e:
        logger.exception(e)
        raise e