from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))

    # Create CarModel instances with mock values for optional fields
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "fuel_efficiency": "27 MPG", "price": 34000.00, "image_url": "https://example.com/pathfinder.jpg"},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "fuel_efficiency": "30 MPG", "price": 28000.00, "image_url": "https://example.com/qashqai.jpg"},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "fuel_efficiency": "29 MPG", "price": 32000.00, "image_url": "https://example.com/xtrail.jpg"},
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "fuel_efficiency": "33 MPG", "price": 39000.00, "image_url": "https://example.com/a-class.jpg"},
        {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "fuel_efficiency": "31 MPG", "price": 42000.00, "image_url": "https://example.com/c-class.jpg"},
        {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "fuel_efficiency": "30 MPG", "price": 50000.00, "image_url": "https://example.com/e-class.jpg"},
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "fuel_efficiency": "28 MPG", "price": 38000.00, "image_url": "https://example.com/a4.jpg"},
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "fuel_efficiency": "29 MPG", "price": 41000.00, "image_url": "https://example.com/a5.jpg"},
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "fuel_efficiency": "27 MPG", "price": 46000.00, "image_url": "https://example.com/a6.jpg"},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3], "fuel_efficiency": "32 MPG", "price": 35000.00, "image_url": "https://example.com/sorrento.jpg"},
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances[3], "fuel_efficiency": "26 MPG", "price": 31000.00, "image_url": "https://example.com/carnival.jpg"},
        {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": car_make_instances[3], "fuel_efficiency": "34 MPG", "price": 22000.00, "image_url": "https://example.com/cerato.jpg"},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "fuel_efficiency": "35 MPG", "price": 23000.00, "image_url": "https://example.com/corolla.jpg"},
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "fuel_efficiency": "33 MPG", "price": 27000.00, "image_url": "https://example.com/camry.jpg"},
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances[4], "fuel_efficiency": "28 MPG", "price": 36000.00, "image_url": "https://example.com/kluger.jpg"},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            fuel_efficiency=data['fuel_efficiency'],
            price=data['price'],
            image_url=data['image_url']
        )
