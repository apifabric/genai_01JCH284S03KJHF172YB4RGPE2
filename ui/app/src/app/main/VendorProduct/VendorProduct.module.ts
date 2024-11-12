import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {VENDORPRODUCT_MODULE_DECLARATIONS, VendorProductRoutingModule} from  './VendorProduct-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    VendorProductRoutingModule
  ],
  declarations: VENDORPRODUCT_MODULE_DECLARATIONS,
  exports: VENDORPRODUCT_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class VendorProductModule { }