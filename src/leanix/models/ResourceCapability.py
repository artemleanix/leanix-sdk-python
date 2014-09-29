#!/usr/bin/env python
"""
The MIT License (MIT)	 

Copyright (c) 2014 LeanIX GmbH

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
class ResourceCapability:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'ID': 'str',
            'displayName': 'str',
            'parentID': 'str',
            'level': 'long',
            'name': 'str',
            'reference': 'str',
            'alias': 'str',
            'description': 'str',
            'tags': 'list[str]',
            'fullName': 'str',
            'factSheetHasParents': 'list[FactSheetHasParent]',
            'factSheetHasChildren': 'list[FactSheetHasChild]',
            'resourceHasResourceCapabilities': 'list[ResourceHasResourceCapability]',
            'factSheetHasDocuments': 'list[FactSheetHasDocument]'

        }


        self.ID = None # str
        self.displayName = None # str
        self.parentID = None # str
        self.level = None # long
        self.name = None # str
        self.reference = None # str
        self.alias = None # str
        self.description = None # str
        self.tags = None # list[str]
        self.fullName = None # str
        self.factSheetHasParents = None # list[FactSheetHasParent]
        self.factSheetHasChildren = None # list[FactSheetHasChild]
        self.resourceHasResourceCapabilities = None # list[ResourceHasResourceCapability]
        self.factSheetHasDocuments = None # list[FactSheetHasDocument]
        
