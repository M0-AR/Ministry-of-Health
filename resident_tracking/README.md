# Resident Doctors Tracking System

نظام متابعة الأطباء المقيمين في مشافي دمشق

## Live Demo 🚀
Try the application here: [https://ministry-of-health.streamlit.app/](https://ministry-of-health.streamlit.app/)

## Overview
This Streamlit application helps track and manage resident doctors across hospitals in Damascus. It provides real-time insights into doctor distributions, transfer history, and residency periods.

## Features

### 📋 Main Dashboard
- Complete list of resident doctors
- Search and filter by hospital and specialty
- Quick view of doctor status and residency periods

### 🏥 Hospital Information
- Detailed hospital profiles
- Number of beds and departments
- Type of hospital (Government, University, Specialized)
- Location information

### 🔄 Transfer Management
- Track doctor transfers between hospitals
- Historical transfer records
- Transfer reasons and documentation

### 📊 Statistical Reports
- Specialty distribution (Pie Chart)
- Hospital distribution (Bar Chart)
- Monthly transfer trends (Line Chart)
- Residency period alerts

### 📱 User Interface
- Mobile-friendly responsive design
- RTL support for Arabic language
- Expandable cards for detailed information
- Intuitive navigation with sidebar

## Technical Details

### Dependencies
```
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.14.0
```

### Local Development
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

### Project Structure
```
resident_tracking/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .streamlit/        # Streamlit configuration
│   └── config.toml    # Theme and settings
└── README.md          # This documentation
```

## Contributing
Feel free to open issues or submit pull requests if you have suggestions for improvements or find any bugs.

## License
This project is part of the Ministry of Health repository. All rights reserved.
