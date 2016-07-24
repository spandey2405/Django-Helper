import os
BASE_DIR = os.path.dirname(os.path.realpath(__file__)).split('src')[0]

CONF = {
  "Base_Dir": BASE_DIR,
  "Project_Dir": '/projects/',
  "Model_Dir": "models/",
  "Serializers_Dir":"serializers/",
  "Constants_File":"constants.py"
}
DEFAULT_MODEL_JSON_FILE =  BASE_DIR + '/conf_json/model.json'

DEFAULT_CLASS_FIELD = "char"

DEFAULT_INDENT      = " " * 4

CLASS_FIELDS = ['char','int','bigint','datetime','foreign','auto']

CLASS_CONFIG = {
    "auto": {
        "init_name": "models.AutoField",
        "attributes": [
            "unique",
            "primary"

        ],
        "default_conf": [
            "primary"
        ]
    },
    "char": {
        "init_name": "models.CharField",
        "attributes": [
            "max_length",
            "default",
            "unique",
            "editable",
            "primary"

        ],
        "default_conf": [
            "max_length=500",
            "default='NA'",
        ]
    },
    "int":{
        "init_name": "models.IntegerField",
        "attributes": [
            "default",
            "max_length",
            "unique",
            "primary"
        ],
        "default_conf":[
            "default=0"
        ]
    },
    "bigint":{
        "init_name": "models.BigIntegerField",
        "attributes": [
            "default",
            "max_length",
            "unique",
            "primary"
        ],
        "default_conf":[
            "default=0"
        ]
    },
    "datetime":{
        "init_name": "models.DateTimeField",
        "attributes": [
            "auto_now",
            "auto_created",
            "auto_now_add"
        ],
        "default_conf":[
            "auto_now"
        ]
    },
    "foreign":{
        "init_name":"models.ForeignKey",
        "attributes": [
            "model",
            "unqiue"
        ],
        "default_conf":False
    }
}