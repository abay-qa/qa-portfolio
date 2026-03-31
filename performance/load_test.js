import http from 'k6/http';
import { check } from 'k6';

export let options = {
  vus: 10,
  duration: '10s',
};

export default function () {
  let response = http.get('https://jsonplaceholder.typicode.com/users/1');
  
  check(response, {
    'status is 200': (r) => r.status === 200,
  });
}