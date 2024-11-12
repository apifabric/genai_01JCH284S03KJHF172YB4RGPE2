import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductHomeComponent } from './home/Product-home.component';
import { ProductNewComponent } from './new/Product-new.component';
import { ProductDetailComponent } from './detail/Product-detail.component';

const routes: Routes = [
  {path: '', component: ProductHomeComponent},
  { path: 'new', component: ProductNewComponent },
  { path: ':id', component: ProductDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Product-detail-permissions'
      }
    }
  },{
    path: ':product_id/OrderDetail', loadChildren: () => import('../OrderDetail/OrderDetail.module').then(m => m.OrderDetailModule),
    data: {
        oPermission: {
            permissionId: 'OrderDetail-detail-permissions'
        }
    }
},{
    path: ':product_id/SupplyOrderDetail', loadChildren: () => import('../SupplyOrderDetail/SupplyOrderDetail.module').then(m => m.SupplyOrderDetailModule),
    data: {
        oPermission: {
            permissionId: 'SupplyOrderDetail-detail-permissions'
        }
    }
},{
    path: ':product_id/VendorProduct', loadChildren: () => import('../VendorProduct/VendorProduct.module').then(m => m.VendorProductModule),
    data: {
        oPermission: {
            permissionId: 'VendorProduct-detail-permissions'
        }
    }
}
];

export const PRODUCT_MODULE_DECLARATIONS = [
    ProductHomeComponent,
    ProductNewComponent,
    ProductDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProductRoutingModule { }