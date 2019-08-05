import citi_lib
import copy
import requests
import json

url_citi = 'http://localhost'


def get_pamareter(name_project, name_version, name_context, name_parameter):

    parameter = citi_lib.get_parameter(name_project, name_version, name_context, name_parameter)

    if parameter['code'] != 200:
         print(json.dumps(parameter, indent=4, sort_keys=True))
         return []

    copy_param = copy.deepcopy(parameter['data'])

    #print(json.dumps(copy_param, indent=4, sort_keys=True))
    return copy_param



def copy_new_parameter(name_project, name_version, name_context, name_parameter, new_name_context, new_name_project = '', new_name_version = ''):

    name_project = str(name_project)
    name_version = str(name_version)
    name_context = str(name_context)
    name_parameter = str(name_parameter)
    new_name_project = str(new_name_project)
    new_name_version = str(new_name_version)
    new_name_context = str(new_name_context)

    copy_param = get_pamareter(name_project, name_version, name_context, name_parameter)

    if copy_param == []:
        return []

    new_name_parameter = name_parameter.replace(name_context, new_name_context, 1)

    copy_param['values'] = []

    if new_name_project == '' and new_name_version == '':

        data = {'type':copy_param['type'],'commentaire':copy_param['commentaire'], 'required':copy_param['required'],'default_value':copy_param['default_value'],'important':copy_param['important'],'values':copy_param['values']}
        response = requests.put(url_citi+'/projects/'+name_project+'/versions/'+name_version+'/contexts/'+new_name_context+'/parameters/'+new_name_parameter, json = data)
        array= response.text
        parameter = json.loads(array)

    elif new_name_project == '' and new_name_version != '':

        data= {'type':copy_param['type'],'commentaire':copy_param['commentaire'], 'required':copy_param['required'],'default_value':copy_param['default_value'],'important':copy_param['important'],'values':copy_param['values']}
        response = requests.put(url_citi+'/projects/'+name_project+'/versions/'+new_name_version+'/contexts/'+new_name_context+'/parameters/'+new_name_parameter, json=data)
        array= response.text
        parameter = json.loads(array)

    elif new_name_project != '' and new_name_version == '':

        data= {'type':copy_param['type'],'commentaire':copy_param['commentaire'], 'required':copy_param['required'],'default_value':copy_param['default_value'],'important':copy_param['important'],'values':copy_param['values']}
        response = requests.put(url_citi+'/projects/'+new_name_project+'/versions/'+name_version+'/contexts/'+new_name_context+'/parameters/'+new_name_parameter, json=data)
        array= response.text
        parameter = json.loads(array)

    elif new_name_project != '' and new_name_version != '':

        data= {'type':copy_param['type'],'commentaire':copy_param['commentaire'], 'required':copy_param['required'],'default_value':copy_param['default_value'],'important':copy_param['important'],'values':copy_param['values']}
        response = requests.put(url_citi+'/projects/'+new_name_project+'/versions/'+new_name_version+'/contexts/'+new_name_context+'/parameters/'+new_name_parameter, json=data)
        array= response.text
        parameter = json.loads(array)

    if parameter['code'] != 200:
        print(json.dumps(parameter, indent=4, sort_keys=True))
        return []

    #print(json.dumps(parameter, indent=4, sort_keys=True))
    return parameter
