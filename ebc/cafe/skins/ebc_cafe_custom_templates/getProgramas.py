## Script (Python) "getAnteriores"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna uma lista de noticias de acordo com os parametros informados


dict = {}


programas = context.portal_catalog.searchResults(portal_type='Programa', \
                                                 sort_on='getData',      \
												 review_state='published')


for programa in programas:
	ano = DateTime(programa.getData).year()
	mes = DateTime(programa.getData).month()
	dia = DateTime(programa.getData).day()
	if dict.has_key(ano):
		dict[ano][mes].append(programa)
	else:
		dict[ano] = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[],}
		dict[ano][mes].append(programa)


return dict