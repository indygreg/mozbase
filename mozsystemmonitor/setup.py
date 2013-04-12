# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

from setuptools import setup

PACKAGE_VERSION = '0.1'

try:
    pwd = os.path.dirname(os.path.abspath(__file__))
    description = open(os.path.join(here, 'README.rst')).read()
except:
    description = ''

setup(
    name='mozsystemmonitor',
    description='Monitor system resource usage.',
    long_description=description,
    license='MPL 2.0',
    packages=['mozsystemmonitor'],
    version=PACKAGE_VERSION,
    install_requires=['psutil'],
)
