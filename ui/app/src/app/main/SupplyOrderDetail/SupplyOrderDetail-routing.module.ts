import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SupplyOrderDetailHomeComponent } from './home/SupplyOrderDetail-home.component';
import { SupplyOrderDetailNewComponent } from './new/SupplyOrderDetail-new.component';
import { SupplyOrderDetailDetailComponent } from './detail/SupplyOrderDetail-detail.component';

const routes: Routes = [
  {path: '', component: SupplyOrderDetailHomeComponent},
  { path: 'new', component: SupplyOrderDetailNewComponent },
  { path: ':id', component: SupplyOrderDetailDetailComponent,
    data: {
      oPermission: {
        permissionId: 'SupplyOrderDetail-detail-permissions'
      }
    }
  }
];

export const SUPPLYORDERDETAIL_MODULE_DECLARATIONS = [
    SupplyOrderDetailHomeComponent,
    SupplyOrderDetailNewComponent,
    SupplyOrderDetailDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class SupplyOrderDetailRoutingModule { }