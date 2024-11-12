import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './VendorProduct-card.component.html',
  styleUrls: ['./VendorProduct-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.VendorProduct-card]': 'true'
  }
})

export class VendorProductCardComponent {


}