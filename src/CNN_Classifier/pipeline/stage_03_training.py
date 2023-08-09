from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.prepare_callbacks import PrepareCallback
from CNN_Classifier.components.training import Training
from CNN_Classifier import logger

STAGE_NAME = "Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def  main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()   

        trainig_config = config.get_training_config()
        training = Training(config=trainig_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )
    

if __name__ == '__main__':
    try :
        logger.info(f"******************")
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<< \n\n x===============x")
    except Exception as e :
        logger.exception(e)
        raise e