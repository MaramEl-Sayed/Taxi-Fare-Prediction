# NYC Taxi Fare Prediction Web Application

A Django-based web application that predicts taxi fare amounts for New York City trips using machine learning. The application takes various factors into account including weather conditions, traffic patterns, trip distance, and temporal features to provide accurate fare predictions.

![Taxi Fare Prediction](https://img.shields.io/badge/ML-TensorFlow-orange) ![Django](https://img.shields.io/badge/Framework-Django-green) ![Python](https://img.shields.io/badge/Python-3.8+-blue)

## 🚖 Features

- **Machine Learning Prediction**: Uses a trained TensorFlow/Keras model for fare estimation
- **Comprehensive Input Parameters**: 19 different features including:
  - Environmental conditions (weather, traffic)
  - Vehicle condition
  - Temporal features (hour, day, month, weekday)
  - Geographic coordinates and distances
  - Trip-specific metrics (distance, bearing)
- **Responsive Web Interface**: Clean, mobile-friendly UI with real-time form validation
- **Interactive Results**: Detailed prediction results with option to make multiple predictions
- **Error Handling**: Robust input validation and error management

## 🛠️ Technology Stack

- **Backend**: Django 5.1.2
- **Machine Learning**: TensorFlow/Keras
- **Frontend**: HTML5, CSS3, Bootstrap 4
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Python**: 3.8+

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/nyc-taxi-fare-prediction.git
cd nyc-taxi-fare-prediction
```

### 2. Create Virtual Environment
```bash
python -m venv taxi_prediction_env
source taxi_prediction_env/bin/activate  # On Windows: taxi_prediction_env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Prepare the Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Place the ML Model
Ensure your trained model file (`model.h5`) is placed in:
```
myAPP/Models/model.h5
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 📁 Project Structure

```
nyc-taxi-fare-prediction/
├── basic/                     # Django app for prediction logic
│   ├── views.py              # Main application views
│   ├── urls.py               # URL routing
│   └── ...
├── myAPP/                    # Main Django project
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL configuration
│   ├── templates/            # HTML templates
│   │   ├── index.html        # Input form
│   │   └── result.html       # Prediction results
│   ├── static/               # Static files (CSS, JS, images)
│   └── Models/               # ML model storage
│       └── model.h5          # Trained prediction model
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## 🎯 Usage

### Making a Prediction

1. **Access the Application**: Navigate to the home page
2. **Fill the Form**: Enter the following information:
   - **Car Condition**: Excellent, Very Good, Good, or Bad
   - **Traffic Condition**: Congested, Dense, or Flow Traffic
   - **Weather Condition**: Sunny, Cloudy, Rainy, Stormy, or Windy
   - **Passenger Count**: Number of passengers (1-6)
   - **Temporal Information**: Hour (0-23), Month (1-12), Day (1-31), Week Day (1-7)
   - **Location Data**: Pickup/Dropoff coordinates
   - **Distance Information**: Distances to major NYC landmarks and airports
   - **Trip Metrics**: Total distance and bearing

3. **Get Prediction**: Click "Predict Fare" to receive the estimated fare amount

### Input Guidelines

- **Coordinates**: Use NYC-area longitude (-75 to -73) and latitude (40 to 42)
- **Distances**: Enter distances in miles to:
  - JFK Airport (jfk_dist)
  - Statue of Liberty (sol_dist)
  - LaGuardia Airport (lga_dist)
  - Newark Airport (ewr_dist)
  - NYC Center (nyc_dist)
- **Time Format**: Use 24-hour format for hours (0-23)

## 🧠 Model Information

The prediction model uses a neural network trained on NYC taxi trip data with the following features:

### Input Features (19 total):
1. **Categorical**: Car condition, traffic condition, weather condition
2. **Temporal**: Hour, day, month, weekday
3. **Geographic**: Pickup/dropoff coordinates, distances to landmarks
4. **Trip**: Total distance, bearing, passenger count

### Model Architecture:
- **Framework**: TensorFlow/Keras
- **Type**: Deep Neural Network
- **Input Shape**: (19,) features
- **Output**: Single fare prediction value

## 🔧 Configuration

### Environment Variables
| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Required |
| `DEBUG` | Debug mode | `True` |
| `ALLOWED_HOSTS` | Allowed host names | `localhost,127.0.0.1` |

### Model Configuration
- Model path: `myAPP/Models/model.h5`
- Model format: TensorFlow SavedModel (.h5)
- Input preprocessing: Categorical encoding + numerical normalization

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

For more comprehensive testing:
```bash
python -m pytest
```

## 📊 API Reference (Future Enhancement)

The application currently supports web form input. API endpoints are planned for future releases:

```http
POST /api/predict
Content-Type: application/json

{
  "car_condition": "Good",
  "traffic_condition": "Flow Traffic",
  "weather_condition": "Sunny",
  "passenger_count": 2,
  "pickup_longitude": -73.986,
  "pickup_latitude": 40.748,
  // ... other parameters
}
```

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use environment variables for secrets
- [ ] Set up production database (PostgreSQL)
- [ ] Configure static file serving
- [ ] Add HTTPS/SSL
- [ ] Set up monitoring and logging

### Deployment Platforms
- **Heroku**: Easy deployment with git integration
- **Railway**: Modern platform with simple deployment
- **DigitalOcean**: App Platform for scalable deployment
- **AWS**: EC2 or Elastic Beanstalk for enterprise deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Write tests for new features
- Update documentation for changes
- Ensure backward compatibility

## 📝 Requirements

Create a `requirements.txt` file with:
```txt
Django==5.1.2
tensorflow==2.13.0
numpy==1.24.3
python-decouple==3.8
gunicorn==21.2.0
whitenoise==6.5.0
```

## 🐛 Known Issues

- Model loading may take time on first request
- Large coordinate values outside NYC bounds may cause errors
- No user authentication or session management currently implemented

## 🔮 Future Enhancements

- [ ] Real-time data integration
- [ ] User authentication and prediction history
- [ ] Interactive map for coordinate selection
- [ ] API endpoints for programmatic access
- [ ] Model retraining pipeline
- [ ] A/B testing for different models
- [ ] Performance monitoring and analytics
- [ ] Mobile application
- [ ] Multi-city support



## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- NYC Taxi and Limousine Commission for the dataset
- TensorFlow/Keras team for the ML framework
- Django community for the excellent web framework
- Bootstrap team for responsive design components

---

**Made with ❤️ for the NYC taxi community**
