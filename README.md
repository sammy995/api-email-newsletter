# Automated Technology News Email Newsletter

Welcome to the repository for the Automated Technology News Email Newsletter, a Python-based application designed to automate the distribution of technology news via email. This backend service fetches the latest technology news using the News API, formats it into an email, and securely sends it to subscribers.

## Key Features

- **Automated News Fetching**: Retrieves the latest headlines from the technology sector using the News API.
- **Email Composition**: Dynamically generates email content featuring news titles, descriptions, and links.
- **Secure Email Delivery**: Uses SMTP over SSL to send emails securely.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What you need to install the software:

- Python 3.x
- `requests` library
- `smtplib` and `ssl` for email handling

### Installing

Follow these steps to get a development environment running:

1. Clone the repository:
 ```bash
git clone https://github.com/your-username/technology-news-email-newsletter.git
```

Navigate to the project directory:
```bash
cd technology-news-email-newsletter
```

Install required Python libraries:
```bash
pip install requests
```

### Usage
Run the script to start fetching news and sending emails:
```bash
python main.py
```

#### Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request



### Contact
Your Name -Shubham Lagad

### Acknowledgments
News API for providing the news data.
