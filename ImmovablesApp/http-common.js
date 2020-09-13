import axios from "axios";

export default axios.create({
  baseURL: "http://54.180.144.184/api",
  headers: {    "Content-type": "application/json"
  }
});