import axios from "axios";

export default axios.create({
  baseURL: "http://127.0.0.1:9874/webhook",
  headers: {
    "Content-type": "application/json"
  }
});