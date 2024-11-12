import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './CareService-card.component.html',
  styleUrls: ['./CareService-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.CareService-card]': 'true'
  }
})

export class CareServiceCardComponent {


}