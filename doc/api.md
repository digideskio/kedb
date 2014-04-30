

# Billometer REST API

## GET /api/v1/

	HTTP 200 OK
	Vary: Accept Content-Type: text/html; charset=utf-8
	Allow: GET, HEAD, OPTIONS
	{
	    "groups": "http://localhost/api/v1/groups/", 
	    "users": "http://localhost/api/v1/users/", 
	    "billing-rates": "http://localhost/api/v1/billing-rates/"
	}

## Read more

* http://django-openstack-auth.readthedocs.org/en/latest/
* http://django-rest-framework.org/
* http://docs.openstack.org/developer/python-ceilometerclient/
