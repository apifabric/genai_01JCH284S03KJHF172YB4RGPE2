import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Vendor-card.component.html',
  styleUrls: ['./Vendor-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Vendor-card]': 'true'
  }
})

export class VendorCardComponent {


}