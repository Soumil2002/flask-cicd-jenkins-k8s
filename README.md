
# 📄 Flask CI/CD Pipeline with Jenkins, Docker, Kubernetes (Minikube), and Helm

---

## 📚 Project Overview

This project implements a complete CI/CD pipeline to automate the build, test, and deployment of a **Python Flask web application** using:

- **Jenkins** for automation
- **Docker** for containerization
- **DockerHub** for image hosting
- **Kubernetes (Minikube)** for container orchestration
- **Helm** for Kubernetes package management
- **AWS EC2** for hosting Jenkins server and Minikube cluster

---

## 🛠 Tech Stack

| Tool/Technology       | Purpose                                     |
|-----------------------|---------------------------------------------|
| Python Flask           | Backend Web Application                    |
| Docker                 | Containerize Flask App                      |
| Jenkins                | Automate CI/CD Pipeline                     |
| DockerHub              | Store Built Docker Images                   |
| Kubernetes (Minikube)  | Deploy and Orchestrate App                  |
| Helm                   | Manage Kubernetes Manifests                 |
| AWS EC2 (Ubuntu 22.04) | Cloud Server to Host Pipeline               |

---



## 🔥 CI/CD Pipeline Flow

1. Developer pushes code to **GitHub** repository.
2. **Jenkins** pulls the latest code.
3. Jenkins **builds Docker image** for Flask app.
4. Jenkins **pushes the image** to **DockerHub**.
5. Jenkins **deploys Flask app** into **Minikube Kubernetes** cluster using **Helm**.
6. Application becomes accessible through a **NodePort Service**.

---

## ⚙️ Complete Setup Guide (AWS EC2)

### 1. Launch an EC2 Instance
- AMI: **Ubuntu 22.04 LTS**
- Instance Type: **t2.medium or above**
- Security Groups:
  - Allow SSH (port 22)
  - Allow HTTP (port 80)
  - Allow Custom TCP (port 8080) — for Jenkins
  - Allow NodePort Range (30000–32767) — for Kubernetes service

### 2. Connect to EC2 Instance

```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
```

### 3. Install Prerequisites

**Install Docker:**
```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ubuntu
```
Logout and login again to apply Docker group permission.

**Install Java (JDK 17):**
```bash
sudo apt install -y openjdk-17-jdk
```

**Install Jenkins:**
```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee   /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]   https://pkg.jenkins.io/debian-stable binary/ | sudo tee   /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update
sudo apt install -y jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

Jenkins URL:  
`http://your-ec2-public-ip:8080`

**Install Minikube:**
```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

**Install kubectl:**
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

**Install Helm:**
```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

**Install Docker Compose (Optional):**
```bash
sudo apt install docker-compose -y
```

---

### 4. Start Minikube (Docker Driver)

```bash
minikube start --driver=docker
```

Check cluster:
```bash
kubectl get nodes
```

---

### 5. Setup Jenkins

- Unlock Jenkins (password path: `/var/lib/jenkins/secrets/initialAdminPassword`)
- Install suggested plugins
- Create admin user

Install Jenkins Plugins:
- Docker Pipeline
- Kubernetes CLI Plugin
- Kubernetes Plugin
- GitHub Integration Plugin
- Helm Plugin

Add Jenkins Credentials:
- DockerHub Credentials (ID: `dockerhub-credentials`)
- GitHub Credentials (if private repo)

---

### 6. Create Jenkins Pipeline Job

- New Item → **Pipeline**
- Definition: **Pipeline script from SCM**
- SCM: Git
- Repository URL: your GitHub repo URL
- Script Path: `Jenkinsfile`

---

### 7. Run Jenkins Build

- Click **Build Now**
- Pipeline will:
  - Pull Code
  - Build Docker Image
  - Push to DockerHub
  - Deploy to Minikube via Helm

---

### 8. Access Flask App

Get Minikube Service URL:

```bash
minikube service flask-service --url
```

Example URL:
```
http://192.168.49.2:30567
```

Open in browser → App is live! 🚀

---

## 🌟 Final Outcome

| Component             | Status            |
|------------------------|-------------------|
| Jenkins CI/CD          | ✅ Completed      |
| Docker Image Build     | ✅ Completed      |
| DockerHub Push         | ✅ Completed      |
| Kubernetes Deployment  | ✅ Completed      |
| Helm Chart Usage       | ✅ Completed      |
| Flask App Access       | ✅ Completed      |

---


# Thank you! 🚀 Happy DevOps! 🌟
