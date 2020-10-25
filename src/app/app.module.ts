import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DownServicesComponent } from './down-services/down-services.component';
import { RecentlyDownComponent } from './recently-down/recently-down.component';
import { AddOutageComponent } from './add-outage/add-outage.component';
import { FlappingScenariosComponent } from './flapping-scenarios/flapping-scenarios.component';

import { HttpClientModule } from '@angular/common/http';
import { ConfigService } from './config.service';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    DownServicesComponent,
    RecentlyDownComponent,
    AddOutageComponent,
    FlappingScenariosComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [ConfigService],
  bootstrap: [AppComponent]
})
export class AppModule { }
