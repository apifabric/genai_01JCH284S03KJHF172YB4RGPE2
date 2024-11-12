import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './SupplyOrder-card.component.html',
  styleUrls: ['./SupplyOrder-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.SupplyOrder-card]': 'true'
  }
})

export class SupplyOrderCardComponent {


}