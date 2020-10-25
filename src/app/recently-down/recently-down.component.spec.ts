import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RecentlyDownComponent } from './recently-down.component';

describe('RecentlyDownComponent', () => {
  let component: RecentlyDownComponent;
  let fixture: ComponentFixture<RecentlyDownComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RecentlyDownComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RecentlyDownComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
