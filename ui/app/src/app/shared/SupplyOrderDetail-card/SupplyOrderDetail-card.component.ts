import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './SupplyOrderDetail-card.component.html',
  styleUrls: ['./SupplyOrderDetail-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.SupplyOrderDetail-card]': 'true'
  }
})

export class SupplyOrderDetailCardComponent {


}