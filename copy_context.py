import citi_lib
import json
import requests
import copy



url_citi = 'http://localhost'


def get_context_parameters(name_project, name_version, name_context):

    project_version_context = citi_lib.get_context(name_project, name_version, name_context)

    if project_version_context['code'] != 200:
         print(json.dumps(project_version_context, indent=4, sort_keys=True))
         return []

    tab_parameters = copy.deepcopy(project_version_context['data'])

    #print(json.dumps(tab_parameters, indent=4, sort_keys=True))
    return tab_parameters



def copy_new_context(name_project, name_version, name_context, new_name_context):

    name_project = str(name_project)
    name_version = str(name_version)
    name_context = str(name_context)
    new_name_context = str(new_name_context)

    new_context = citi_lib.put_context(name_project, name_version, new_name_context)

    if new_context['code'] != 200:
         print(json.dumps(new_context, indent=4, sort_keys=True))
         return []

    cop_context = get_context_parameters(name_project, name_version, name_context)

    if cop_context == []:
        return []

    parameters = cop_context['parameters']

    for parameter in parameters:

        name_parameter = parameter['name']
        new_name_parameter = name_parameter.replace(name_context, new_name_context, 1)
        parameter['values'] = []

        response = requests.put(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/contexts/'+new_name_context+'/parameters/'+new_name_parameter, json = parameter)
        array= response.text
        parameter = json.loads(array)

    #print(json.dumps(new_context, indent=4, sort_keys=True))
    return new_context
