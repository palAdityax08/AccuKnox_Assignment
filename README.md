# AccuKnox AI/ML Assessment - Aditya Pal

This repository contains my solutions for the Problem Statement 1 coding tasks.

## 📂 Project Structure
- `task1_books.py`: Fetches mock book data and stores it in SQLite.
- `task2_scores.py`: Visualizes student test scores using Matplotlib.
- `task3_csv_import.py`: Imports user data from CSV to SQLite.

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install pandas matplotlib
2. Run any task:
   ```bash
   pyhton task1.py
   
📝 Assumptions Made
For Task 1 & 2, since no public API URL was provided, I mocked the API response data within the script as per instructions.
For Task 3, I created a dummy users.csv file for demonstration.

---

### **Step 2: The Final PDF Document (The "Selection" Document)**
This is what you will email or upload. Do not just paste wall-to-wall code. Use this professional structure.

**Title:** `Aditya_Pal_AccuKnox_Assessment_Response.pdf`

**Content to Copy/Paste into Word (then save as PDF):**

> **Name:** Aditya Pal
> **Role Applied:** AI/ML Trainee
> **Email:** adipal521@gmail.com
> **GitHub:** [Link to your Profile]
>
> ---
>
> ### **Part 1: Coding Assessment Solutions**
> **Repository Link:** [Insert Link to your new AccuKnox-Assessment-Aditya Repo Here]
>
> **Task 1: API Retrieval & Storage**
> * **Approach:** I created a Python script that mimics fetching JSON data and uses the `sqlite3` library to persist it locally.
> * **Assumption:** As no live API endpoint was provided, I mocked the response payload to demonstrate the parsing logic[cite: 74].
> * **Output Screenshot:**
>     [PASTE SCREENSHOT OF YOUR TERMINAL SHOWING THE BOOKS DATA]
>
> **Task 2: Data Visualization**
> * **Approach:** Used `pandas` for calculating the mean and `matplotlib` for generating the bar chart.
> * **Output Screenshot:**
>     [PASTE SCREENSHOT OF THE BLUE BAR CHART]
>
> **Task 3: CSV Import**
> * **Approach:** Utilized the `csv` module to read data and insert it into a new SQLite table `users`.
> * **Output Screenshot:**
>     [PASTE SCREENSHOT OF TERMINAL SAYING "Success"]
>
> ---
>
> ### **Part 2: Subjective Answers**
>
> **1. Self Rating**
> * **Rating:** **A (Independent)** for Python & LLMs; **B (Supervised)** for Deep Learning theory.
> * **Reasoning:** I have independently engineered end-to-end RAG systems (like my project AIKARA), so I am confident in coding. However, I am still exploring advanced DL research topics and would value supervision there[cite: 82].
>
> **2. LLM Chatbot Architecture**
> To build a reliable chatbot, I advocate for a **RAG (Retrieval-Augmented Generation)** approach to prevent hallucinations[cite: 84].
> * **Core Components:**
>     * **Vector Database:** To store knowledge as embeddings.
>     * **Retriever:** To fetch relevant context based on user queries.
>     * **Generator (LLM):** To synthesize the answer using *only* the retrieved context.
>
> **3. Vector Databases**
> * **Explanation:** Vector DBs store data as high-dimensional vectors, enabling "semantic search" (search by meaning) rather than keyword matching[cite: 86].
> * **My Choice:** **ChromaDB**.
> * **Why:** For most initial use cases, Chroma is open-source, runs locally (no complex server setup), and integrates seamlessly with Python, making it ideal for rapid development.
>
> ---
>
> ### **Part 3: Code Samples**
>
> **Most Complex Python Code:**
> * **Project:** AIKARA (AI Teaching Assistant)
> * **Link:** [INSERT LINK TO YOUR AIKARA REPO]
> * **Description:** This code implements a RAG pipeline involving PDF chunking, vector embedding generation (using `bge-m3`), and context injection into Llama 3.2.
>
> **Most Complex Database Code:**
> * **Project:** SecureNest (IoT Data Handling)
> * **Link:** [INSERT LINK TO YOUR SECURENEST REPO]
> * **Description:** Handles real-time telemetry data processing and storage for edge anomaly detection.

---

### **Why this format wins:**
1.  **It follows instructions:** The instructions said "You may make any assumptions you want, just document them"[cite: 74]. We explicitly added an **"Assumption"** bullet point for Task 1.
2.  **It is clean:** The recruiter doesn't have to scroll through pages of code. They see the Screenshot (proof it works) and the Link (proof you write clean code).
3.  **It highlights AIKARA:** The "Complex Code" section drives them to your best project, which we already know is strong.

**Action:** Go create the Repo now. Then take the screenshots. Then build this PDF. You've got this.
