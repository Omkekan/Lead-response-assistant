# AI Lead Response Assistant (LRA) --- Agentic Workflow

A safe, reliable AI-driven lead qualification system for home
maintenance enquiries.

------------------------------------------------------------------------

## 📖 Overview

The **Lead Response Assistant (LRA)** is an agentic workflow designed to
process incoming home maintenance enquiries with structured technical
triage.

Unlike generic conversational chatbots, this system functions as a
controlled diagnostic gatekeeper. It:

-   Identifies customer intent
-   Applies strict safety guardrails
-   Avoids diagnostic claims
-   Generates structured follow-up questions for structural engineers

The objective is not to provide conclusions --- but to qualify leads
safely and consistently.

------------------------------------------------------------------------

## ✨ Key Features

### Intent Identification

Automatically categorizes issues such as: - Damp patches - Structural
cracking - Water ingress - Roof leaks - Foundation concerns

### Zero-Hallucination Policy

-   No definitive diagnoses
-   No price estimates
-   No liability-inducing statements
-   No structural guarantees

### Client Triage Logic

Generates 3 structured follow-up questions to assess: - Location -
Severity - Duration - Environmental triggers

### Professional Tone

Maintains a calm, empathetic, technically responsible posture suitable
for: - Structural engineers - Property maintenance firms - Surveying
professionals

------------------------------------------------------------------------

## 🛠️ Architecture

The system uses: - Llama 3.3 - GitHub Inference API - Structured System
Prompt with logical gating

Workflow: 1. User submits maintenance enquiry 2. Intent classification
stage 3. Safety constraint enforcement 4. Follow-up question generation
5. Structured output returned

------------------------------------------------------------------------

## 🚀 Getting Started

### Prerequisites

-   Python 3.10+
-   GitHub Personal Access Token (PAT) with Models (read-only) access

### Installation

Clone the repository:

git clone https://github.com/yourusername/lead-response-assistant.git cd
lead-response-assistant

Install dependencies:

pip install requests

### Usage

Run the script:

python Project.py

Example input:

"Hi, I am getting damp patches on my bedroom wall after rains. What
should I do?"

------------------------------------------------------------------------

## ✅ Reliability & Safety

Safeguards include:

-   Negative Constraints enforced in the system prompt
-   Controlled Output Scope
-   No Fabrication Policy
-   No Commercial Claims

Safe Immediate Advice Examples: - Avoid painting over damp areas -
Monitor spread after rainfall - Check for obvious external leaks

------------------------------------------------------------------------

## 🔧 Known Limitations

-   Text-Only Processing (no image analysis)
-   No live weather integration
-   No building code database integration
-   No CRM integration

------------------------------------------------------------------------

## 🤝 Future Improvements

### RAG Integration

Connecting to structural engineering manuals and building pathology
references for grounded advice.

### Human-in-the-Loop

Engineer approval dashboard for reviewing and editing AI drafts.

### Multimodal Expansion

Image-based crack classification and moisture pattern analysis.

------------------------------------------------------------------------

## 📜 License

MIT License

------------------------------------------------------------------------

## 🧠 Philosophy

This system treats AI not as an expert replacement, but as a structured
triage assistant.

Safety \> Speed\
Qualification \> Diagnosis\
Clarity \> Speculation
