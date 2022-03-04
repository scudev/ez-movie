import axios from "axios";

const apihost = "http://121.40.123.93:9092";
axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded";

export function post(action, params) {
  return new Promise((resolve, reject) => {
    const url = apihost + action;
    axios
      .post(url, params)
      .then((response) => {
        resolve(response.data);
      })
      .catch((error) => {
        reject(error);
      });
  });
}

export function get(action, params) {
  return new Promise((resolve, reject) => {
    axios
      .get(apihost + action, { params: params })
      .then((response) => {
        resolve(response.data);
      })
      .catch((error) => {
        reject(error);
      });
  });
}

export default {
  postData(action, params) {
    return post(action, params);
  },
  getData(action, params) {
    return get(action, params);
  }
};
