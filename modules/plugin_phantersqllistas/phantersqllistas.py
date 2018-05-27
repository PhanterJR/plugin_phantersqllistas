# -*- coding: utf-8 -*-

from gluon.html import *
from pydal.objects import Field
from gluon import current
import json
import types
from plugin_phantersqllistas.remover_acentos import remover_acentos
from plugin_phantersqllistas.conv_datetime import conv_date, conv_datetime

ICONE_MENU=XML("""
<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" width="2480px" height="2480px" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd"
viewBox="0 0 2480 2480"
 xmlns:xlink="http://www.w3.org/1999/xlink">
 <g>
  <path class="fil0" d="M1389.78 986.79c304.318,0 608.637,0 912.956,0 63.9651,0 116.3,52.3351 116.3,116.3 0,110.485 0,220.969 0,331.454 0,63.9651 -52.3351,116.3 -116.3,116.3 -304.32,0 -608.638,0 -912.956,0 -63.9651,0 -116.299,-52.3351 -116.299,-116.3 0,-110.485 0,-220.969 0,-331.454 0,-63.9651 52.3339,-116.3 116.299,-116.3zm0 914.884l912.956 0c63.9651,0 116.3,52.3351 116.3,116.3l0 331.456c0,63.9651 -52.3351,116.3 -116.3,116.3l-912.956 0c-63.9651,0 -116.3,-52.3351 -116.3,-116.3l0 -331.456c0,-63.9651 52.3351,-116.3 116.3,-116.3zm0 -1829.77l912.956 0c63.9651,0 116.3,52.3351 116.3,116.3l0 331.456c0,63.9651 -52.3351,116.3 -116.3,116.3l-912.956 0c-63.9651,0 -116.3,-52.3351 -116.3,-116.3l0 -331.456c0,-63.9651 52.3351,-116.3 116.3,-116.3zm-1286.82 1254.06l479.833 -360.61 479.833 -360.603 0.00354286 721.217 -0.00354286 721.211 -479.833 -360.604 -479.833 -360.612z"/>
  <path class="fil1" d="M1350.49 947.492c304.318,0 608.637,0 912.956,0 63.9651,0 116.3,52.3351 116.3,116.3 0,110.485 0,220.969 0,331.454 0,63.9651 -52.3351,116.3 -116.3,116.3 -304.32,0 -608.638,0 -912.956,0 -63.9651,0 -116.299,-52.3351 -116.299,-116.3 0,-110.485 0,-220.969 0,-331.454 0,-63.9651 52.3339,-116.3 116.299,-116.3zm0 914.884l912.956 0c63.9651,0 116.3,52.3351 116.3,116.3l0 331.456c0,63.9651 -52.3351,116.3 -116.3,116.3l-912.956 0c-63.9651,0 -116.3,-52.3351 -116.3,-116.3l0 -331.456c0,-63.9651 52.3351,-116.3 116.3,-116.3zm0 -1829.77l912.956 0c63.9651,0 116.3,52.3351 116.3,116.3l0 331.456c0,63.9651 -52.3351,116.3 -116.3,116.3l-912.956 0c-63.9651,0 -116.3,-52.3351 -116.3,-116.3l0 -331.456c0,-63.9651 52.3351,-116.3 116.3,-116.3zm-1286.82 1254.06l479.833 -360.61 479.833 -360.603 0.00354286 721.217 -0.00354286 721.211 -479.833 -360.604 -479.833 -360.612z"/>
 </g>
</svg>
""")
ICONE_PRIMEIRO=XML("""
<svg class="botao_paginacao" xmlns="http://www.w3.org/2000/svg" xml:space="preserve" width="2480px" height="2480px" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd"
viewBox="0 0 2480 2480"
 xmlns:xlink="http://www.w3.org/1999/xlink">
 <g>
  <path class="fil0" d="M223.546 1259.65l1110.19 -1110.19 212.106 212.105 -898.091 898.089 898.091 898.091 -212.106 212.105 -1110.19 -1110.2zm719.909 0l1110.19 -1110.19 212.106 212.105 -898.091 898.089 898.091 898.091 -212.106 212.105 -1110.19 -1110.2z"/>
 </g>
</svg>
""")
ICONE_PROXIMO=XML("""
<svg class="botao_paginacao" xmlns="http://www.w3.org/2000/svg" xml:space="preserve" width="2480px" height="2480px" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd"
viewBox="0 0 2480 2480"
 xmlns:xlink="http://www.w3.org/1999/xlink">
 <g>
  <polygon class="fil0" points="1910.45,1279.3 800.257,169.102 588.151,381.207 1486.24,1279.3 588.151,2177.39 800.257,2389.49 "/>
 </g>
</svg>
""")
ICONE_ANTERIOR=XML("""
<svg class="botao_paginacao" xmlns="http://www.w3.org/2000/svg" xml:space="preserve" width="2480px" height="2480px" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd"
viewBox="0 0 2480 2480"
 xmlns:xlink="http://www.w3.org/1999/xlink">
 <g>
  <polygon class="fil0" points="588.151,1279.3 1698.35,169.102 1910.45,381.207 1012.36,1279.3 1910.45,2177.39 1698.35,2389.49 "/>
 </g>
</svg>
""")
ICONE_ULTIMO=XML("""
<svg class="botao_paginacao" xmlns="http://www.w3.org/2000/svg" xml:space="preserve" width="2480px" height="2480px" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd"
viewBox="0 0 2480 2480"
 xmlns:xlink="http://www.w3.org/1999/xlink">
 <g>
  <path class="fil0" d="M2265.76 1259.65l-1110.19 -1110.19 -212.106 212.105 898.091 898.089 -898.091 898.091 212.106 212.105 1110.19 -1110.2zm-719.909 0l-1110.19 -1110.19 -212.106 212.105 898.091 898.089 -898.091 898.091 212.106 212.105 1110.19 -1110.2z"/>
 </g>
</svg>
""")
ICON_IR=XML("""
<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" width="2480px" height="2480px" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd"
viewBox="0 0 2480 2480"
 xmlns:xlink="http://www.w3.org/1999/xlink">
 <g>
  <path class="fil0" d="M159.329 106.073l2137 0 0 1634.18 -534.251 351.729 -534.249 351.729 -534.249 -351.729 -534.251 -351.729 0 -1634.18zm609.105 794.572c0,71.4618 2.09619,179.277 6.28621,323.133 3.84164,143.857 5.93665,251.672 5.93665,323.135 0,12.1178 -3.14251,19.8849 -9.08034,22.6814 -1.39589,0.621181 -10.4762,1.86354 -26.5395,3.72827 -44.3507,4.97181 -103.718,7.14594 -178.103,7.14594 -99.5283,0 -163.085,-2.17413 -190.325,-7.14594 -19.9061,-3.72827 -29.6832,-13.0495 -29.6832,-28.2744 0,9.63185 3.14133,-43.4992 9.07798,-160.013 12.224,-245.768 18.5091,-407.335 18.5091,-484.39 0,-64.9382 -2.44339,-162.5 -6.98415,-292.064 -4.88914,-129.875 -7.33371,-227.437 -7.33371,-292.374 0,-13.3601 8.03284,-19.8849 23.3982,-19.8849 21.302,0 53.0814,0.931771 95.6867,2.48472 42.6052,1.86472 74.733,2.7965 95.6855,2.7965 21.302,0 52.3835,-0.931771 93.5928,-2.7965 41.5554,-1.55295 72.6368,-2.48472 93.5905,-2.48472 19.905,0 29.6832,6.52476 29.6832,19.8849 0,64.937 -3.84164,162.499 -11.5237,292.374 -8.03166,129.563 -11.8745,227.125 -11.8745,292.064zm1428.31 663.667c0,4.03886 -6.98533,7.14594 -20.6029,9.01067 -25.844,3.72827 -91.1483,5.59299 -195.215,5.59299 -89.4005,0 -150.165,-1.86472 -182.294,-5.59299 -15.0158,-1.86472 -23.397,-3.41768 -25.492,-4.66004 -4.1912,-1.86472 -9.08034,-7.7683 -14.319,-18.0213 -10.1267,-23.6143 -25.1437,-59.0346 -45.0498,-105.64 -26.5395,-60.5876 -68.0973,-150.072 -125.02,-268.451 -12.2229,-23.9237 -40.509,-36.9733 -84.8597,-39.1486 20.6029,1.24236 -14.6674,1.86472 -105.117,1.86472 -10.4762,0 -15.3654,15.2237 -15.3654,46.2945 0,41.3239 4.19002,102.843 12.5712,184.87 8.73196,81.716 12.922,143.546 12.922,184.559 0,10.5648 -3.1437,16.4672 -9.07916,18.3319 -9.77829,0.621181 -19.2082,1.24236 -28.9865,1.86472 -40.1606,2.48472 -102.67,3.72827 -188.23,3.72827 -97.4321,0 -156.102,-1.86472 -176.007,-5.59299 -19.5566,-3.72827 -29.3349,-13.0495 -29.3349,-28.2744 0,-66.8018 3.49208,-167.471 10.4762,-302.006 7.33371,-134.846 10.8258,-235.826 10.8258,-303.248 0,-256.643 -6.28503,-457.049 -19.5554,-600.905l-1.0475 -12.7389c-0.350743,-10.253 10.1267,-17.0884 32.4774,-20.8178 22.0011,-3.72827 126.417,-7.45653 312.552,-10.8742 126.068,-2.4859 226.644,-3.72827 301.726,-3.72827 155.404,0 282.519,31.3814 380.652,93.8326 111.052,70.2194 166.577,172.131 166.577,304.803 0,88.5514 -14.3179,159.392 -42.9536,212.212 -28.6369,52.8193 -81.3676,104.087 -158.546,153.799 -15.7138,9.63185 -23.397,18.9531 -23.397,27.3426 0,-0.621181 41.5565,75.5018 124.671,228.369 83.465,152.867 125.022,237.379 125.022,253.225zm-429.89 -816.534c0,-74.2595 -27.2387,-125.526 -81.7184,-153.8 -42.2545,-22.0602 -108.607,-32.9344 -198.356,-32.9344 -64.9547,0 -99.5283,9.01067 -103.37,26.4096 -4.19002,20.8178 -6.28621,80.1619 -6.28621,178.345 0,13.9825 0.349562,34.7991 1.0475,62.1417 0.699124,27.0308 1.04869,47.5381 1.04869,60.8982 0,3.10709 10.8258,5.90358 32.8258,9.01067 41.5577,5.59181 85.2104,8.3883 130.958,8.3883 149.116,0 223.851,-52.8193 223.851,-158.459z"/>
 </g>
</svg>
""")
class PhanterSqlListas():
    url_ajax=URL(current.request.application, "plugin_phantersqllistas", 'echo_phantersqllistas')
    def __init__(self, db, nome_tabela, campo_padrao_pesquisa, filtro, campos=None, registro_por_pagina=50, pagina=1, url_ajax=url_ajax):
        self._db=db
        self._nome_tabela=nome_tabela
        self.id_phantersqllistas_container="phantersqllistas-main_%s" %nome_tabela
        self.id_phantersqllistas_avisos="phantersqllistas-avisos_%s" %nome_tabela
        self._campo_padrao_pesquisa=campo_padrao_pesquisa
        self._campos_db=db[nome_tabela].fields
        if campo_padrao_pesquisa in self._campos_db:
            self.campo_de_consulta=db[nome_tabela][campo_padrao_pesquisa].label
        else:
            self.campo_de_consulta=campo_padrao_pesquisa
        self._filtro=filtro
        self._campos=campos
        self._campo_ordenador="id"
        self._sentido="crescente"
        self._url_ajax=url_ajax
        self._modificar_campo_cabecalho={}
        self._modificar_campo_pesquisa={}
        self._modificar_campo_ordenador={}
        self._modificar_campo_dados={}
        self._modificar_linhas_dados=None
        self._links_menu=[]
        self._palavra=""
        self._numero_registros_por_pagina=registro_por_pagina
        self._pagina_atual=pagina
        self._numero_de_registros_no_banco=0
        if not self._campos:
            self._campos=self._campos_db
        self._dict_campos=self._define_dict_campos(self._campos)
        self._scripts=""
        self._avisos=""
        self._html_paginacao=""
        self._dict_API={}
        self._dict_API_menu={}
        self._campos_pesquisa=[]
        self._formato_data='%d/%m/%Y'
        self._formato_datahora='%d/%m/%Y %H:%M:%S'
        
    def setFormatoData(self, formato):
        self._formato_data=formado

    def setFormatoDataHora(self, formato):
        self._formato_datahora=formado

    def setAviso(self, frase):
        self._avisos=frase
        self._dict_API['avisos']=frase

    def setFiltroPadrao(self, filtro):
        self._filtro=filtro

    def setCampos(self, lista_campos):
        self._campos=lista_campos
        self._dict_campos=self._define_dict_campos(lista_campos)

    def setCamposPesquisa(self, lista_campos):
        self._campos_pesquisa=lista_campos

    def setAtributosCampo(self, campo, dict_atributos):
        if campo in self._campos:
            if isinstance(dict_atributos, dict):
                if "_class" in dict_atributos:
                    class_atual=dict_atributos['_class']
                    class_atual=" ".join([class_atual,"phantersqllistas-campo%s" %(" phantersqllistas-campo_db" if campo in self._campos_db else "")])
                    dict_atributos['_class']=class_atual
                    dict_atributos['_data-phantersqllistas-nome_campo']=campo
                    dict_atributos['_data-phantersqllistas-tabela']=self._nome_tabela
                self._dict_campos[campo]=dict_atributos
            else:
                raise Exception("Os atributos devem ser um dicionário")
        else:
            raise Exception("O campo especificado em setAtributosCampo não foi especificado em setCampo e nem no instancimanto da classe")

    def modificarCampoCabecalho(self, campo, valor):
        if campo in self._campos:
            self._modificar_campo_cabecalho[campo]=valor
        else:
            raise Exception("O campo especificado em modificarCampoCabecalho não foi especificado em setCampo e nem no instancimanto da classe")

    def modificarCampoPesquisa(self, campo, filtro):
        if campo in self._campos:
            self._modificar_campo_pesquisa[campo]=filtro
        else:
            raise Exception("O campo especificado em modificarCampoCabecalho não foi especificado em setCampo e nem no instancimanto da classe")


    def modificarCampoOrdenador(self, campo, ordenador):
        if campo in self._campos:
            self._modificar_campo_ordenador[campo]=ordenador
        else:
            raise Exception("O campo especificado em modificarCampoCabecalho não foi especificado em setCampo e nem no instancimanto da classe")


    def modificarCampoDados(self, campo, valor):
        if campo in self._campos:
            self._modificar_campo_dados[campo]=valor
        else:
            raise Exception("O campo especificado em modificarCampoDados não foi especificado em setCampo e nem no instancimanto da classe")

    def modificarLinhasDados(self, valor):
        pass

    def addMenuItem(self, link_or_lambda):
        self._links_menu.append(link_or_lambda)

    def setUrlAjax(self, url):
        self.url_ajax=url

    def echoHTML(self, campo_ordenador, sentido , campo_consulta , termo_procurado , numero_registros_por_pagina , pagina):
        self._campo_ordenador=campo_ordenador
        self._sentido=sentido
        self._campo_padrao_pesquisa=campo_consulta
        self._palavra=termo_procurado
        self._numero_registros_por_pagina=numero_registros_por_pagina
        self._pagina_atual=pagina
        self.campo_de_consulta=self._db[self._nome_tabela][self._campo_padrao_pesquisa].label
        return {"status":"OK", "tipo":"html", "dados":self._update().xml(), "parametros":{"campo_ordenador":campo_ordenador,  "sentido":sentido,  "campo_consulta":campo_consulta,  "termo_procurado":termo_procurado,  "numero_registros_por_pagina":numero_registros_por_pagina,  "pagina":pagina, }}

    def echoAPI(self, campo_ordenador, sentido, campo_consulta, termo_procurado, numero_registros_por_pagina, pagina):
        self._campo_ordenador=campo_ordenador
        self._sentido=sentido
        self._campo_padrao_pesquisa=campo_consulta
        self._palavra=termo_procurado
        self._numero_registros_por_pagina=numero_registros_por_pagina
        self._pagina_atual=pagina
        self.campo_de_consulta=self._db[self._nome_tabela][self._campo_padrao_pesquisa].label
        self._update()
        return {
        "status":"OK", 
        "tipo":"json", 
        "dados":self._dict_API, "avisos":self._avisos, "parametros":{"campo_ordenador":campo_ordenador,  "sentido":sentido,  "campo_consulta":campo_consulta,  "termo_procurado":termo_procurado,  "numero_registros_por_pagina":numero_registros_por_pagina,  "pagina":pagina, }}

    def _urlAjax(self):
        url=self.url_ajax
        table=self._db[self._nome_tabela]
        nome_tabela=self._nome_tabela
        campo_padrao_pesquisa=self._campo_padrao_pesquisa
        campos=self._campos
        campos_db=self._campos_db
        self._scripts+="""
            //Gerado automaticamente em Phantersqllistas
            function pesquisar(s){
                var botao_pesquisar=$("#phantersqllistas-%(nome_tabela)s_botao_pesquisar")
                var ordem=$(botao_pesquisar).attr("data-ordem");
                var sentido=$(botao_pesquisar).attr("data-sentido");
                var campo=$(botao_pesquisar).attr("data-campo");
                var num_registros=$(botao_pesquisar).attr("data-num_registros");
                var pagina=$(botao_pesquisar).attr("data-pagina");
                var palavra=$("#phantersqllistas-%(nome_tabela)s_input_pesquisar").val();
                if(palavra!=""){
                    $("#phantersqllistas-%(nome_tabela)s_progress").addClass("actived");
                }
                var url_ajax="%(url)s?ordem="+ordem+"&sentido="+sentido+"&campo="+campo+"&num_registros="+num_registros+"&pagina="+pagina+"&palavra="+palavra+"&tabela=%(nome_tabela)s"
                console.log(url_ajax);
                //ajax(url_ajax, [], ":eval");
                $.ajax({
                    url: url_ajax,
                    type: "POST",
                    processData: false,
                    contentType: false,
                    async: true,
                    success: function(response) {
                        if (response.status=="OK"){
                            if(response.tipo=='html'){
                                $("#phantersqllistas-main_%(nome_tabela)s").html(response.dados)
                            } else if (response.tipo=="json"){
                                $(".phantersqllistas-linha_dados_container").each(function(){
                                    $(this).remove();
                                })
                                var mapa_html_linha='<div class="list-group-item phantersqllistas-linha_dados_container"><div class="phantersqllistas-linha phantersqllistas-linha_dados row">§§dados_linha§§</div></div>'
                                var mapa_html_campo='<div§§atributos§§>§§dados§§</div>'
                                var mapa_html_menu='<div class="phantersqllistas-linha_menu_container dropleft"><div aria-expanded="false" aria-haspopup="true" class="phantersqllistas-linha_menu_botao dropdown-toggle" data-toggle="dropdown" id="phantersqllistas-linha_menu_botao_§§id§§"><div class="phantersqllistas-linha_menu_botao_svg"><i class="phantersqllitas-icone icone-menu"></i></div></div><div aria-labelledby="phantersqllistas-linha_menu_botao_§§id§§" class="dropdown-menu">§§links§§</div></div>'
                                var mapa_html_links='<div class="phantersqllistas-linha_menu_item_container">§§link§§</div>'
                                for(x=0; x<response.dados.ordem_linhas.length; x++){
                                    var html_campo=""
                                    var html_menu=""
                                    var id_linha=response.dados.ordem_linhas[x]
                                    var linha=response.dados.linhas[id_linha]
                                    html_menu=mapa_html_menu.replace("§§id§§", id_linha)
                                    for(y=0; y<linha.campos.length; y++){
                                        html_campo=html_campo+mapa_html_campo.replace("§§atributos§§", response.dados.atributos[y]).replace("§§dados§§", linha.campos[y]);
                                    }
                                    var html_links=""
                                    for (l=0; l<linha.menus.length; l++){
                                        var html_links=html_links+mapa_html_links.replace("§§link§§", linha.menus[l])
                                    }
                                    html_menu=html_menu.replace("§§links§§", html_links)
                                    var html=mapa_html_linha.replace("§§dados_linha§§", html_campo+html_menu)
                                    $("#phantersqllistas-lista_%(nome_tabela)s").append(html);
                                }
                                $("#phantersqllistas-%(nome_tabela)s_progress").removeClass("actived");
                                $("#phantersqllistas-%(nome_tabela)s_progress_paginacao").removeClass("actived");
                                if(response.avisos!=""){
                                    $("#phantersqllistas-avisos_%(nome_tabela)s").html(response.avisos);
                                } else {
                                    $("#phantersqllistas-avisos_%(nome_tabela)s").html("");
                                }
                                $("#phantersqllistas-%(nome_tabela)s_paginacao_info").html("<div>"+response.dados.paginacao.info_paginas+"</div>");
                                $("#phantersqllistas-paginacao_%(nome_tabela)s_container").attr("data-numero_paginas", response.dados.paginacao.numero_paginas);
                                $("#phantersqllistas-paginacao_%(nome_tabela)s_container").attr("data-info_paginas", response.dados.paginacao.info_paginas);
                                $("#phantersqllistas-%(nome_tabela)s_input_paginacao").hide()
                                $("#phantersqllistas-%(nome_tabela)s_paginacao_info").show()
                                if(response.dados.paginacao.primeiro_registro=="ativo"){
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_primeiro_registro").removeClass("disabled");
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_primeiro_registro").addClass("actived");
                                } else {
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_primeiro_registro").addClass("disabled");
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_primeiro_registro").removeClass("actived");
                                }
                                if(response.dados.paginacao.registro_anterior=="ativo"){
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_registro_anterior").removeClass("disabled");
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_registro_anterior").addClass("actived");
                                } else {
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_registro_anterior").addClass("disabled");
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_registro_anterior").removeClass("actived");
                                }
                                if(response.dados.paginacao.proximo_registro=="ativo"){
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_proximo_registro").removeClass("disabled");
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_proximo_registro").addClass("actived");
                                } else {
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_proximo_registro").addClass("disabled");
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_proximo_registro").removeClass("actived");
                                }
                                if(response.dados.paginacao.ultimo_registro=="ativo"){
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_ultimo_registro").removeClass("disabled");
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_ultimo_registro").addClass("actived");
                                } else {
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_ultimo_registro").addClass("disabled");
                                    $("#phantersqllistas-%(nome_tabela)s_paginacao_ultimo_registro").removeClass("actived");
                                }
                                update_icones();

                            } else {
                                console.log("Há algum erro");
                            }
                        } else {
                            console.log(response.error);
                        }
                    },
                    error: function(jqXHR, textStatus, errorMessage) {
                       console.log(errorMessage);
                    }
                });
            };
            $("#phantersqllistas-%(nome_tabela)s_select_campo_pesquisar").on("change", function(){
                $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-campo", $(this).val())
                var valor_place=$("#phantersqllistas-%(nome_tabela)s_select_campo_pesquisar option:selected").text();
                $("#phantersqllistas-%(nome_tabela)s_input_pesquisar").attr("placeholder", "Pesquisar em "+valor_place)
            });            
            $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").on("click", function(){
                $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-pagina", 1);
                pesquisar();
            });
            $("#phantersqllistas-%(nome_tabela)s_input_pesquisar").on("keyup", function(event){
                    $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-pagina", 1);
                  event.preventDefault();
                  if (event.keyCode === 13) {
                    pesquisar();
                  }
            });
            $(".phantersqllistas-campo_db[data-phantersqllistas-tabela='%(nome_tabela)s']").on("click", function(){
                $("#phantersqllistas-%(nome_tabela)s_progress").addClass("actived");
                var sentido=$("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-sentido");
                var campo_ordenador=$("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-ordem");
                var este_campo=$(this).attr("data-phantersqllistas-nome_campo")
                console.log(este_campo);
                console.log(campo_ordenador);
                console.log(sentido);
                $(".phantersqllistas-campo_db[data-phantersqllistas-tabela='%(nome_tabela)s']").each(function(){
                    $(".phantersqllistas-icone_sentido").each(function(){
                        $(this).remove();
                    });
                });
                $(this).append('<i class="phantersqllistas-icone_sentido phantersqllistas-icone"></i>');
                update_icones();
                if (este_campo==campo_ordenador){
                    if(sentido=="crescente"){
                        $(".phantersqllistas-icone_sentido").removeClass("icone-up");
                        $(".phantersqllistas-icone_sentido").addClass("icone-down");

                        $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-sentido", "decrescente");
                    } else {
                        $(".phantersqllistas-icone_sentido").removeClass("icone-down");
                        $(".phantersqllistas-icone_sentido").addClass("icone-up");
                        $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-sentido", "crescente");
                    }
                    $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-pagina", 1);
                    pesquisar();
                } else{
                    $(".phantersqllistas-icone_sentido").removeClass("icone-down");
                    $(".phantersqllistas-icone_sentido").addClass("icone-up");
                    $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-ordem", este_campo);
                    $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-pagina", 1);
                    $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-sentido", "crescente");
                    pesquisar();
                }
                update_icones();
            });
        """ %dict(url=url, nome_tabela=nome_tabela)
        attr={"_id":"phantersqllistas-%s_input_pesquisar" %nome_tabela,
            "_type":"text",
            "_class":"form-control",
            "_placeholder":"Pesquisar em %s" %(table[campo_padrao_pesquisa].label if campo_padrao_pesquisa in self._campos_db else campo_padrao_pesquisa),
            "_aria-label":"Pesquisar...",
            "_aria-describedby":"basic-addon2",
            "_autocomplete":"off"}
        attr2={"_id":"phantersqllistas-%s_botao_pesquisar" %nome_tabela,
                "_class":"input-group-append phantersqllistas-botao_pesquisar",
                "_data-ordem":"id",
                "_data-sentido":"crescente",
                "_data-campo":campo_padrao_pesquisa,
                "_data-num_registros":self._numero_registros_por_pagina,
                "_data-pagina":1
                }
        html_select=SELECT(_autocomplete="off", _class="form-control", _id="phantersqllistas-%s_select_campo_pesquisar" %nome_tabela)
        tem_select=False
        if not self._campos_pesquisa:
            self._campos_pesquisa=campos
        attr2['_data-campos_pesquisa']=str(self._campos_pesquisa)
        for f in self._campos_pesquisa:
            if f in campos_db and self._db[self._nome_tabela][f].type=="string":
                tem_select=True
                html_select.append(OPTION(table[f].label , _value=f, _selected='selected' if f==campo_padrao_pesquisa else None))
            elif f in self._modificar_campo_pesquisa.keys():
                tem_select=True
                html_select.append(OPTION(f , _value=f, _selected='selected' if f==campo_padrao_pesquisa else None))                

        if tem_select:
            html=CAT(
                DIV(
                    DIV(
                        DIV(
                            INPUT(**attr),
                            DIV(
                                SPAN("Pesquisar", _class="input-group-text", _id="basic-addon2"),
                            **attr2), 
                            _class="input-group mb-3"),
                        _class='col-8'),
                        DIV(
                    DIV(html_select,  _class="input-group") if tem_select else "",
                    _class='col-4'
                    ),
                _class='phantersqllistas-caixa_pesquisa row'))
            self.html_search=DIV(
                html, 
                DIV(DIV(
                    DIV(_class="indeterminate"),
                    _class='phantersqllistas-progress', _id="phantersqllistas-%s_progress" %self._nome_tabela), _class="phantersqllistas-progress_container_fixed"), 
                DIV(
                    DIV(self._avisos, _id=self.id_phantersqllistas_avisos, _class="phantersqllistas-avisos%s" %(" actived" if self._avisos else "")),
                    _class="col-12"),
                _class="phantersqllistas-pesquisa_container")
        else:
            self.html_search=""

    def _menuLinhas(self, row):
        
        if self._links_menu:
            links=self._links_menu
            self._dict_API['linhas'][row.id]['menus']=[]
            html_menu=DIV(_class="phantersqllistas-linha_menu_container dropleft")
            attrs={"_aria-expanded":"false",
            "_aria-haspopup":"true",
            "_class":"phantersqllistas-linha_menu_botao dropdown-toggle",
            "_data-toggle":"dropdown",
            "_id":"phantersqllistas-linha_menu_botao_%s" %row.id}
            attrs2={"_aria-labelledby": "phantersqllistas-linha_menu_botao_%s" %row.id, "_class":"dropdown-menu"}
            html_link_container=DIV(**attrs2)
            html_botao=DIV(DIV(I(_class="phantersqllistas-icone icone-menu"), _class="phantersqllistas-linha_menu_botao_svg"), **attrs)
            if isinstance(links, list):
                for x in links:
                    if isinstance(x, types.FunctionType):
                        html_link=DIV(x(row), _class="phantersqllistas-linha_menu_item_container")
                        self._dict_API['linhas'][row.id]['menus'].append(x(row))
                    else:
                        html_link=DIV(x, _class="phantersqllistas-linha_menu_item_container")
                        self._dict_API['linhas'][row.id]['menus'].append(x)
                    html_link_container.append(html_link)
            html_menu.append(CAT(html_botao, html_link_container))
            return html_menu
        else:
            return ""

    def _define_dict_campos(self, campos):
        dict_campos={}
        if isinstance(campos, str):
            campos=[campos]
        elif not isinstance(campos, list):
            raise Exception("campos deve ser uma lista")

        quant_campos=len(campos)
        largura=100/float(quant_campos)
        dict_campos['plugin_phantersqllistas_ordem_campos']=campos

        for x in campos:
            dict_campos[x]={"_class":"phantersqllistas-campo%s" %(" phantersqllistas-campo_db" if x in self._campos_db else ""), '_style':"width:%.3f%%" %largura}
            dict_campos[x]['_data-phantersqllistas-nome_campo']=x
            dict_campos[x]['_data-phantersqllistas-tabela']=self._nome_tabela
        return dict_campos

    def _linhaCabecalho(self):
        db=self._db
        nome_tabela=self._nome_tabela
        dict_campos=self._dict_campos
        campos_db=self._campos_db
        html=DIV(_class='phantersqllistas-linha phantersqllistas-linha_cabecalho row')
        for x in dict_campos['plugin_phantersqllistas_ordem_campos']:
            if x in self._modificar_campo_cabecalho:
                modificador=self._modificar_campo_cabecalho[x]
                if isinstance(modificador, types.FunctionType):
                    label=modificador(db[nome_tabela][x])
                else:
                    label=modificador
            else:
                if x in campos_db:
                    label=db[nome_tabela][x].label
                else:
                    label=x
            html.append(DIV(label, **dict_campos[x]))
        return DIV(html, _class='list-group-item phantersqllistas-linha_cabecalho')

    def _paginacao(self, pagina_atual, total_paginas, num_registros):
        attr_nav={'_aria-label':'...'}
        class_primeiros=""
        class_ultimos=""
        if pagina_atual==1:
            class_primeiros=" disabled"
        else:
            class_primeiros=" actived"
        if pagina_atual==total_paginas:
            class_ultimos=" disabled"
        else:
            class_ultimos=" actived"
        self._scripts+="""
            function apenas_numeros(string){
              var valores_aceitos=["0","1","2","3","4","5","6","7","8","9"]
              var string=string;
              var new_string="";
              for (var i = 0; i < string.length; i++) {
                if (valores_aceitos.includes(string[i])){
                  new_string+=string[i];
                };
              }
              return new_string;
            }
            $("#phantersqllistas-%(nome_tabela)s_paginacao_info").on("click", function(){
                $(this).hide();
                $("#phantersqllistas-%(nome_tabela)s_input_paginacao").show();
                $("#phantersqllistas-%(nome_tabela)s_input_paginacao input").focus()
            });
            $("#phantersqllistas-paginacao_%(nome_tabela)s_primeiro").on("click", function(){
                $("#phantersqllistas-%(nome_tabela)s_progress_paginacao").addClass("actived");

            });
            $("#phantersqllistas-paginacao_%(nome_tabela)s_botao_ir").on("click", function(){
                $("#phantersqllistas-%(nome_tabela)s_progress_paginacao").addClass("actived");
                var pagina=$("#phantersqllistas-%(nome_tabela)s_input_paginacao input").val();
                $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-pagina", pagina);
                $("#phantersqllistas-%(nome_tabela)s_input_paginacao input").val("")
                pesquisar();
            });
            $("#phantersqllistas-%(nome_tabela)s_input_paginacao input").on("keyup", function(event){
                var valor=$(this).val();
                var new_valor=parseInt(apenas_numeros(valor));
                if (new_valor>%(total_paginas)s){
                    $(this).val(%(total_paginas)s);
                } else if (new_valor<1){
                    $(this).val(1);
                } else{
                    $(this).val(new_valor);
                }
                event.preventDefault();
                if (event.keyCode === 13) {
                    $("#phantersqllistas-%(nome_tabela)s_progress_paginacao").addClass("actived");
                    var pagina=$("#phantersqllistas-%(nome_tabela)s_input_paginacao input").val();
                    $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-pagina", pagina);
                    $("#phantersqllistas-%(nome_tabela)s_input_paginacao input").val("")
                    pesquisar();
                }

            });
            $("#phantersqllistas-%(nome_tabela)s_paginacao_primeiro_registro").on("click", function(){
                if($(this).hasClass("actived")){

                    //var pagina_atual=$("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-pagina")
                    $("#phantersqllistas-%(nome_tabela)s_progress_paginacao").addClass("actived");
                    $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-pagina",1)
                    pesquisar();
                }
            })
            $("#phantersqllistas-%(nome_tabela)s_paginacao_registro_anterior").on("click", function(){
                if($(this).hasClass("actived")){
                    var pagina_atual=$("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-pagina")
                    $("#phantersqllistas-%(nome_tabela)s_progress_paginacao").addClass("actived");
                    $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-pagina",parseInt(pagina_atual)-1)
                    pesquisar();
                }
            })
            $("#phantersqllistas-%(nome_tabela)s_paginacao_proximo_registro").on("click", function(){
                if($(this).hasClass("actived")){
                    var pagina_atual=$("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-pagina")
                    $("#phantersqllistas-%(nome_tabela)s_progress_paginacao").addClass("actived");
                    $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-pagina",parseInt(pagina_atual)+1)
                    pesquisar();
                }
            })
            $("#phantersqllistas-%(nome_tabela)s_paginacao_ultimo_registro").on("click", function(){
                if($(this).hasClass("actived")){
                    var ultima=$("#phantersqllistas-paginacao_%(nome_tabela)s_container").attr("data-numero_paginas")
                    console.log(ultima)
                    $("#phantersqllistas-%(nome_tabela)s_progress_paginacao").addClass("actived");
                    $("#phantersqllistas-%(nome_tabela)s_botao_pesquisar").attr("data-pagina",ultima)
                    pesquisar();
                }
            })
            """ %dict(nome_tabela=self._nome_tabela, total_paginas=total_paginas)
        attr3={'_data-numero_paginas': total_paginas, 
        '_data-info_paginas': "Página %s de %s" %(pagina_atual, total_paginas),
        '_class':"phantersqllistas-paginacao_container",
        '_id':"phantersqllistas-paginacao_%s_container" %(self._nome_tabela)
        }
        html=DIV(
            DIV(
                DIV(
                    DIV(_class="indeterminate"),
                    _class='phantersqllistas-progress', _id="phantersqllistas-%s_progress_paginacao" %self._nome_tabela),
                 _class="phantersqllistas-progress_paginacao_container"),
            DIV(
                UL(
                    LI(DIV(ICONE_PRIMEIRO,_title="Primeiro", _class="page-link"), _class="page-item%s" %(class_primeiros), _id="phantersqllistas-%s_paginacao_primeiro_registro" %self._nome_tabela),
                    LI(DIV(ICONE_ANTERIOR,_title="Anterior", _class="page-link"),_class="page-item%s" %(class_primeiros), _id="phantersqllistas-%s_paginacao_registro_anterior" %self._nome_tabela),
                    LI(
                        DIV(
                            DIV("Página %s de %s" %(pagina_atual, total_paginas)), 
                            _class="page-link phantersqllistas-paginacao_info", _id="phantersqllistas-%s_paginacao_info" %self._nome_tabela),
                         DIV(
                            DIV(DIV(ICON_IR, _class="phantersqllistas-paginacao_botao_ir", _id="phantersqllistas-paginacao_%s_botao_ir" %self._nome_tabela), _class="phantersqllistas-paginacao_mudar_pagina"),
                            INPUT(_autocomplete="off", _class="form-control form-control-sm", _type="text", _placeholder="Página %s de %s" %(pagina_atual, total_paginas)),
                            _class="page-link phantersqllistas-input_paginacao", _id="phantersqllistas-%s_input_paginacao" %(self._nome_tabela)),
                        _class="page-item"),
                    LI(DIV(ICONE_PROXIMO,_title="Próximo", _class="page-link"),_class="page-item%s" %(class_ultimos), _id="phantersqllistas-%s_paginacao_proximo_registro" %self._nome_tabela),
                    LI(DIV(ICONE_ULTIMO,_title="Último", _class="page-link"), _class="page-item%s" %(class_ultimos), _id="phantersqllistas-%s_paginacao_ultimo_registro" %self._nome_tabela),
                    _class="pagination pagination-lg justify-content-center"),
            **attr_nav), **attr3)
        self._dict_API['paginacao']={"info_paginas": "Página %s de %s" %(pagina_atual, total_paginas), 'numero_paginas': total_paginas}
        self._dict_API['paginacao']['primeiro_registro']='ativo'
        self._dict_API['paginacao']['registro_anterior']='ativo'
        self._dict_API['paginacao']['proximo_registro']='ativo'
        self._dict_API['paginacao']['ultimo_registro']='ativo'
        if pagina_atual==1:
            self._dict_API['paginacao']['primeiro_registro']='inativo'
            self._dict_API['paginacao']['registro_anterior']='inativo' 
        if pagina_atual==total_paginas:
            self._dict_API['paginacao']['proximo_registro']='inativo'
            self._dict_API['paginacao']['ultimo_registro']='inativo'         


        return html

    def _linhasdados(self):
        db=self._db
        nome_tabela=self._nome_tabela
        dict_campos=self._dict_campos
        campos_db=self._campos_db
        filtro=self._filtro
        campos=dict_campos['plugin_phantersqllistas_ordem_campos']
        html_container=CAT()
        numero_registros_por_pagina=self._numero_registros_por_pagina
        pagina_atual=self._pagina_atual
        numero_de_registros_no_banco=self._numero_de_registros_no_banco
        inicio=(numero_registros_por_pagina*pagina_atual)-numero_registros_por_pagina
        fim=inicio+numero_registros_por_pagina
        selects2={'limitby': (inicio,fim)}
        if self._campo_ordenador in self._modificar_campo_ordenador:
            selects2['orderby']=self._modificar_campo_ordenador[self._campo_ordenador]
        else:
            selects2['orderby']=db[nome_tabela][self._campo_ordenador] if self._sentido=='crescente' else ~db[nome_tabela][self._campo_ordenador]
        if "id" in campos:
            selects=[db[nome_tabela][f] for f in campos if f in campos_db]
        else:
            selects=[db[nome_tabela].id]+[db[nome_tabela][f] for f in campos if f in campos_db]
        if self._palavra and self._campo_padrao_pesquisa in self._modificar_campo_pesquisa:
            query_modificada=self._modificar_campo_pesquisa[self._campo_padrao_pesquisa]
            query_final=db(query_modificada).selects(*selects, **selects2)
        elif self._palavra and db[nome_tabela][self._campo_padrao_pesquisa].type=="string":
            gerador1=[x.id for x in db(db[nome_tabela].id>0).select() if remover_acentos(self._palavra) in remover_acentos(x[self._campo_padrao_pesquisa])]
            gerador2=[x.id for x in db(db[nome_tabela].id.belongs(gerador1)).select() if remover_acentos(x[self._campo_padrao_pesquisa]).startswith(remover_acentos(self._palavra))]
            new_gerador=gerador2
            for z in gerador1:
                if not z in new_gerador:
                    new_gerador.append(z)

            filtro1=(db[nome_tabela].id.belongs(new_gerador))
            q_registros=db(filtro1)
            if self._campo_ordenador=="id" or self._campo_ordenador==self._campo_padrao_pesquisa:
                query_final=db(filtro1).select(*selects, **selects2).sort(lambda row: new_gerador.index(row.id))
            else:
                query_final=db(filtro1).select(*selects, **selects2)
        else:
            filtro=self._filtro
            q_registros=db(filtro)
            query_final=db(filtro).select(*selects, **selects2)
        numero_de_registros_no_banco=q_registros.count()
        pagina_a_mais=0
        if numero_de_registros_no_banco%numero_registros_por_pagina:
            pagina_a_mais=1
        quant_paginas=(numero_de_registros_no_banco/numero_registros_por_pagina)+pagina_a_mais

        self._html_paginacao=self._paginacao(pagina_atual, quant_paginas, numero_registros_por_pagina)
        self._dict_API['ordem_linhas']=[]
        self._dict_API['linhas']={}
        for y in query_final:
            html=DIV(_class='phantersqllistas-linha phantersqllistas-linha_dados row')
            self._dict_API['ordem_linhas'].append(y.id)
            self._dict_API['ordem_campos']=[]
            self._dict_API['atributos']=[]
            self._dict_API['linhas'][y.id]={'campos':[]}

            for x in campos:
                self._dict_API['ordem_campos'].append(x)
                if x in self._modificar_campo_dados:
                    modificador=self._modificar_campo_dados[x]

                    if isinstance(modificador, types.FunctionType):
                        dado=modificador(db[nome_tabela][y.id])
                        self._dict_API['linhas'][y.id]['campos'].append(str(dado))
                    else:
                        dado=modificador
                        self._dict_API['linhas'][y.id]['campos'].append(str(dado))
                else:
                    if x in campos_db:
                        if db[nome_tabela][x].type.startswith("reference"):
                            dado=db[nome_tabela][x].represent(y[x])
                            self._dict_API['linhas'][y.id]['campos'].append(str(dado))
                        elif db[nome_tabela][x].type=="date":
                            try:
                                dado=conv_date(y[x], self._formato_data)
                            except:
                                dado=""
                            self._dict_API['linhas'][y.id]['campos'].append(str(dado))
                        elif db[nome_tabela][x].type=="datetime":
                            try:
                                dado=conv_date(y[x], self._formato_data)
                            except:
                                dado=""
                            self._dict_API['linhas'][y.id]['campos'].append(str(dado))
                        else:
                            dado=y[x]
                            self._dict_API['linhas'][y.id]['campos'].append(str(dado))
                    else:
                        dado=x
                        self._dict_API['linhas'][y.id]['campos'].append(str(dado))
                attributos_api=""
                for at in dict_campos[x]:
                    if at.startswith("_"):
                        attributos_api=" ".join([attributos_api, "=".join([at[1:], dict_campos[x][at]])])
                self._dict_API['atributos'].append(attributos_api)
                html.append(DIV(dado, **dict_campos[x]))
            html_container.append(DIV(html, self._menuLinhas(y), _class='list-group-item phantersqllistas-linha_dados_container'))
        return html_container

    def _update(self):
        campos=self._campos
        html_cabecalho=self._linhaCabecalho()
        html_linhas_dados=self._linhasdados()
        self._urlAjax()
        html=CAT(self.html_search,  DIV(html_cabecalho, html_linhas_dados,_class="list-group", _id='phantersqllistas-lista_%s' %self._nome_tabela), self._html_paginacao, SCRIPT(self._scripts))
        return html

    def xml(self):
        return "%s" %(DIV(self._update(), _id=self.id_phantersqllistas_container))
