<h3>Disaster Response RAG Model with Offline Bluetooth Support</h3>

<h4>Overview</h4>

This project presents a Retrieval-Augmented Generation (RAG) model designed for disaster response, offering **offline functionality via Bluetooth** and **multilingual support**. The model operates with **real-time data updates** on a server, which seamlessly connects with client devices during emergencies, delivering essential, life-saving information in multiple languages—without requiring an internet connection.
#Key Features
<u>Real-Time Disaster Updates</u>: The server gathers real-time crisis data and prepares it for retrieval.
<u>Offline Accessibility</u>: Bluetooth connectivity ensures the model provides critical guidance even without network access.
<u>Personalized Assistance</u>: Tailored advice on first aid, evacuation routes, and emergency contacts.
<u>Multilingual Support</u>: Reach broader audiences with support for multiple languages.
Location-Based Alerts: Localized information such as flood alerts, available even offline.


<h4>Installation</h4>

Clone the Repository:
```bash
Copy code
git clone https://github.com/yourusername/disaster-response-rag.git
```

Install Dependencies:
```bash
Copy code
cd disaster-response-rag
pip install -r requirements.txt
```

<h4>Usage</h4>

The server updates real-time data regularly and stores it for offline access.
<u>Client Setup</u>: Client devices establish Bluetooth pairing with the server and retrieve data as needed.
Queries can be made offline, with responses tailored to the user's location and circumstances.
Project Structure
<u>server.py</u>: Manages data updates, Bluetooth connections, and RAG model responses.
<u>client.py</u>: Interface for users to query the RAG model and receive offline assistance.

<h4>Contributing</h4>
Contributions are welcome! Please fork the repo and create a pull request for review.
