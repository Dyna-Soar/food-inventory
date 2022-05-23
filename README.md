# Food-Inventory API

## This is a food inventory api using FastAPI and sqlalchemy. This API let users create, read and update a supermarket inventory

### How to run the application
To create db and tables run: `python ormconnector/create_db.py`

To start a server run: `uvicorn main:app --reload`

### Endpoints
To review endpoints go to host:port/docs
- /foods/ to view all items
- /foods/ as a POST request, to add a new item in the inventory
- /foods/<id>/ to view a single item
- /foods/<id>/ as a DELETE request to delete an item
- /foods/<id>/amount/ as a PUT request to update the amount value of an item
- /foods/<id>/price/ as a PUT request to update the price value of an item
- /foods/<id>/vat/ as a PUT request to update the vat value of an item

