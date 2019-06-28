from pdb import post_mortem
from sys import exc_info
import traceback
traceback.print_exc()

try:
    0 / 0
except Exception as e:
    print('error: {}'.format(e))
    post_mortem(exc_info()[2])
