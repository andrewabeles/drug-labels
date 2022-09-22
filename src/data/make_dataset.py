# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import pandas as pd 
from src.data.cleaning import process_data


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    logger.info('reading raw data')
    drugs_raw = pd.read_csv('{0}/drugs.csv'.format(input_filepath), usecols=['warnings', 'openfda.product_type'])

    logger.info('processing raw data')
    drugs_processed = process_data(drugs_raw)

    logger.info('writing processed data')
    drugs_processed.to_csv('{0}/drugs.csv'.format(output_filepath), index=False)

    logger.info('done')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
