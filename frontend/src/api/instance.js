import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000',
});

const get = (path, request = null) => {
  return new Promise((resolve, reject) => {
    instance
      .get(path, request)
      .then(({ data }) => resolve(data))
      .catch((e) => reject(e));
  });
};

export { get };
