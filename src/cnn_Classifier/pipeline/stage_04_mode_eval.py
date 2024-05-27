from cnn_Classifier.config.configuration import ConfigurationManager
from cnn_Classifier.components.model_eval import Evaluation
from cnn_Classifier import logger
import dagshub
dagshub.init(repo_owner='Anhtt9x', repo_name='End-to_End_MLflow', mlflow=True)

STAGE_NAME = "Evaluation stage"

class EvaluationPipeLine:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config  = config.get_evaluation()
        eval = Evaluation(config=eval_config)
        eval.evaluation()
        eval.save_score()
        eval.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>> stage {STAGE_NAME} started <<<")
        obj = EvaluationPipeLine()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} complete <<<")
    except Exception as e:
        logger.exception(e)
        raise e