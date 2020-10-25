import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddOutageComponent } from './add-outage.component';

describe('AddOutageComponent', () => {
  let component: AddOutageComponent;
  let fixture: ComponentFixture<AddOutageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddOutageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddOutageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
