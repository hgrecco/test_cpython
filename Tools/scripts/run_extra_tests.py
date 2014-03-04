
import ensurepip
ensurepip.bootstrap(upgrade=True)

import pip
pip.main(['install', 'flask'])

from flask.testsuite import main
main()
