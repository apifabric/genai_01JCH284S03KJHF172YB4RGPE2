# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Customer(Base):
    __tablename__ = 'customer'
    """description: Customer details including their contact information and balance"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String)
    balance = Column(Integer, default=0)
    credit_limit = Column(Integer, default=5000)


class Employee(Base):
    __tablename__ = 'employee'
    """description: Employee details and associated pet shop operational roles"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    role = Column(String)
    salary = Column(Integer)


class Pet(Base):
    __tablename__ = 'pet'
    """description: Details of pets available or owned by customers"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String)
    age = Column(Integer)
    owner_id = Column(Integer, ForeignKey('customer.id'))


class Product(Base):
    __tablename__ = 'product'
    """description: Product offerings at the pet shop"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    category = Column(String)
    price = Column(Integer)
    quantity_in_stock = Column(Integer)


class Order(Base):
    __tablename__ = 'orders'
    """description: Orders placed by customers for pets or products"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    date_placed = Column(DateTime)
    amount_total = Column(Integer, default=0)


class OrderDetail(Base):
    __tablename__ = 'order_detail'
    """description: Details of individual line items within an order"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Integer, nullable=False)
    amount = Column(Integer, default=0)


class Vendor(Base):
    __tablename__ = 'vendor'
    """description: Vendors supplying products to the pet shop"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)


class VendorProduct(Base):
    __tablename__ = 'vendor_product'
    """description: Relationship between vendors and products they supply"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    vendor_id = Column(Integer, ForeignKey('vendor.id'))
    product_id = Column(Integer, ForeignKey('product.id'))


class CareService(Base):
    __tablename__ = 'care_service'
    """description: Pet care services offered at the shop"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    duration = Column(Integer)  # in minutes
    price = Column(Integer)


class Appointment(Base):
    __tablename__ = 'appointment'
    """description: Appointments for pet care services"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    pet_id = Column(Integer, ForeignKey('pet.id'))
    care_service_id = Column(Integer, ForeignKey('care_service.id'))
    appointment_date = Column(DateTime)
    amount = Column(Integer, default=0)


class SupplyOrder(Base):
    __tablename__ = 'supply_order'
    """description: Orders placed to vendors for supplying products"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    vendor_id = Column(Integer, ForeignKey('vendor.id'))
    date_ordered = Column(DateTime)
    total_amount = Column(Integer, default=0)


class SupplyOrderDetail(Base):
    __tablename__ = 'supply_order_detail'
    """description: Details of supplies ordered in each vendor order"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    supply_order_id = Column(Integer, ForeignKey('supply_order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Integer, nullable=False)
    amount = Column(Integer, default=0)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import date

# Create test data for Customer
customer1 = Customer(id=1, name="John Doe", email="john@example.com", phone="123-456-7890", balance=100, credit_limit=5000)
customer2 = Customer(id=2, name="Jane Smith", email="jane@example.com", phone="098-765-4321", balance=150, credit_limit=3000)
customer3 = Customer(id=3, name="Albert White", email="albert@example.com", phone="123-123-1234", balance=200, credit_limit=7000)
customer4 = Customer(id=4, name="Mary Jones", email="mary@example.com", phone="321-321-4321", balance=350, credit_limit=4000)

# Create test data for Employee
employee1 = Employee(id=1, name="Alice", role="Manager", salary=50000)
employee2 = Employee(id=2, name="Bob", role="Clerk", salary=30000)
employee3 = Employee(id=3, name="Charlie", role="Vet", salary=60000)
employee4 = Employee(id=4, name="Diana", role="Groomer", salary=40000)

# Create test data for Pet
pet1 = Pet(id=1, name="Fido", species="Dog", breed="Beagle", age=3, owner_id=1)
pet2 = Pet(id=2, name="Whiskers", species="Cat", breed="Siamese", age=2, owner_id=2)
pet3 = Pet(id=3, name="Goldie", species="Fish", breed="Goldfish", age=1, owner_id=3)
pet4 = Pet(id=4, name="Polly", species="Bird", breed="Parrot", age=4, owner_id=4)

# Create test data for Product
product1 = Product(id=1, name="Dog Food", category="Pet Food", price=20, quantity_in_stock=100)
product2 = Product(id=2, name="Cat Litter", category="Pet Supplies", price=12, quantity_in_stock=50)
product3 = Product(id=3, name="Aquarium", category="Pet Accessories", price=85, quantity_in_stock=20)
product4 = Product(id=4, name="Bird Cage", category="Pet Accessories", price=50, quantity_in_stock=15)

