import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'SupplyOrder-new',
  templateUrl: './SupplyOrder-new.component.html',
  styleUrls: ['./SupplyOrder-new.component.scss']
})
export class SupplyOrderNewComponent {
  @ViewChild("SupplyOrderForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}