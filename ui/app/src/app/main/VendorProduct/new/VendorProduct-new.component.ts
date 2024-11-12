import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'VendorProduct-new',
  templateUrl: './VendorProduct-new.component.html',
  styleUrls: ['./VendorProduct-new.component.scss']
})
export class VendorProductNewComponent {
  @ViewChild("VendorProductForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}