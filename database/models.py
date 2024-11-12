# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 12, 2024 20:51:12
# Database: sqlite:////tmp/tmp.pI3sBqYhuT-01JCH284S03KJHF172YB4RGPE2/PetShop/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class CareService(SAFRSBaseX, Base):
    __tablename__ = 'care_service'
    _s_collection_name = 'CareService'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    duration = Column(Integer)
    price = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="care_service")



class Customer(SAFRSBaseX, Base):
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String)
    balance = Column(Integer)
    credit_limit = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")
    PetList : Mapped[List["Pet"]] = relationship(back_populates="owner")



class Employee(SAFRSBaseX, Base):
    __tablename__ = 'employee'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String)
    salary = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)



class Product(SAFRSBaseX, Base):
    __tablename__ = 'product'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String)
    price = Column(Integer)
    quantity_in_stock = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    VendorProductList : Mapped[List["VendorProduct"]] = relationship(back_populates="product")
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="product")
    SupplyOrderDetailList : Mapped[List["SupplyOrderDetail"]] = relationship(back_populates="product")



class Vendor(SAFRSBaseX, Base):
    __tablename__ = 'vendor'
    _s_collection_name = 'Vendor'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    SupplyOrderList : Mapped[List["SupplyOrder"]] = relationship(back_populates="vendor")
    VendorProductList : Mapped[List["VendorProduct"]] = relationship(back_populates="vendor")



class Order(SAFRSBaseX, Base):
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customer.id'))
    date_placed = Column(DateTime)
    amount_total = Column(Integer)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="order")



class Pet(SAFRSBaseX, Base):
    __tablename__ = 'pet'
    _s_collection_name = 'Pet'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String)
    age = Column(Integer)
    owner_id = Column(ForeignKey('customer.id'))

    # parent relationships (access parent)
    owner : Mapped["Customer"] = relationship(back_populates=("PetList"))

    # child relationships (access children)
    AppointmentList : Mapped[List["Appointment"]] = relationship(back_populates="pet")



class SupplyOrder(SAFRSBaseX, Base):
    __tablename__ = 'supply_order'
    _s_collection_name = 'SupplyOrder'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    vendor_id = Column(ForeignKey('vendor.id'))
    date_ordered = Column(DateTime)
    total_amount = Column(Integer)

    # parent relationships (access parent)
    vendor : Mapped["Vendor"] = relationship(back_populates=("SupplyOrderList"))

    # child relationships (access children)
    SupplyOrderDetailList : Mapped[List["SupplyOrderDetail"]] = relationship(back_populates="supply_order")



class VendorProduct(SAFRSBaseX, Base):
    __tablename__ = 'vendor_product'
    _s_collection_name = 'VendorProduct'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    vendor_id = Column(ForeignKey('vendor.id'))
    product_id = Column(ForeignKey('product.id'))

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("VendorProductList"))
    vendor : Mapped["Vendor"] = relationship(back_populates=("VendorProductList"))

    # child relationships (access children)



class Appointment(SAFRSBaseX, Base):
    __tablename__ = 'appointment'
    _s_collection_name = 'Appointment'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    pet_id = Column(ForeignKey('pet.id'))
    care_service_id = Column(ForeignKey('care_service.id'))
    appointment_date = Column(DateTime)
    amount = Column(Integer)

    # parent relationships (access parent)
    care_service : Mapped["CareService"] = relationship(back_populates=("AppointmentList"))
    pet : Mapped["Pet"] = relationship(back_populates=("AppointmentList"))

    # child relationships (access children)



class OrderDetail(SAFRSBaseX, Base):
    __tablename__ = 'order_detail'
    _s_collection_name = 'OrderDetail'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'))
    product_id = Column(ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Integer, nullable=False)
    amount = Column(Integer)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderDetailList"))
    product : Mapped["Product"] = relationship(back_populates=("OrderDetailList"))

    # child relationships (access children)



class SupplyOrderDetail(SAFRSBaseX, Base):
    __tablename__ = 'supply_order_detail'
    _s_collection_name = 'SupplyOrderDetail'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    supply_order_id = Column(ForeignKey('supply_order.id'))
    product_id = Column(ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Integer, nullable=False)
    amount = Column(Integer)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("SupplyOrderDetailList"))
    supply_order : Mapped["SupplyOrder"] = relationship(back_populates=("SupplyOrderDetailList"))

    # child relationships (access children)
