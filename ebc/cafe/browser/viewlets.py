from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.viewlets import common

class SearchBoxViewlet(common.SearchBoxViewlet):
    index = ViewPageTemplateFile('templates/searchbox.pt')

class RodapeViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/rodape.pt')

class DestaqueViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/destaque.pt')