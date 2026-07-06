import { useState } from "react";
import { askQuestion } from "../services/api";
import toast from "react-hot-toast";

function QuestionSection() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question) {
      toast.error("Please enter a question.");
      return;
    }

    try {
      setLoading(true);

      const res = await askQuestion(question);

      console.log(res.data);

      setAnswer(res.data.answer);
      toast.success("Answer generated!");
    } catch (error) {
      console.error(error);
      toast.error("Failed to get answer.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-slate-900 p-6 rounded-2xl shadow-lg">
      <h2 className="text-2xl font-bold mb-4">
        Ask Questions (RAG)
      </h2>

      <textarea
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        className="w-full p-3 bg-slate-800 rounded-lg"
        rows="4"
        placeholder="Ask anything from your document..."
      />

      <button
        onClick={handleAsk}
        disabled={loading}
        className="mt-4 w-full bg-green-600 hover:bg-green-700 p-3 rounded-lg font-semibold"
      >
        {loading ? "Thinking..." : "Ask AI"}
      </button>

      {answer && (
        <div className="mt-6 p-4 bg-slate-800 rounded-lg">
          <h3 className="font-bold mb-2">Answer:</h3>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
}

export default QuestionSection;