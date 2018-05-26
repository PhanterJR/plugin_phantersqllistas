# -*- coding: utf-8 -*-
if request.is_local:
	from gluon.custom_import import track_changes
	track_changes()

from plugin_phantersqllistas.phantersqllistas import PhanterSqlListas

MODELS_PHANTERSQLLISTAS_ESTABELECIMENTO=PhanterSqlListas(db, "estabelecimentos", "estabelecimento", db.estabelecimentos.id>0)
MODELS_PHANTERSQLLISTAS_ESTABELECIMENTO.setCampos(["estabelecimento", "razao_social", "cnpj", "tipos"])
MODELS_PHANTERSQLLISTAS_ESTABELECIMENTO.setAtributosCampo("estabelecimento",{"_class": "col-4"})
MODELS_PHANTERSQLLISTAS_ESTABELECIMENTO.setAtributosCampo("razao_social",{'_class':'col-4'}) 
MODELS_PHANTERSQLLISTAS_ESTABELECIMENTO.setAtributosCampo("cnpj",{"_class":'col-2'})
MODELS_PHANTERSQLLISTAS_ESTABELECIMENTO.setAtributosCampo("tipos",{"_class": "col-2"})
MODELS_PHANTERSQLLISTAS_ESTABELECIMENTO.addMenuItem(lambda row: A("Editar", _href=URL("servicos", "produtos", args=['editar', row.id]), _class="link_dropdown dropdown-item"))
MODELS_PHANTERSQLLISTAS_ESTABELECIMENTO.addMenuItem(lambda row: A("Editar", _href=URL("servicos", "produtos", args=['editar', row.id]), _class="link_dropdown dropdown-item"))

MODELS_PHANTERSQLLISTAS_VEICULOS=PhanterSqlListas(db, "veiculos", "placa", db.veiculos.id>0)
MODELS_PHANTERSQLLISTAS_VEICULOS.setCampos(["placa", "modelos", "proprietario", "Troca de Óleo(KM)", "Combustível/Litro"])
MODELS_PHANTERSQLLISTAS_VEICULOS.setAtributosCampo("placa",{"_class": "col-1"})
MODELS_PHANTERSQLLISTAS_VEICULOS.setAtributosCampo("modelos",{'_class':'col-3'}) 
MODELS_PHANTERSQLLISTAS_VEICULOS.setAtributosCampo("proprietario",{"_class":'col-4'})
MODELS_PHANTERSQLLISTAS_VEICULOS.setAtributosCampo("Troca de Óleo(KM)",{"_class": "col-2"})
MODELS_PHANTERSQLLISTAS_VEICULOS.setAtributosCampo("Combustível/Litro",{"_class": "col-2"})
MODELS_PHANTERSQLLISTAS_VEICULOS.addMenuItem(lambda row: A("Visualizar Detalhes",_class="link_dropdown dropdown-item", _href=URL('detalhes','veiculo', args=[row.id])))
MODELS_PHANTERSQLLISTAS_VEICULOS.addMenuItem(lambda row: A("Registrar Abastecimento",_class="link_dropdown dropdown-item", _href=URL('opcoes','abastecimento', args=[row.id])))
MODELS_PHANTERSQLLISTAS_VEICULOS.addMenuItem(lambda row: A("Registrar Troca de Óleo",_class="link_dropdown dropdown-item", _href=URL('opcoes','oleo', args=[row.id])))
MODELS_PHANTERSQLLISTAS_VEICULOS.addMenuItem(lambda row: A("Registrar Manutenção",_class="link_dropdown dropdown-item", _href=URL('opcoes','manutencao', args=[row.id])))
