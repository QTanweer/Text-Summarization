"""
Data Ingestion Pipeline Stage 01
"""
from textSummarization.config.configuration import ConfigurationManager
from textSummarization.components.data_ingestion import DataIngestion
from textSummarization.logging import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    """
    Data Ingestion Pipeline Stage 01
    """
    def __init__(self):
        pass

    def main(self):
        '''
        Main method for Data Ingestion Pipeline Stage 01
        '''
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(">>>>>Stage: %s started<<<<<" , STAGE_NAME)
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(">>>>>Stage: %s completed<<<<<" , STAGE_NAME)
    except Exception as ex:
        logger.error(ex, exc_info = True)
        raise ex
    