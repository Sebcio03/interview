import axios from "axios";
import { API_URL } from "../commons/constans/env.js";

const baseAPI = axios.create({
  baseURL: API_URL + "api/",
  headers: { "Content-Type": "application/json" },
});

export default baseAPI;
