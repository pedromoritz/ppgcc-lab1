import http from 'k6/http';
import { sleep } from 'k6';
import { reportHTML } from "https://raw.githubusercontent.com/fziviello/k6-report-html/main/dist/reportHtml.min.js";

export const options = {
  stages: [
    { duration: '30s', target: 10 },
    { duration: '5m', target: 400 },
    { duration: '30s', target: 10 },
  ],
};

const API_BASE_URL = 'http://192.168.59.100';

export function handleSummary(data) {
  return {
    [`summary_${__ENV.SCHEDULER_TYPE}_${__ENV.POD_AMOUNT}.html`]: reportHTML(data, {title:`${__ENV.SCHEDULER_TYPE} - ${__ENV.POD_AMOUNT} pods`})
  };
}

export default function () {
  http.batch([
    ['GET', `${API_BASE_URL}:31001/memory/increase`],
    ['GET', `${API_BASE_URL}:31002/memory/increase`],
    ['GET', `${API_BASE_URL}:31003/memory/increase`]
  ]);

  sleep(1);
}
