# CRM

### Customer Relationship Management (CRM)

**Features**
- Customer relationship management (CRM). Handles relation between customer and store.
- Customer track there orders, can change there profile details(eg. name, profile photo)
- New Customer can create there account.
- admins or staff can change order status, search, delete specific orders. Can Add or remove new products

**How To Setup**

Create the virtual environment and activate it.
```
virtualenv venv

source venv/bin/activate
```
> [!NOTE]
> For windows user command can be:  ```.\venv\bin\activate```


Install all the dependecies:
```
pip install -r requirements.txt
```
> [!NOTE]
> We are using sqlite3 as a database too keep it simple, you can always change it by changing the **DATABASES** variable in the [./crm1/settings.py](./crm1/settings.py). Refer this link [django databses connections](https://docs.djangoproject.com/en/5.0/ref/databases/#databases)

We will migrate all the changes to database by doing.
```
./manage.py migrate
```


Now you are ready to run the project

You can start the server with:
```
.manage.py runserver
```