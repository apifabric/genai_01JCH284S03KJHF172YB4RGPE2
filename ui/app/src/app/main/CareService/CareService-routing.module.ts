import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CareServiceHomeComponent } from './home/CareService-home.component';
import { CareServiceNewComponent } from './new/CareService-new.component';
import { CareServiceDetailComponent } from './detail/CareService-detail.component';

const routes: Routes = [
  {path: '', component: CareServiceHomeComponent},
  { path: 'new', component: CareServiceNewComponent },
  { path: ':id', component: CareServiceDetailComponent,
    data: {
      oPermission: {
        permissionId: 'CareService-detail-permissions'
      }
    }
  },{
    path: ':care_service_id/Appointment', loadChildren: () => import('../Appointment/Appointment.module').then(m => m.AppointmentModule),
    data: {
        oPermission: {
            permissionId: 'Appointment-detail-permissions'
        }
    }
}
];

export const CARESERVICE_MODULE_DECLARATIONS = [
    CareServiceHomeComponent,
    CareServiceNewComponent,
    CareServiceDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CareServiceRoutingModule { }