from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from ormconnector.create_food import CreateFood
from ormconnector.read_food import ReadFoods, ReadFood
from ormconnector.update_food import UpdateFoodAmount, UpdateFoodPrice, UpdateFoodVat
from ormconnector.delete_food import DeleteFood

app = FastAPI()


# Read table
@app.get("/foods", status_code=200)
async def read_foods():
    food = ReadFoods()
    return food.foods


# Read one food by id
@app.get("/foods/{food_id}", status_code=200)
async def read_food(food_id):
    food = ReadFood(food_id)
    return food.food


# Create row
@app.post("/foods", status_code=201)
async def create_food(id, name, amount, price, vat, category):
    new_food = CreateFood(id, name, amount, price, vat, category)
    return new_food.new_food


# Update amount
@app.put("/foods/{food_id}/amount", status_code=200)
async def update_food_amount(food_id, amount):
    update_food = UpdateFoodAmount(food_id, amount)
    return update_food.update_food


# Update price
@app.put("/foods/{food_id}/price", status_code=200)
async def update_food_price(food_id, price):
    update_food = UpdateFoodPrice(food_id, price)
    return update_food.update_food


# Update vat
@app.put("/foods/{food_id}/vat", status_code=200)
async def update_food_vat(food_id, vat):
    update_food = UpdateFoodVat(food_id, vat)
    return update_food.update_food


# Delete row
@app.delete("/foods/{food_id}", status_code=200)
async def delete_food(food_id):
    delete_food = DeleteFood(food_id)
    return jsonable_encoder({"food": "Food deleted successfully"})
