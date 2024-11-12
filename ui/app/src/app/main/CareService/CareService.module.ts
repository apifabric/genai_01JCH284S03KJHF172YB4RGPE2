import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {CARESERVICE_MODULE_DECLARATIONS, CareServiceRoutingModule} from  './CareService-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    CareServiceRoutingModule
  ],
  declarations: CARESERVICE_MODULE_DECLARATIONS,
  exports: CARESERVICE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class CareServiceModule { }