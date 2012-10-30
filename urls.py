### URLS.PY (PROJETO)
    #LIST
    (r'^(?P<app_name>\w+)/(?P<model_name>\w+)/list.(?P<return_type>(json|xml))$', 'util.generic_views.generic_get_json_xml' ),
    #GET ONE
    (r'^(?P<app_name>\w+)/(?P<model_name>\w+)/(?P<instance_id>\d+).(?P<return_type>(json|xml))$', 'util.generic_views.generic_get_json_xml' ),
    #EDIT
    (r'^(?P<app_name>\w+)/(?P<model_name>\w+)/(?P<instance_id>\d+)/edit$', 'util.generic_views.generic_add_edit'),
    #DELETE
    (r'^(?P<app_name>\w+)/(?P<model_name>\w+)/(?P<instance_id>\d+)/delete$', 'util.generic_views.generic_delete'),
    #ADD
    (r'^(?P<app_name>\w+)/(?P<model_name>\w+)/add[/]{0,1}$', 'util.generic_views.generic_add_edit'),

### URLS.PY (APLICACAO)
	# personalizando
    (r'^aluno/list.(?P<return_type>(json|xml))$',           'util.generic_views.generic_get_json_xml', {
        'app_name': 'agenda',
        'model_name':'aluno',
        'extras':('is_presente_hoje','nome'),
        'excludes':('turma'),}),
