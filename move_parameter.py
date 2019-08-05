import citi_lib
import copy
import requests
import json
import copy_parameter


def move_param(name_project, name_version, name_context, name_parameter, new_name_context, new_name_project = '', new_name_version = ''):

    name_project = str(name_project)
    name_version = str(name_version)
    name_context = str(name_context)
    name_parameter = str(name_parameter)
    new_name_project = str(new_name_project)
    new_name_version = str(new_name_version)
    new_name_context = str(new_name_context)

    copy_parameter.copy_new_parameter(name_project, name_version, name_context,name_parameter, new_name_context, new_name_project = '', new_name_version = '')

    #print('parameter: ' , type(parameter))

    if parameter['code'] != 200:
        print(json.dumps(parameter, indent=4, sort_keys=True))
        return []

    else:
        parameter = citi_lib.delete_parameter_in_context(name_project,name_version,name_context,name_parameter)

    #print(json.dumps(parameter, indent=4, sort_keys=True))
    return parameter
