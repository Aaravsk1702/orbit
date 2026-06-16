# Orbit

AI-powered multi-agent medical assessment system.

## Features

* PDF Report Analysis
* Medical Image Analysis
* Multi-Agent Workflow
* Diagnosis Agent
* Validation Agent
* Threshold-Based Review
* Feedback Loop
* Downloadable PDF Report

## Architecture

Diagnosis Agent
↓
Validation Agent
↓
Threshold Agent

If confidence is below threshold:
Threshold Agent → Diagnosis Agent

If confidence is above threshold:
Generate Final Report

## Tech Stack

Frontend:

* Next.js
* TailwindCSS
* shadcn/ui

Backend:

* FastAPI
* LangGraph
* Gemini 2.5 Flash

Deployment:

* Railway
* Vercel
