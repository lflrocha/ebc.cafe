# -*- coding: utf-8 -*-
"""Definition of the Programa content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from ebc.cafe import cafeMessageFactory as _
from ebc.cafe.interfaces import IPrograma
from ebc.cafe.config import PROJECTNAME

ProgramaSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'frase',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Frase do programa"),
            size=60,
        ),
    ),

    atapi.DateTimeField(
        'data',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Data do programa"),
            show_hm=False,
        ),
        required=True,
        validators=('isValidDate'),
    ),

    atapi.TextField(
        'transcricao',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label=_(u"Transcrição"),
            rows=10,
        ),
        default_output_type = "text/html",
        default_content_type = "text/plain",
        allowable_content_types = ("text/plain",
                                   "text/html")
    ),

    atapi.FileField(
        'audio.mp3',
        storage=atapi.AnnotationStorage(),
        widget=atapi.FileWidget(
            label=_(u"Arquivo de áudio com qualidade baixa"),
        ),
        required=True,
        validators=('isNonEmptyFile'),
        mutator='setAudio',
        acessor='getAudio',
        primary = 1,
    ),

    atapi.FileField(
        'alta',
        storage=atapi.AnnotationStorage(),
        widget=atapi.FileWidget(
            label=_(u"Arquivo de áudio com qualidade alta"),
        ),
        validators=('isNonEmptyFile'),
    ),

    atapi.ImageField(
        'imagem',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Imagem"),
            description=_(u"Field description"),
        ),
        validators=('isNonEmptyFile'),
        original_size=(281,306),
    ),


))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

ProgramaSchema['title'].storage = atapi.AnnotationStorage()
ProgramaSchema['description'].storage = atapi.AnnotationStorage()
ProgramaSchema['description'].widget.label = "Resumo"
ProgramaSchema['location'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['language'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['expirationDate'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['creators'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['contributors'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['rights'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['allowDiscussion'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['excludeFromNav'].widget.visible = {"edit": "invisible", "view": "invisible"}
ProgramaSchema['nextPreviousEnabled'].widget.visible = {"edit": "invisible", "view": "invisible"}

schemata.finalizeATCTSchema(
    ProgramaSchema,
    folderish=True,
    moveDiscussion=False
)

class Programa(folder.ATFolder):
    """ """
    implements(IPrograma)

    meta_type = "Programa"
    schema = ProgramaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')


    def get_size(self):
        """ZMI / Plone get size method
        """
        f = self.getPrimaryField()
        if f is None:
            return 0
        else:    
            bytes = float(f.get_size(self))
            if bytes >= 1048576:
                megabytes = bytes / 1048576
                size = '%.2fMb' % megabytes
            elif bytes >= 1024:
                kilobytes = bytes / 1024
                size = '%.2fKb' % kilobytes
            else:
               size = '%.2fb' % bytes
        return size


    def get_size_alta(self):
        f = self.getField('alta') 
        if f is None:
            return 0
        else:    
            bytes = float(f.get_size(self))
            if bytes >= 1048576:
                megabytes = bytes / 1048576
                size = '%.2fMb' % megabytes
            elif bytes >= 1024:
                kilobytes = bytes / 1024
                size = '%.2fKb' % kilobytes
            else:
               size = '%.2fb' % bytes
        return size


    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    imagem = atapi.ATFieldProperty('imagem')


atapi.registerType(Programa, PROJECTNAME)
