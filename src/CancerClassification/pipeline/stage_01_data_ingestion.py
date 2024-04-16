from CancerClassification.config.configuration import ConfigurationManager
from CancerClassification.components.data_ingestion import DataIngestion
from CancerClassification import logger



STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} has started <<<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} successfully completed >>>>>><<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
