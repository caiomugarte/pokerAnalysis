import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  constructor(private httpClient: HttpClient) { }
  url = "/api/rest/pokerstars"

  getData(): Observable<any> {
    return this.httpClient.get(this.url)
  }
}
