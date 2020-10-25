import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FlappingScenariosComponent } from './flapping-scenarios.component';

describe('FlappingScenariosComponent', () => {
  let component: FlappingScenariosComponent;
  let fixture: ComponentFixture<FlappingScenariosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FlappingScenariosComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FlappingScenariosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
