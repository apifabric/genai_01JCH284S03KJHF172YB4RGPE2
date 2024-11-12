import { MenuRootItem } from 'ontimize-web-ngx';

import { AppointmentCardComponent } from './Appointment-card/Appointment-card.component';

import { CareServiceCardComponent } from './CareService-card/CareService-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderDetailCardComponent } from './OrderDetail-card/OrderDetail-card.component';

import { PetCardComponent } from './Pet-card/Pet-card.component';

import { ProductCardComponent } from './Product-card/Product-card.component';

import { SupplyOrderCardComponent } from './SupplyOrder-card/SupplyOrder-card.component';

import { SupplyOrderDetailCardComponent } from './SupplyOrderDetail-card/SupplyOrderDetail-card.component';

import { VendorCardComponent } from './Vendor-card/Vendor-card.component';

import { VendorProductCardComponent } from './VendorProduct-card/VendorProduct-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Appointment', name: 'APPOINTMENT', icon: 'view_list', route: '/main/Appointment' }
    
        ,{ id: 'CareService', name: 'CARESERVICE', icon: 'view_list', route: '/main/CareService' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderDetail', name: 'ORDERDETAIL', icon: 'view_list', route: '/main/OrderDetail' }
    
        ,{ id: 'Pet', name: 'PET', icon: 'view_list', route: '/main/Pet' }
    
        ,{ id: 'Product', name: 'PRODUCT', icon: 'view_list', route: '/main/Product' }
    
        ,{ id: 'SupplyOrder', name: 'SUPPLYORDER', icon: 'view_list', route: '/main/SupplyOrder' }
    
        ,{ id: 'SupplyOrderDetail', name: 'SUPPLYORDERDETAIL', icon: 'view_list', route: '/main/SupplyOrderDetail' }
    
        ,{ id: 'Vendor', name: 'VENDOR', icon: 'view_list', route: '/main/Vendor' }
    
        ,{ id: 'VendorProduct', name: 'VENDORPRODUCT', icon: 'view_list', route: '/main/VendorProduct' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AppointmentCardComponent

    ,CareServiceCardComponent

    ,CustomerCardComponent

    ,EmployeeCardComponent

    ,OrderCardComponent

    ,OrderDetailCardComponent

    ,PetCardComponent

    ,ProductCardComponent

    ,SupplyOrderCardComponent

    ,SupplyOrderDetailCardComponent

    ,VendorCardComponent

    ,VendorProductCardComponent

];