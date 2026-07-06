import UploadSection from "./components/UploadSection";
import QuestionSection from "./components/QuestionSection";
import SummarySection from "./components/SummarySection";
import ReportSection from "./components/ReportSection";

function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-white p-10">
      <div className="max-w-7xl mx-auto">

        <h1 className="text-5xl font-bold text-center mb-3">
          Multi-Agent AI Research Platform
        </h1>

        <p className="text-center text-gray-400 mb-12">
          AI Powered Research • Summarization • Report Generation
        </p>

        <div className="grid md:grid-cols-2 gap-8">
          <UploadSection />
          <QuestionSection />
          <SummarySection />
          <ReportSection />
        </div>
      </div>
    </div>
  );
}

export default App;