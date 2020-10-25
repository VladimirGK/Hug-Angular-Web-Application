import { Component, OnInit } from '@angular/core';
import { ConfigService } from '../config.service';
@Component({
  selector: 'app-down-services',
  templateUrl: './down-services.component.html',
  styleUrls: ['./down-services.component.css']
})
export class DownServicesComponent implements OnInit {

  response_json:any;

  constructor(
    private configService: ConfigService,
  ) { }

  ngOnInit(): void {
    this.configService.getCurrentlyDownServices().subscribe((data: JSON
      )=>{
        this.response_json = data;
      }
    )
  }

  isEmptyObject(obj) {
    return (obj && (Object.keys(obj).length === 0));
  }

}
