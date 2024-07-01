from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_callbacks import PrepareCallback
from cnnClassifier.components.training import Training
from cnnClassifier import logger

STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callback_config = config.get_prepare_callback_config()
        prepare_callback = PrepareCallback(prepare_callback_config)
        callback_list = prepare_callback.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(training_config)
        training.get_base_model()
        training.train_vaild_generator()
        training.train(
            callback_list=callback_list
        )

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e