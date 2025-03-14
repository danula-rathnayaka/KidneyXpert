from KidneyXpert.components.model_evaluation_mlflow import Evaluation
from KidneyXpert.components.model_training import Training
from KidneyXpert.config.configuration import ConfigurationManager
from KidneyXpert import logger

STAGE_NAME = "Evaluating the Model"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.error(f">>>>> Stage {STAGE_NAME} Exception Occured: {e}")
        raise e
