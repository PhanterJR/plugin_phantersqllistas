# -*- coding: utf-8 -*-
#usado no desenvolcimento
if request.is_local:
	from gluon.custom_import import track_changes
	track_changes()

#tabela usada como exemplo
db.define_table("tipos",
		Field("tipo", "string"),
		format="%(id)s - %(tipo)"
	       )
		
db.define_table("estabelecimentos", 
		Field("estabelecimento", "string"),
		Field("razao_social", "string", label="Razão Social"),
		Field("cnpj", "string", label="CNPJ"),
		Field("tipo", "reference tipos"),
		format="%(id)s - %(estabelecimento)",
	       )

from plugin_phantersqllistas.phantersqllistas import PhanterSqlListas

MODELS_PHANTERSQLLISTAS=PhanterSqlListas(db, "estabelecimentos", "estabelecimento", db.estabelecimentos.id>0)
MODELS_PHANTERSQLLISTAS.setUrlAjax(URL(request.application, "plugin_phantersqllistas", 'echo_phantersqllistas'))
MODELS_PHANTERSQLLISTAS.setCampos(["estabelecimento", "razao_social", "cnpj", "tipos", "novo_campo"])
MODELS_PHANTERSQLLISTAS.setAtributosCampo("estabelecimento",{"_class": "col-3"})
MODELS_PHANTERSQLLISTAS.setAtributosCampo("razao_social",{'_class':'col-3'}) 
MODELS_PHANTERSQLLISTAS.setAtributosCampo("cnpj",{"_class":'col-2'})
MODELS_PHANTERSQLLISTAS.setAtributosCampo("tipos",{"_class": "col-2"})
MODELS_PHANTERSQLLISTAS.setAtributosCampo("novo_campo",{"_class": "col-2"})
MODELS_PHANTERSQLLISTAS.modificarCampoDados("novo_campo", lambda row: "%s-%s" %(row.id, row.estabelecimento))
MODELS_PHANTERSQLLISTAS.addMenuItem(lambda row: A("Visualizar", _href=URL("default", "index", args=['editar', row.id]), _class="link_dropdown dropdown-item"))
MODELS_PHANTERSQLLISTAS.addMenuItem(lambda row: A("Editar", _href=URL("default", "index", args=['editar', row.id]), _class="link_dropdown dropdown-item"))
