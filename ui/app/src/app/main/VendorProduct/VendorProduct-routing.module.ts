import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { VendorProductHomeComponent } from './home/VendorProduct-home.component';
import { VendorProductNewComponent } from './new/VendorProduct-new.component';
import { VendorProductDetailComponent } from './detail/VendorProduct-detail.component';

const routes: Routes = [
  {path: '', component: VendorProductHomeComponent},
  { path: 'new', component: VendorProductNewComponent },
  { path: ':id', component: VendorProductDetailComponent,
    data: {
      oPermission: {
        permissionId: 'VendorProduct-detail-permissions'
      }
    }
  }
];

export const VENDORPRODUCT_MODULE_DECLARATIONS = [
    VendorProductHomeComponent,
    VendorProductNewComponent,
    VendorProductDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class VendorProductRoutingModule { }