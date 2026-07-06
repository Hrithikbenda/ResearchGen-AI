import { useState } from "react";
import { generateSummary } from "../services/api";

function SummarySection() {
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSummary = async () => {
    try {
      setLoading(true);

      const res = await generateSummary(
        "Generate summary of the uploaded PDF"
      );

      console.log(res.data);

      setSummary(
        res.data.summary ||
          res.data.result ||
          JSON.stringify(res.data, null, 2)
      );
    } catch (error) {
      console.log(error);
      setSummary("Failed to generate summary.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-slate-900 p-6 rounded-2xl shadow-lg">
      <h2 className="text-2xl font-bold mb-4">
        Generate Summary
      </h2>

      <button
        onClick={handleSummary}
        className="w-full bg-purple-600 hover:bg-purple-700 p-3 rounded-lg font-semibold"
      >
        {loading ? "Generating..." : "Generate Summary"}
      </button>

      {summary && (
        <div className="mt-6 bg-slate-800 p-4 rounded-lg">
          <h3 className="font-bold mb-2">Summary:</h3>

          <p className="whitespace-pre-wrap">
            {summary}
          </p>
        </div>
      )}
    </div>
  );
}

export default SummarySection;