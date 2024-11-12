import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {SUPPLYORDERDETAIL_MODULE_DECLARATIONS, SupplyOrderDetailRoutingModule} from  './SupplyOrderDetail-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    SupplyOrderDetailRoutingModule
  ],
  declarations: SUPPLYORDERDETAIL_MODULE_DECLARATIONS,
  exports: SUPPLYORDERDETAIL_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class SupplyOrderDetailModule { }