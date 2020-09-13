import axios from "axios";

export default axios.create({
  baseURL: "http://54.180.109.57:3001/api",
  headers: {    "Content-type": "application/json"
  }
});