import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PetHomeComponent } from './home/Pet-home.component';
import { PetNewComponent } from './new/Pet-new.component';
import { PetDetailComponent } from './detail/Pet-detail.component';

const routes: Routes = [
  {path: '', component: PetHomeComponent},
  { path: 'new', component: PetNewComponent },
  { path: ':id', component: PetDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Pet-detail-permissions'
      }
    }
  },{
    path: ':pet_id/Appointment', loadChildren: () => import('../Appointment/Appointment.module').then(m => m.AppointmentModule),
    data: {
        oPermission: {
            permissionId: 'Appointment-detail-permissions'
        }
    }
}
];

export const PET_MODULE_DECLARATIONS = [
    PetHomeComponent,
    PetNewComponent,
    PetDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PetRoutingModule { }