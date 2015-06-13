# -*- coding: utf-8 -*-
"""Definition of the Trecho content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import file
from Products.ATContentTypes.content import schemata

from ebc.cafe import cafeMessageFactory as _
from ebc.cafe.interfaces import ITrecho
from ebc.cafe.config import PROJECTNAME

TrechoSchema = schemata.ATContentTypeSchema.copy() + file.ATFileSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

TrechoSchema['title'].storage = atapi.AnnotationStorage()
TrechoSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(TrechoSchema, moveDiscussion=False)

class Trecho(base.ATCTContent):
    """Description of the Example Type"""
    implements(ITrecho)

    meta_type = "Trecho"
    schema = TrechoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(Trecho, PROJECTNAME)
