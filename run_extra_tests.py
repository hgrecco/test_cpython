import sys

import ensurepip
try:
    ensurepip.bootstrap(upgrade=True)
except:
    sys.exit(1)
    
import pip
pip.main(['install', 'flask'])

from flask.testsuite import main
main()
