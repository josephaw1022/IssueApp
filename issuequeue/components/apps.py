INSTALLED_APPS = [
    # Initial Apps 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd Party
    'corsheaders',
    'rest_framework',
    'dynamic_rest',
    "rest_framework_api_key",
    'django_filters',
    'rest_framework_word_filter',
    # My Apps
    'apps.api.account.apps.AccountConfig',
    'apps.api.bug.apps.BugConfig',
    'apps.api.root.apps.RootConfig',

]
