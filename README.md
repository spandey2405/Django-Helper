# Django-Helper

A General framework that automates the creation of model and serializer for a given configration. it also add model and serizalizer to your project is the project configration is added!

### Sample Model Configration Json

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you're storing. Generally, each model maps to a single database table. The basics: Each model is a Python class that subclasses ```django.db.models.Model``` .

Type of Keys ```ruby ["char","int","bigint","datetime","foreign","auto"] ```


```ruby

{
"model_name": "SampleModel",
"table_name": "sample_models",
"fields": [
    "id,auto",
    "user,char,max_length=500,default='NA'",
    "datetime",
    "type,char,default='referral'",
    "amount,int,default=0",
    "next_check,int,default=0",
    "check_count,int,default=0",
    "remark,char,max_length=500"
],
"app": "appname"
}


```