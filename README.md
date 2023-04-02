# automation_infrastructure_prototype
## install
install the packages of the product_application
```
pip install .
```
## product_application
#### MVC pattern controller, model, data.
### model
will have hierarchy of generic applications such as
```
product_application/
├─ controller/
│  ├─ AppRun.py
│  ├─ AutoVersion.py
│  ├─ AppsController.py
│  ├─ VersionController.py
├─ model/
│  ├─ applications/
│  │  ├─ app.py
│  │  ├─ ApplicationBaseClass.py
│  │  ├─ BmwClass.py
│  │  ├─ MercedesClass.py
│  │  ├─ SuzukiClass.py
│  │  ├─ ToyotaClass.py
```
as we can see the applications are generic applications that inherit from ApplicationBaseClass.py
the Applications could be BMW, MERCEDES, SUZUKI, TOYOTA, and maybe more in the future.

the execute of creating an app is app.py that will give us the service of executing the desired
application generic.

### controller
control the model, gives us services that creating application through the user input.
eventually will execute the driver `AutoVersion.py` with the application as `cmd` arguments.

it will generate the apps versions such as:
```commandline
python AutoVersion.py BMW MERCEDES SUZUKI
```
and the output comes to be:
```commandline
BMW  generated by VersionController 0
Mercedes version  generated by VersionController 0
Suzuki() generated by VersionController 0
```

## testing_infra
#### MVC pattern controller, model, data.
### model
### controller
### data