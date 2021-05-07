import json

from django.shortcuts import render

def index(request):
    keys = [
        'Shib-Application-ID',
        'Shib-Authentication-Instant',
        'Shib-Authentication-Method',
        'Shib-AuthnContext-Class', 
        'Shib-Handler', 
        'Shib-Identity-Provider', 
        'Shib-Session-ID', 
        'Shib-Session-Index', 
        'UMAPrimaryAccount', 
        'UMAemailService', 
        'UMAservices', 
        'affiliation', 
        'displayName', 
        'eppn', 
        'fcHomeInstitution', 
        'fcIdNumber', 
        'fcLogoutURL', 
        'fcMiddleName', 
        'givenName', 
        'mail', 
        'mailAlias', 
        'persistent-id', 
        'sn', 
        'transientId', 
        'uid', 
        'unscoped-affiliation'
    ]

    shib_dict = {key: request.META[key] for key in keys}
    json_pretty = json.dumps(shib_dict, sort_keys=True, indent=4)
    return render(request, "user.html", {'meta': json_pretty}) 
