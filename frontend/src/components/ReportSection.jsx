import { useState } from "react";
import { generateReport } from "../services/api";

function ReportSection() {
  const [report, setReport] = useState("");
  const [loading, setLoading] = useState(false);

  const handleReport = async () => {
    try {
      setLoading(true);

      const res = await generateReport(
        "Generate detailed report of the uploaded PDF"
      );

      console.log(res.data);

      setReport(
        res.data.report ||
          res.data.result ||
          JSON.stringify(res.data, null, 2)
      );
    } catch (error) {
      console.log(error);
      setReport("Failed to generate report.");
    } finally {
      setLoading(false);
    }
  };

  const downloadReport = () => {
    const blob = new Blob([report], {
      type: "text/plain",
    });

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "Research_Report.txt";

    document.body.appendChild(a);
    a.click();

    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
  };

  return (
    <div className="bg-slate-900 p-6 rounded-2xl shadow-lg">
      <h2 className="text-2xl font-bold mb-4">
        Generate Research Report
      </h2>

      <button
        onClick={handleReport}
        className="w-full bg-orange-600 hover:bg-orange-700 p-3 rounded-lg font-semibold"
      >
        {loading
          ? "Generating AI Report..."
          : "Generate Report"}
      </button>

      {report && (
        <div className="mt-6 bg-slate-800 p-4 rounded-lg max-h-96 overflow-y-auto">
          <h3 className="font-bold mb-4 text-lg">
            Research Report:
          </h3>

          <p className="whitespace-pre-wrap">
            {report}
          </p>

          <button
            onClick={downloadReport}
            className="mt-6 bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-lg font-semibold"
          >
            Download Report
          </button>
        </div>
      )}
    </div>
  );
}

export default ReportSection;