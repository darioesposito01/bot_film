import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "jksjksnknsdkjwjdk298398"

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'MasterUser'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '09c93304-ec98-4a71-ba1a-2449ae0581df'

    # Report Id for which Embed token needs to be generated
    REPORT_ID = '98ec2d4d-5af4-4613-9255-14442b3219e9'

    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '3493137b-5b4f-46cf-8833-c9113da132b8'

    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '3bd5da65-ffb1-46dc-b7c9-3fe3d908ed49'

    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'OKsO0Mv~l460.0YX4YWe6t.sMztZm~kBGj'

    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']

    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations'

    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = 'Mirko.esposito@ktmsrl.it'

    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = 'KTM_122017'
