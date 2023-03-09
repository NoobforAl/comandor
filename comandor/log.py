import logging as log

FORMAT: str = '%(asctime)s : %(levelname)s : %(name)s : %(message)s'
DATEFMT: str = '%d-%b-%y %H:%M:%S'

# Setup basics setting logger
log.basicConfig(level=log.INFO, format=FORMAT, datefmt=DATEFMT)
