# IOTProject
reception ttn module


# using application manager client
app_client = handler.application()
my_app = app_client.get()
print(my_app)
my_devices = app_client.devices()
print(my_devices)

