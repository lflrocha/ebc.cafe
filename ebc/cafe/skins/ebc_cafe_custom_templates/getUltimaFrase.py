## Script (Python) "getAnteriores"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna uma lista de noticias de acordo com os parametros informados


programa = context.portal_catalog.searchResults(portal_type='Programa', sort_on='getData', sort_order='reverse', review_state='published')[0]

frase = programa.getFrase

if not frase: 
    frase = "."

return frase