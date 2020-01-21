import thrift_sasl
from pyhive import hive
from TCLIService.ttypes import TOperationState

from pyhive import hive
conn = hive.connect(host='1.6.194.180', port=10000,auth='NOSASL')
print(f'Hi:{conn}')
