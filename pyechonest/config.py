#!/usr/bin/env python
# encoding: utf-8

"""
Copyright (c) 2010 The Echo Nest. All rights reserved.
Created by Tyler Williams on 2010-04-25.

Global configuration variables for accessing the Echo Nest web API.
"""

__version__ = "4.2.13"

import os

if('ECHO_NEST_API_KEY' in os.environ):
    ECHO_NEST_API_KEY = os.environ['ECHO_NEST_API_KEY']
else:
    ECHO_NEST_API_KEY = None


API_HOST = 'developer.echonest.com'
"The API endpoint you're talking to"

API_SELECTOR = 'api'
"API selector... just 'api' for now"

API_VERSION = 'v4'
"Version of api to use... only 4 for now"

HTTP_USER_AGENT = 'PyEchonest'
"""
You may change this to be a user agent string of your
own choosing
"""

TRACE_API_CALLS = False
"""
If true, API calls will be traced to the console
"""

CALL_TIMEOUT = 10
"""
The API call timeout (seconds)
"""

CODEGEN_BINARY_OVERRIDE = None
"""
Location of your codegen binary. If not given, we will guess codegen.platform-architecture on your system path, e.g. codegen.Darwin, codegen.Linux-i386
"""
