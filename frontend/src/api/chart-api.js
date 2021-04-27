import { get } from './instance';

export const getChartData = (form) => {
  return get(`/chart-data?form=${form}`);
};
