import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {SUPPLYORDER_MODULE_DECLARATIONS, SupplyOrderRoutingModule} from  './SupplyOrder-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    SupplyOrderRoutingModule
  ],
  declarations: SUPPLYORDER_MODULE_DECLARATIONS,
  exports: SUPPLYORDER_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class SupplyOrderModule { }