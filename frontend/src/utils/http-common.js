import axios from "axios"
export const API_BASE_URL = "//ec2-3-7-189-139.ap-south-1.compute.amazonaws.com/api/"

export const http = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json"
  }
})

export default http
