from decimal import Decimal
import json

class CreateMixin:
    def create(self, data):

        with open(self.file_name, 'r') as file:
            data1 = json.load(file)

        new_id = self.get_max_id(data1)
        self.data['id'] = new_id
        data1.append(self.data)

        with open(self.file_name, 'w') as file:
            json.dump(data1, file, indent=4)
            return f'Created new data: {data}.'
        
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
                index = data2.index(i)
                data2[index] = data
        

        with open(self.file_name, 'w') as file:
            json.dump(data2, file, indent=4)
            return f'Successfully updated: {data}.'



class DeleteMixin:
    def delete(self, id):
        with open('cars.json', 'r') as file:
            data = json.load(file)

        for i in data:
            if i['id'] == id:
                index = data.index(i)
                data.remove(data[index])
        
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)
            return f'Successfully Deleted.'

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


while True:

    def main():
        print('Привет, вам доступны следующие функции:\n\tPOST\n\tGET\n\tDETAIL\n\tPUT\n\tDELETE')
        method = input('Введите одну из функции: ').upper()
        car = Cars('Mars', 'Bans', 2003, 2.9, 'black', 'right', 777, 20000)
        if method == 'GET':
            print(car.listing())

        elif method == 'DETAIL':
            id = int(input('Введите id: '))
            print(car.retrieve(id))

        elif method == 'POST':
            brand = input('Введите марку: ')
            model = input('Введите модель: ')
            year = int(input('Введите год выпуска: '))
            engine = int(input('Введите объем двигателя: '))
            color = input('Введите цвет: ')
            body_type = input('Введите тип кузова: ')
            mileage = int(input('Введите пробег: '))
            price = int(input('Введите цену: '))
            data = {
            'brand': brand,
            'model': model,
            'year': year,
            'engine_capacity': engine,
            'color': color,
            'body_type': body_type,
            'mileage': mileage,
            'price': price
            }
            print(car.create(data))

        elif method == 'PUT':
            brand = input('Введите марку: ')
            model = input('Введите модель: ')
            year = int(input('Введите год выпуска: '))
            engine = int(input('Введите объем двигателя: '))
            color = input('Введите цвет: ')
            body_type = input('Введите тип кузова: ')
            mileage = int(input('Введите пробег: '))
            price = int(input('Введите цену: '))
            id = int(input('Введите id: '))
            data = {
            'id': id,
            'brand': brand,
            'model': model,
            'year': year,
            'engine_capacity': engine,
            'color': color,
            'body_type': body_type,
            'mileage': mileage,
            'price': price
            }
            print(car.update(data, id))

        elif method == 'DELETE':
            id = int(input('Введите id: '))
            print(car.delete(id))


    main()

