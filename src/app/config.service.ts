import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable()
export class ConfigService {

  URL_FLAPPING_SCENARIOS = 'http://localhost:8000/flapping_scenarios';
  URL_CURRENTLY_DOWN_SERVICES = 'http://localhost:8000/currently_down_services';
  URL_RECENTLY_DOWN_SERVICES = 'http://localhost:8000/recently_down_services?hours=';
  URL_ADD_OUTAGE = "http://localhost:8000/add_new_outage";
  constructor(private http: HttpClient) { }

  getFlappingScenarios() {
    return this.http.get(this.URL_FLAPPING_SCENARIOS);
  }

  getCurrentlyDownServices() {
    return this.http.get(this.URL_CURRENTLY_DOWN_SERVICES);
  }

  getRecentlyDownServices(period) {
    return this.http.get(this.URL_RECENTLY_DOWN_SERVICES + period);
  }

  addOutage(body) {
    return this.http.post(this.URL_ADD_OUTAGE, body);
  }

}
