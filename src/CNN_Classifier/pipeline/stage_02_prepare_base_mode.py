from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.prepare_base_model import PrepareBaseModel
from CNN_Classifier import logger

STAGE_NAME = "prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        prepare_base_model_config=config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f"***************************")
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<< \n\n x===========x")
        
    except Exception as e:
        logger.exception(e)
        raise e