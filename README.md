### README for Football Paradise Stream Management Platform

### **Project Overview**  
This repository contains the codebase for the **Stream Management Platform** developed for Football Paradise, a leading football literature website. The platform enhances user engagement by integrating live streams, match highlights, and post-match analyses. It leverages MediaCMS as the foundation, with custom UI and technical changes to meet Football Paradise’s unique requirements.  

---

### **Project Structure**  
1. **UI/UX Design**:  
   - Custom designs created to align with Football Paradise’s branding and enhance user interaction.  

2. **Frontend Development**:  
   - Developed using React.js to deliver a responsive and dynamic user interface.  

3. **Backend Development**:  
   - Built with Django (MediaCMS core) to handle data processing, API integration, and stream management workflows.  

4. **Test Environment**:  
   - Comprehensive testing to ensure the reliability of streaming and media management functionalities before deployment.  

---

### **Key Features**  
- **Centralized Media Management**:  
   Unified platform for managing live streams, pre-recorded videos, and metadata.  

- **Real-Time Monitoring and Health Checks**:  
   Integrated tools for tracking stream performance and system uptime.  

- **Scalable Video Storage**:  
   Seamlessly integrated with AWS S3 for efficient and scalable media storage.  

- **User Analytics and Engagement Tracking**:  
   Analytics dashboard for tracking viewer engagement, stream performance, and user interactions.  

---

### **Technologies Used**  

1. **Frontend**:  
   - React.js, HTML, CSS, JavaScript.  

2. **Backend**:  
   - MediaCMS with Django and PostgreSQL.  

3. **Cloud Services**:  
   - AWS (S3 for storage, EC2 for hosting).  

4. **Version Control**:  
   - Git for collaboration and version management.  

---

### **Customizations to MediaCMS**  

- **UI Adjustments**:  
   - Updated the interface with Football Paradise branding, including logo and theme changes.  
   - Added features like live streaming sections and analytics dashboards.  

- **Technical Changes**:  
   - Integrated adaptive video streaming with HLS for seamless playback.  
   - Configured transcoding profiles and prioritized workflows for football-specific needs.  
   - Enhanced role-based access control for administrators, uploaders, and viewers.  

---

### **Getting Started**  

#### **Prerequisites**  
- Node.js (v14 or above)  
- Docker (for containerized deployment)  
- AWS account (for cloud storage and hosting)  

#### **Installation**  

1. Clone the repository:  
   ```bash
   git clone https://github.com/UMDMSISCapstone/StreamingPlatform-FP.git
   ```  

2. Navigate to the project directory:  
   ```bash
   cd StreamingPlatform-FP
   ```  

3. Build and start the application using Docker Compose:  
   ```bash
   docker-compose up --build
   ```  

4. Access the application:  
   - Frontend: `http://localhost:3000`  
   - Admin Panel: `http://localhost:8000/admin`  

---

### **Running the Project**  

To start the platform locally:  
```bash
docker-compose up
```  

For running unit tests:  
```bash
docker exec -it <container_id> pytest
```  

---

### **Contribution Guidelines**  

We welcome contributions to improve the platform!  

1. **Fork the Repository**:  
   ```bash
   git fork https://github.com/UMDMSISCapstone/StreamingPlatform-FP.git
   ```  

2. **Create a Branch**:  
   ```bash
   git checkout -b feature/your-feature-name
   ```  

3. **Commit and Push Changes**:  
   ```bash
   git commit -m "Add your changes"
   git push origin feature/your-feature-name
   ```  

4. **Submit a Pull Request**.  

---  
