import os

def get_app_directory():
    return os.getenv('APP_DIR', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'))

def get_config_file():
    return os.path.join(get_app_directory(), 'config.json')

def get_contest_directory():
    return os.path.join(get_app_directory(), 'contest')