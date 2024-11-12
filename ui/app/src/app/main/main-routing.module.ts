import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MainComponent } from './main.component';

export const routes: Routes = [
  {
    path: '', component: MainComponent,
    children: [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'about', loadChildren: () => import('./about/about.module').then(m => m.AboutModule) },
        { path: 'home', loadChildren: () => import('./home/home.module').then(m => m.HomeModule) },
        { path: 'settings', loadChildren: () => import('./settings/settings.module').then(m => m.SettingsModule) },
      
    
        { path: 'Appointment', loadChildren: () => import('./Appointment/Appointment.module').then(m => m.AppointmentModule) },
    
        { path: 'CareService', loadChildren: () => import('./CareService/CareService.module').then(m => m.CareServiceModule) },
    
        { path: 'Customer', loadChildren: () => import('./Customer/Customer.module').then(m => m.CustomerModule) },
    
        { path: 'Employee', loadChildren: () => import('./Employee/Employee.module').then(m => m.EmployeeModule) },
    
        { path: 'Order', loadChildren: () => import('./Order/Order.module').then(m => m.OrderModule) },
    
        { path: 'OrderDetail', loadChildren: () => import('./OrderDetail/OrderDetail.module').then(m => m.OrderDetailModule) },
    
        { path: 'Pet', loadChildren: () => import('./Pet/Pet.module').then(m => m.PetModule) },
    
        { path: 'Product', loadChildren: () => import('./Product/Product.module').then(m => m.ProductModule) },
    
        { path: 'SupplyOrder', loadChildren: () => import('./SupplyOrder/SupplyOrder.module').then(m => m.SupplyOrderModule) },
    
        { path: 'SupplyOrderDetail', loadChildren: () => import('./SupplyOrderDetail/SupplyOrderDetail.module').then(m => m.SupplyOrderDetailModule) },
    
        { path: 'Vendor', loadChildren: () => import('./Vendor/Vendor.module').then(m => m.VendorModule) },
    
        { path: 'VendorProduct', loadChildren: () => import('./VendorProduct/VendorProduct.module').then(m => m.VendorProductModule) },
    
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class MainRoutingModule { }