# Create test data for Order
order1 = Order(id=1, customer_id=1, date_placed=date(2023, 10, 5), amount_total=60)
order2 = Order(id=2, customer_id=2, date_placed=date(2023, 10, 6), amount_total=80)
order3 = Order(id=3, customer_id=3, date_placed=date(2023, 10, 7), amount_total=120)
order4 = Order(id=4, customer_id=4, date_placed=date(2023, 10, 8), amount_total=160)

# Create test data for OrderDetail
order_detail1 = OrderDetail(id=1, order_id=1, product_id=1, quantity=2, unit_price=20, amount=40)
order_detail2 = OrderDetail(id=2, order_id=2, product_id=2, quantity=3, unit_price=12, amount=36)
order_detail3 = OrderDetail(id=3, order_id=3, product_id=3, quantity=1, unit_price=85, amount=85)
order_detail4 = OrderDetail(id=4, order_id=4, product_id=4, quantity=2, unit_price=50, amount=100)

# Create test data for Vendor
vendor1 = Vendor(id=1, name="Pet Supplies Co.", contact_info="contact@petsupplies.com")
vendor2 = Vendor(id=2, name="Animal Essentials", contact_info="info@animalessentials.com")
vendor3 = Vendor(id=3, name="VetCare", contact_info="support@vetcare.com")
vendor4 = Vendor(id=4, name="Happy Pets", contact_info="service@happypets.com")

# Create test data for VendorProduct
vendor_product1 = VendorProduct(id=1, vendor_id=1, product_id=1)
vendor_product2 = VendorProduct(id=2, vendor_id=2, product_id=2)
vendor_product3 = VendorProduct(id=3, vendor_id=3, product_id=3)
vendor_product4 = VendorProduct(id=4, vendor_id=4, product_id=4)

# Create test data for CareService
care_service1 = CareService(id=1, name="Grooming", duration=60, price=30)
care_service2 = CareService(id=2, name="Vaccination", duration=15, price=20)
care_service3 = CareService(id=3, name="Training", duration=120, price=50)
care_service4 = CareService(id=4, name="Check-up", duration=20, price=40)

# Create test data for Appointment
appointment1 = Appointment(id=1, pet_id=1, care_service_id=1, appointment_date=date(2023, 10, 10), amount=30)
apppointment2 = Appointment(id=2, pet_id=2, care_service_id=2, appointment_date=date(2023, 10, 11), amount=20)
apppointment3 = Appointment(id=3, pet_id=3, care_service_id=3, appointment_date=date(2023, 10, 12), amount=50)
apppointment4 = Appointment(id=4, pet_id=4, care_service_id=4, appointment_date=date(2023, 10, 13), amount=40)

# Create test data for SupplyOrder
supply_order1 = SupplyOrder(id=1, vendor_id=1, date_ordered=date(2023, 9, 1), total_amount=1000)
supply_order2 = SupplyOrder(id=2, vendor_id=2, date_ordered=date(2023, 9, 5), total_amount=1500)
supply_order3 = SupplyOrder(id=3, vendor_id=3, date_ordered=date(2023, 9, 10), total_amount=2200)
supply_order4 = SupplyOrder(id=4, vendor_id=4, date_ordered=date(2023, 9, 15), total_amount=3000)

# Create test data for SupplyOrderDetail
supply_order_detail1 = SupplyOrderDetail(id=1, supply_order_id=1, product_id=1, quantity=50, unit_price=20, amount=1000)
supply_order_detail2 = SupplyOrderDetail(id=2, supply_order_id=2, product_id=2, quantity=125, unit_price=12, amount=1500)
supply_order_detail3 = SupplyOrderDetail(id=3, supply_order_id=3, product_id=3, quantity=20, unit_price=110, amount=2200)
supply_order_detail4 = SupplyOrderDetail(id=4, supply_order_id=4, product_id=4, quantity=60, unit_price=50, amount=3000)



session.add_all([customer1, customer2, customer3, customer4, employee1, employee2, employee3, employee4, pet1, pet2, pet3, pet4, product1, product2, product3, product4, order1, order2, order3, order4, order_detail1, order_detail2, order_detail3, order_detail4, vendor1, vendor2, vendor3, vendor4, vendor_product1, vendor_product2, vendor_product3, vendor_product4, care_service1, care_service2, care_service3, care_service4, appointment1, apppointment2, apppointment3, apppointment4, supply_order1, supply_order2, supply_order3, supply_order4, supply_order_detail1, supply_order_detail2, supply_order_detail3, supply_order_detail4])
session.commit()
