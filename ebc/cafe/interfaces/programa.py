from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from ebc.cafe import cafeMessageFactory as _

class IPrograma(Interface):
    """Description of the Example Type"""
    
    # -*- schema definition goes here -*-
    imagem = schema.Bytes(
        title=_(u"Imagem"), 
        required=False,
        description=_(u"Field description"),
    )

