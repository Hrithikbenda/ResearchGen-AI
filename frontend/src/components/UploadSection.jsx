import { useState } from "react";
import { FaFileUpload } from "react-icons/fa";
import { uploadPDF } from "../services/api";
import toast from "react-hot-toast";

function UploadSection() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      toast.error("Please select a PDF first.");
      return;
    }

    try {
      setLoading(true);

      const formData = new FormData();
      formData.append("file", file);

      const res = await uploadPDF(formData);

      toast.success("PDF uploaded successfully!");
      console.log(res.data);
    } catch (error) {
      console.error(error);
      toast.error("Upload failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-slate-900 p-6 rounded-2xl shadow-lg">
      <h2 className="text-2xl font-bold mb-4 flex items-center gap-2">
        <FaFileUpload />
        Upload PDF
      </h2>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
        className="w-full p-3 bg-slate-800 rounded-lg"
      />

      <button
        onClick={handleUpload}
        disabled={loading}
        className="mt-4 w-full bg-blue-600 hover:bg-blue-700 p-3 rounded-lg font-semibold"
      >
        {loading ? "Uploading..." : "Upload"}
      </button>
    </div>
  );
}

export default UploadSection;