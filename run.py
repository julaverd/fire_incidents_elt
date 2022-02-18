from fire_incidents_extract.extract import Extract
from fire_incidents_load.load import Load
import logging

def main():
    logging.basicConfig(filename='fire_pieline.log', level=logging.INFO)
    logging.info('PIPELINE STARTED')
    logging.info('<< Extract Step Started')
    extractor = Extract()
    is_extracted = extractor.read_source()
    if is_extracted == 200:
        logging.info('Extract Step Finished >>')
    else:
        logging.error('Extract Step Don´t Finished >>')
        return False
    logging.info('<< Load Step Started')
    loader = Load()
    df_data = loader.load_data_local()
    loader.copy_data(df_data)
    logging.info('Load Step Finished >>')
    logging.info('PIPELINE FINISHED')

if __name__ == '__main__':
    main()