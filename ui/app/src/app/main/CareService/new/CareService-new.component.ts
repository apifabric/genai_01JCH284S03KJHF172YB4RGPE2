import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'CareService-new',
  templateUrl: './CareService-new.component.html',
  styleUrls: ['./CareService-new.component.scss']
})
export class CareServiceNewComponent {
  @ViewChild("CareServiceForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}