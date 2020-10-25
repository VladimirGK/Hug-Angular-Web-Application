import { Component, OnInit } from '@angular/core';
import { ConfigService } from '../config.service';

@Component({
  selector: 'app-flapping-scenarios',
  templateUrl: './flapping-scenarios.component.html',
  styleUrls: ['./flapping-scenarios.component.css']
})
export class FlappingScenariosComponent implements OnInit {

  response_json:any;

  constructor(
    private configService: ConfigService,
  ) { }

  ngOnInit(): void {
    this.configService.getFlappingScenarios().subscribe((data: JSON
      )=>{
        this.response_json = data;
      }
    )
  }
  
  isEmptyObject(obj) {
    return (obj && (Object.keys(obj).length === 0));
  }

}
