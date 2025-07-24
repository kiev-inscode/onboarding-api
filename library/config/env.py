import environ

env = environ.Env()

BASE_DIR = environ.Path(__file__) - 1
APPS_DIR = BASE_DIR.path("library")