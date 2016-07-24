import json, os
from src.helpers.get_directory import MODEL_DIR, PROJECT_DIR
from config import CLASS_CONFIG, DEFAULT_CLASS_FIELD, CLASS_FIELDS, DEFAULT_INDENT, DEFAULT_MODEL_JSON_FILE

def CreateModel(name=False):
    with open(DEFAULT_MODEL_JSON_FILE) as data_file:
        data = json.load(data_file)
    if name:
        data = data[name]

    fields = data['fields']
    fields, primary_key = create_fields(fields=fields)
    path, filename, created = check_file_exists(model_class=data['model_name'])

    if created:
        data['model_name'] = filename.capitalize()
        data['table_name'] = filename

    model = make_class(
        class_name=data['model_name'],
        class_fields=fields,
        primary_key=primary_key,
        table_name=data['table_name'],
        app_name=data['app']

    )

    add_model_to_project(model=model, filename=filename)
    return filename

def create_fields(fields):
    fields_name = []
    fields_type = []
    fields_attr = []

    for field in fields:
        sub_content = field.replace(' ','').split(',')
        fields_name.append(sub_content[0])
        selected_type_field = get_field_type(sub_content)
        fields_type.append(selected_type_field)
        selected_field_attr, key_primary = get_fields_attributes(type_field=selected_type_field, sub_content=sub_content)
        if key_primary > 0:
            primary_key = sub_content[0]
        fields_attr.append(selected_field_attr)
    return make_field_line(name=fields_name, type=fields_type, attr=fields_attr), primary_key


def get_field_type(sub_content):
    field_type = [data for data in sub_content if data in CLASS_FIELDS]
    try:
        return field_type[0]
    except:
        return DEFAULT_CLASS_FIELD


def get_fields_attributes(type_field, sub_content):
    primary_key = 0
    attributes              = ''
    selected_field          = CLASS_CONFIG[type_field]
    selected_attributes     = selected_field['attributes']
    provided_attributes     = [data for data in sub_content if data in selected_attributes]
    if len(provided_attributes) <= 0:
        provided_attributes = selected_field['default_conf']

    for attr in provided_attributes:

        attr = attr.split('=')
        key = attr[0]
        try:
            value = attr[1]
        except:
            value = "True"
        if key == "primary" and value == "True":
            primary_key = 1
        attributes = attributes + '{0}={1}, '.format(key,value)
    attributes = "("+attributes[:-2]+")"

    return attributes, primary_key

def make_field_line(name, type, attr):
    max_space = (len(max(name, key=len)) + 1)
    total_fields = len(name)
    fields = ''
    for i in range(0,total_fields):
        space = ' ' * (max_space - len(name[i]))
        fields = fields + DEFAULT_INDENT + name[i] + space + " = " + CLASS_CONFIG[type[i]]['init_name'] + attr[i] + '\n'

    return fields


def make_class(class_name, class_fields, table_name, app_name, primary_key):
    class_data = '''from django.db import models

class {0}(models.Model):
{1}

    def is_authenticated(self):
        return True

    def save(self, *args, **kwargs):
        return super({0}, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.{4})

    class Meta:
        db_table = '{2}'
        app_label = '{3}'
    '''.format(
        class_name, class_fields, table_name, app_name, primary_key
    )

    return class_data

def add_model_to_project(model, filename):
    model_path = MODEL_DIR + filename + '.py'
    file = open(model_path, 'w')
    file.write(model)
    file.close()
    return True

def check_file_exists(model_class):
    created = False
    filename = model_class.lower()
    path = MODEL_DIR + '/' + filename + '.py'
    while os.path.isfile(path):
        filename = raw_input("File {} already exists please give a new name >> : ".format(filename))
        filename = filename.replace(' ','').replace('.py',' ')
        path = MODEL_DIR + '/' + filename + '.py'
        created = True
    return path, filename, created