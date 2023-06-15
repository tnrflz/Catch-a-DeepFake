import axios from "axios";

const RequestService = axios.create({
    baseURL: "https://5eed-35-197-151-153.ngrok-free.app//api",
});

export default RequestService