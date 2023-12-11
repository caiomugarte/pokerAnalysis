import { Component, OnInit } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  standalone: true
})
export class AppComponent implements OnInit {
  title = 'frontend-poker-analysis';
  data: any;

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.loadData();
  }

  loadData() {
    // Chama o método do serviço para obter dados da API
    this.apiService.getData().subscribe({
      next: (data) => {
        this.data = data
        console.log(this.data);
      },
      error: (error) => {
        console.log(error)
      }
    }
    );
  }
}
