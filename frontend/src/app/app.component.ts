import { Component, OnInit } from '@angular/core';
import { AppService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  title = 'frontend';
  data :any;
  constructor(private appService: AppService){}

  ngOnInit(): void {
    this.appService.getData().subscribe({
      next: (response) => {
        console.log(response)
        this.data = response;
      },
      error: (err) => {
        console.log(err)
      }
    })
  }

}
