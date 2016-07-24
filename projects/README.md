# Django-Helper-Sample-Model-Serializer-Config

### Models

A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you're storing. Generally, each model maps to a single database table. The basics: Each model is a Python class that subclasses ```django.db.models.Model``` .

### Serializor

Django’s serialization framework provides a mechanism for “translating” Django models into other formats. Usually these other formats will be text-based and used for sending Django data over a wire, but it’s possible for a serializer to handle any format (text-based or not).

