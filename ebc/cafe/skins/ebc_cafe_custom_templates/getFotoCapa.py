## Script (Python) "getFotoCapa"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Retorna um nome de arquivo para ser usado como foto da capa


padrao = [ 'capa01.jpg','capa02.jpg','capa03.jpg','capa04.jpg','capa05.jpg', \
          'capa06.jpg','capa07.jpg', ]

ultimo = context.portal_catalog.searchResults(portal_type='Programa', sort_on='getData', sort_order='reverse', review_state='published')[0]
imagem = ultimo.getImagem


if not imagem:
	imagem = context.portal_url() + '/' + padrao[random.randint(0,6)] 
else:
	imagem = ultimo.getURL() + "/imagem"

return imagem