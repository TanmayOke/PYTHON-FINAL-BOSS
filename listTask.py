#Automobile Industry usecase 
car_models=["Swift Desire","Mahendra Bolero","Maruti Alto","Audi","Toyota Fortuner","Honda Amaze"]

print("List of all availiable car models:-")
for i in car_models:
    print(i)

print("The first model:-",car_models[0])
print("The Last model:-",car_models[-1])

#print("The newly added model is:- ",car_models.append("Tata sumo"),car_models[-1])

car_models.sort()
print(car_models)

car_models.remove("Audi")
print(car_models)