## Script (Python) "getFotos"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=

root = context.portal_url.getPortalObject().getPhysicalPath()[1]

path = '/' + root + '/multimidia/fotos'
fotos = context.portal_catalog.searchResults(Type="Image", path=path)
return fotos
