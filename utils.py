def get_querystring_as_dict_from_request(request):
    """
    Retorna um dicionario com os parametros(key) recebidos por querystring e seus valores(value)
    """
    kwargs = {}
    for k,v in request.GET.items():
        kwargs[str(k)] = str(v)

    return kwargs

def filter_model_from_querystring(query_set, request):
    """
    Se tiver algum parametro queryString
    eh usado como filter para o model
    #ex: ?prototipo__pk=24&localizacao__pk=396
    """
    kwargs = get_querystring_as_dict_from_request(request)
    if kwargs:
        query_set = query_set.filter(**kwargs)

    return query_set

def model_to_modelform(model):
    """
    Cria e Retorna a Classe ModelForm associada ao model passado.
    """
    meta = type('Meta', (), { "model":model, })
    modelform_class = type('modelform', (forms.ModelForm,), {"Meta": meta})
    return modelform_class