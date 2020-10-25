import { Component, OnInit } from '@angular/core';
import { ConfigService } from '../config.service';
@Component({
  selector: 'app-recently-down',
  templateUrl: './recently-down.component.html',
  styleUrls: ['./recently-down.component.css']
})
export class RecentlyDownComponent implements OnInit {

  Period:any;
  response_json:any;

  constructor(
    private configService: ConfigService,
  ) { }

  ngOnInit(): void {

  }

  onSubmit() {
    var temp = +this.Period;
    this.configService.getRecentlyDownServices(temp).subscribe((data: JSON
      )=>{
        this.response_json = data;
      }
    )
  }

  isEmptyObject(obj) {
    return (obj && (Object.keys(obj).length === 0));
  }
}
