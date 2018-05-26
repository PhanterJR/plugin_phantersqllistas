# -*- coding: utf-8 -*-

def index():
    #Exemplo de uso, observer que é necessário jquery, bootstrap 4 e suas dependências.
    conteudo_body=CAT()
    html=HTML(HEAD(LINK(_rel="stylesheet", _href=URL("static", "css", args=["bootstrap.min.css"])),
        LINK(_rel="stylesheet", _href=URL("static", "plugin_phantersqllistas", args=["css","plugin_phantersqllistas.css"])),
        TITLE("Phanter SQL LISTAS"),
        SCRIPT(_src=URL("static", "js", args=["jquery.js"]), _type="text/javascript"),
        ), BODY(DIV(conteudo_body, _class="container"), SCRIPT(_src=URL("static", "js", args=["popper.min.js"]), _type="text/javascript"), 
        SCRIPT(_src=URL("static", "js", args=["bootstrap.min.js"]), _type="text/javascript"),
        SCRIPT(_src=URL("static", "plugin_phantersqllistas", args=["js","phantersqllistas.js"]), _type="text/javascript")), doctype='html5')
    conteudo_body.append(MODELS_PHANTERSQLLISTAS)
    return html

def echo_phantersqllistas():
    #Exemplo da função que vai receber as requisições de ordenar, paginar, pesquisar na tabela e retornar um json.
    import json
    ordem=request.vars.ordem
    sentido=request.vars.sentido
    campo=request.vars.campo
    palavra=request.vars.palavra
    num_registros=int(request.vars.num_registros)
    tabela=request.vars.tabela
    pagina=int(request.vars.pagina)
    if palavra:
        frase="Pesquisando em \"%s\" por \"%s\"" %(db[tabela][campo].label, palavra)
        MODELS_PHANTERSQLLISTAS.setAviso(frase)
        api=MODELS_PHANTERSQLLISTAS.echoAPI(ordem, sentido , campo , palavra , num_registros , pagina)
        return response.json(api)
    else:
        frase=""
        MODELS_PHANTERSQLLISTAS.setAviso(frase)
        api=MODELS_PHANTERSQLLISTAS.echoAPI(ordem, sentido , campo , palavra , num_registros , pagina)
        return response.json(api)

