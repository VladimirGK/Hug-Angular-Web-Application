import { Component, OnInit } from '@angular/core';
import { ConfigService } from '../config.service';
@Component({
  selector: 'app-add-outage',
  templateUrl: './add-outage.component.html',
  styleUrls: ['./add-outage.component.css']
})
export class AddOutageComponent implements OnInit {

  Service_ID:any;
  Duration:any;
  Start_time:any;

  constructor(
    private configService: ConfigService,
  ) { }

  ngOnInit(): void {
  }

  onSubmit() {
    var body ={'service_id': this.Service_ID, 'duration': this.Duration, 'startTime': this.Start_time};

    this.configService.addOutage(body).subscribe((data: JSON
      )=>{
        console.log(data);
      }
    )
  }

}
