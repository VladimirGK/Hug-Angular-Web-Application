import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AddOutageComponent } from './add-outage/add-outage.component';
import { DownServicesComponent } from './down-services/down-services.component';
import { FlappingScenariosComponent } from './flapping-scenarios/flapping-scenarios.component';
import { RecentlyDownComponent } from './recently-down/recently-down.component';

const routes: Routes = [
  { path: 'add_new_outage', component: AddOutageComponent },
  { path: 'currently_down_services', component: DownServicesComponent },
  { path: 'flapping_scenarios', component: FlappingScenariosComponent },
  { path: 'recently_down_services', component: RecentlyDownComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
