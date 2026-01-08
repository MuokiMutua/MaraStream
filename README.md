# MaraStream: Real-Time Fintech Event Streaming Pipeline

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/f7cc9602-6cda-4d36-a7a6-453e425b7451" />


## 1. Problem Statement
Traditional financial systems rely heavily on **batch processing**, where transactions are collected during the day and processed later in bulk. This delay prevents **real-time fraud detection** and **instant balance updates**.  

In a fast-moving retail and banking ecosystem like **Nairobi’s**, businesses need systems that can **process, analyze, and secure transactions in milliseconds**, not hours.

---

## 2. Solution
**MaraStream** is a **high-throughput, real-time event streaming pipeline** built with **Apache Kafka**. It decouples:

- **Data Sources** (transactions)  
- **Data Storage** (PostgreSQL & MongoDB)  
- **Security Layers** (Fraud Detection)

This architecture ensures **fault tolerance**—even if one database is slow or unavailable, the pipeline continues processing without losing a single transaction.

---

## 3. Objectives
- **Real-Time Ingestion:** Simulate a continuous stream of mobile money transactions using a Python-based Kafka **Producer**.  
- **Polyglot Persistence:** Store the same data stream in:
  - **PostgreSQL** for strict financial auditing  
  - **MongoDB** for flexible behavioral analytics  
- **Proactive Security:** Implement a real-time **Fraud Detection Engine** that instantly flags suspicious transactions (e.g., amounts > **100,000 KES**).  
- **Infrastructure as Code:** Use **Docker Compose** to orchestrate Kafka, Zookeeper, PostgreSQL, MongoDB, and Kafka UI with a single command.

---

## 4. The “How” (Project Architecture)
The pipeline operates through **independent, parallel workers**:

- **Ingestion (`producer.py`):**  
  Generates random *M-Pesa–style* JSON events (transaction ID, amount, merchant, location) and publishes them to a Kafka topic.

- **Streaming Core (Kafka):**  
  Acts as the central **event conveyor belt**, storing messages in partitions and serving them to multiple consumers simultaneously.

- **Auditing Loop (`consumer_postgres.py`):**  
  Consumes events and performs **at-least-once inserts** into a structured PostgreSQL table for compliance and auditing.

- **Analytics Loop (`mongo.py`):**  
  Stores raw JSON events in MongoDB, enabling future **machine learning**


- **Security Loop (`fraud.py`):**  
  A high-priority consumer that applies business rules to flag and alert on **high-risk transactions** in real time.

- **Orchestration (`run_all.py`):**  
  A master script that manages and runs all Python workers concurrently.

---

## 5. Processing Type: Continuous (Streaming)
This system is **continuous**, not batch-based.

- **Why?**  
  In batch systems, data is static (e.g., CSV files). In MaraStream, data is **ephemeral and constantly in motion**.

- **The Difference:**  
  Every new transaction is processed **immediately** by `fraud.py` and `mongo.py`. The pipeline never pauses—it reacts to each event **as it arrives**, enabling true real-time intelligence.
