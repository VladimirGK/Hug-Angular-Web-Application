import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DownServicesComponent } from './down-services.component';

describe('DownServicesComponent', () => {
  let component: DownServicesComponent;
  let fixture: ComponentFixture<DownServicesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DownServicesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DownServicesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
