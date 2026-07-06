# 🚀 ResearchGen AI
### Multi-Agent AI Research & Report Generation Platform

ResearchGen AI is an intelligent research assistant that leverages **Generative AI, Retrieval-Augmented Generation (RAG), and Multi-Agent Systems** to generate research reports, summarize documents, and answer questions from uploaded PDFs.

The platform allows users to securely upload documents, ask questions in natural language, generate summaries, and create AI-powered reports using advanced Large Language Models.

---

## 🌟 Features

### 🔐 Secure Authentication
- User Registration
- User Login
- JWT Authentication
- Protected API Endpoints
- Bearer Token Authorization

### 📄 PDF Processing
- Upload PDF documents
- Automatic document parsing
- PDF text extraction
- Support for multiple research documents

### 🧠 Retrieval-Augmented Generation (RAG)
- Document chunking and indexing
- Semantic search using vector embeddings
- Context-aware question answering
- AI responses grounded in uploaded documents

### 🤖 Multi-Agent AI System
ResearchGen AI uses multiple specialized AI agents:

#### 🔍 Research Agent
- Collects and analyzes information on a given topic.

#### 📝 Summary Agent
- Generates concise summaries from research content.

#### ✅ Verification Agent
- Validates and verifies generated information.

#### ✍️ Writer Agent
- Produces structured reports and final responses.

#### 🎯 Orchestrator Agent
- Coordinates all agents and manages the workflow.

### 📊 AI Report Generation
- Generate detailed reports on research topics
- Structured and organized content generation
- Automated report creation

### ❓ Intelligent Question Answering
- Ask questions from uploaded PDFs
- Context-aware responses
- Natural language interaction

### 🎨 Modern User Interface
- Responsive React frontend
- Clean and intuitive design
- Easy document upload and interaction

---

# 🏗️ System Architecture

```text
User
 │
 ▼
React Frontend
 │
 ▼
FastAPI Backend
 │
 ├── JWT Authentication
 ├── PDF Processing
 ├── Vector Database (FAISS)
 ├── RAG Pipeline
 └── Multi-Agent System
        │
        ├── Research Agent
        ├── Summary Agent
        ├── Verification Agent
        ├── Writer Agent
        └── Orchestrator
```

---

# 🛠️ Tech Stack

## Frontend
- React.js
- Vite
- JavaScript
- CSS

## Backend
- FastAPI
- Python
- Uvicorn

## Authentication
- JWT (JSON Web Tokens)
- Passlib (Bcrypt)

## Database
- SQLite
- SQLAlchemy ORM

## AI & RAG
- OpenRouter API
- FAISS Vector Database
- HuggingFace Embeddings
- Sentence Transformers
- LangChain

## PDF Processing
- PyPDF
- Python Multipart

---

# 📁 Project Structure

```text
ResearchGen-AI
│
├── backend
│   ├── app
│   │   ├── agents
│   │   ├── api
│   │   ├── auth
│   │   ├── database
│   │   ├── models
│   │   ├── schemas
│   │   ├── services
│   │   └── utils
│   ├── main.py
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
└── README.md
```

---

# 🔑 API Endpoints

## Authentication

### Register User
```http
POST /auth/register
```

### Login User
```http
POST /auth/login
```

---

## PDF Operations

### Upload PDF
```http
POST /upload
```

### Ask Questions
```http
POST /ask
```

### Generate Summary
```http
POST /summary
```

### Generate Report
```http
POST /report
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Hrithikbenda/ResearchGen-AI.git
cd ResearchGen-AI
```

---

## Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`

```env
OPENROUTER_API_KEY=your_api_key
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

Run Backend

```bash
uvicorn main:app --reload
```

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

# 🚀 Future Enhancements

- Multi-document search
- Chat history
- Downloadable reports (PDF/DOCX)
- User dashboard
- Research citations and references
- Cloud deployment
- Role-based access control
- Advanced analytics

---

# 📸 Screenshots

Add screenshots here:

- Login Page
- PDF Upload Page
- Question Answering
- Report Generation
- Summary Generation

---

# 👨‍💻 Author

**Hrithik Kumar Benda**

- LinkedIn: https://www.linkedin.com/in/hrithik-kumar-benda-583a35374
- GitHub: https://github.com/Hrithikbenda

---

# ⭐ If you found this project useful, please give it a star!
