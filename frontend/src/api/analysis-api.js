import { get } from './instance';

export const getAnalysisData = (form) => {
  return get(`/min-max-profit?form=${form}`);
};
