#!/usr/bin/env python3
from os import getenv

env1 = getenv('HBNB_MYSQL_USER')
env2 = getenv('HBNB_ENV')

print(env1, env2)
