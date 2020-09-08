import axios from "axios";

export default axios.create({
  //baseURL: "http://13.125.30.205:3000/api",
  baseURL: "http://192.168.0.14:3000/api",
   //baseURL: "http://192.168.25.3:3000/api",
  headers: {    "Content-type": "application/json"
  }
});