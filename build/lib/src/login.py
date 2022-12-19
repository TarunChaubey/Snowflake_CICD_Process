import json

credentials_dict = {}

credentials_dict['user'] = 'tarunchaubey55',
credentials_dict['password'] = 'Bhargav09@',
credentials_dict['account'] = 'fd05331.central-india.azure',
credentials_dict['warehouse'] = 'TEST_WAREHOUSES',
credentials_dict['database'] = 'CLASSIFICATION_DATASETES',
credentials_dict['schema'] = 'PUBLIC',
credentials_dict['role'] = 'ACCOUNTADMIN'

with open('./include/login.json','w') as lgjson:
    json.dump(credentials_dict,lgjson)