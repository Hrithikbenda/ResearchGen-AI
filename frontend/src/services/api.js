import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

// Upload PDF
export const uploadPDF = (formData) =>
  API.post("/upload", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

// Ask Question (RAG)
export const askQuestion = (question) =>
  API.post("/ask", {
    question,
  });

// Generate Summary
export const generateSummary = (question) =>
  API.post("/summary", {
    question,
  });

// Generate Report
export const generateReport = (question) =>
  API.post("/report", {
    question,
  });

export default API;