# 🚀 Kizon's Inventory System

**Live Demo:** http://54.251.213.179:5000/

## 📋 Project Overview
A containerized Python web application deployed on cloud infrastructure. This project serves as a practical demonstration of modern deployment pipelines, bridging local development with live server hosting. The application is packaged using Docker for environment consistency and hosted on a remote AWS EC2 instance.

## 🛠️ The Tech Stack
* **Cloud Infrastructure:** AWS EC2 (Ubuntu Linux)
* **Containerization:** Docker & Docker Compose
* **Version Control:** Git & GitHub
* **Backend Code:** Python / Flask
* **Database:** PostgreSQL 

## 🏗️ Architecture & Deployment Pipeline
This project utilizes a manual CI/CD approach to ensure zero-downtime updates:
1. **Local Development:** Code is written and tested locally in VS Code.
2. **Version Control:** Changes are packaged and pushed to a remote GitHub repository using secure Personal Access Tokens (PAT).
3. **Remote Pull:** The AWS Ubuntu server securely pulls the latest main branch via SSH.
4. **Hot-Swapping:** `docker compose up --build -d` is executed to bypass cache, rebuild the image in the background, and seamlessly swap the live container with minimal downtime.

## ⚔️ Challenges Conquered
Building this project involved actively troubleshooting real-world DevOps scenarios, including:
* **Resolving Git Merge Conflicts:** Successfully diagnosed and cleared stalled commits caused by remote vs. local branch desynchronization.
* **Managing Docker Build Caches:** Overcame ghost-caching issues by forcing strict image rebuilds to ensure live code reflection.
* **Network & Port Configuration:** Configured AWS EC2 dynamic IPs and mapped internal Docker container ports (5000:5000) to safely expose the application to the internet.

## ⚙️ How to Run Locally
If you want to run this container on your own machine:

1. Clone this repository:
   ```bash
   git clone https://github.com/Kizon29/my-first-container.git

2. Navigate into the directory:
    cd my-first-container

3. Start the Docker engine:
    docker compose up --build -d

4. Open your browser and go to http://localhost:5000