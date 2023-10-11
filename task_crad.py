from decimal import Decimal
import json

class CreateMixin:
    def create(self):

        with open(self.file_name, 'r') as file:
            data1 = json.load(file)

        new_id = self.get_max_id(data1)
        self.data['id'] = new_id
        data1.append(self.data)

        with open(self.file_name, 'w') as file:
            json.dump(data1, file, indent=4)
            return f'Created new data: {self.data}.'
        
    def get_max_id(self, data):
        if data:
            all_id = [int(i['id']) for i in data]
            return max(all_id) + 1
        return 0


class ListingMixin:
    def listing(self):
        with open('cars.json', 'r') as file:
            return json.load(file)


class RetrieveMixin:
    def retrieve(self, id):
        with open('cars.json', 'r') as file:
            data = json.load(file)
        for i in data:
            if i['id'] == id:
                return i
        else:
            return 'Wrong id!'
            
class UpdateMixin:
    def update(self, data, id):
        with open(self.file_name, 'r') as file:
            data2 = json.load(file)

        for i in data2:
            if i['id'] == id:
                continue
            else:
                pass

        data2[id] = data

        with open(self.file_name, 'w') as file:
            json.dump(data2, file, indent=4)
            return f'Successfully updated: {self.data}.'



class DeleteMixin:
    def delete(self, id):
        data = self.read(self.file_name)
        for i in data:
            if i.get('id') == id:
                data.remove(i)
        with open(self.file_name, 'w') as file:
            json.dump(data, file)

class Cars(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin):
    def __init__(self, brand, model, year, engine_capacity, color, body_type, mileage, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_capacity = Decimal(engine_capacity)
        self.color = color
        self.body_type = body_type
        self.mileage = mileage
        self.price = Decimal(price)

        self.data = {
            'id': 1,
            'brand': brand,
            'model': model,
            'year': year,
            'engine_capacity': engine_capacity,
            'color': color,
            'body_type': body_type,
            'mileage': mileage,
            'price': price
        }

        self.file_name = 'cars.json'



    
car = Cars('Mars', 'Bans', 2003, 2.9, 'black', 'right', 777, 20000)
# print(car.create())

# print(car.listing())

# print(car.retrieve(2))
kwargs = {
        "id": 2,
        "brand": "rui",
        "model": "Bans",
        "year": 2003,
        "engine_capacity": 2.9,
        "color": "black",
        "body_type": "right",
        "mileage": 777,
        "price": 20000
    }
print(car.update(kwargs, 2))
