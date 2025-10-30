# 💵 MyPay Predictor

A machine learning-powered web application that predicts salaries based on years of experience and job complexity rating. Built with Streamlit and featuring real-time currency conversion, interactive visualizations, and comprehensive market analysis.

## 🌟 Features

- **Real-time Salary Predictions**: Get instant salary estimates based on experience and job rate
- **Currency Conversion**: Automatic USD to INR conversion with live exchange rates
- **Interactive Visualizations**: 
  - Salary vs Experience comparison charts
  - Market analysis by job rate
  - Sample salary trend visualizations
- **Export Functionality**: Download predictions as CSV for record-keeping
- **Responsive UI**: Clean, modern interface with gradient design
- **Advanced Options**: Toggle comparison charts and market analysis

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/MyPay-Predictor.git
   cd MyPay-Predictor
   ```

2. **Install required dependencies**
   ```bash
   pip install streamlit numpy pandas plotly joblib requests
   ```

3. **Ensure model file is present**
   
   Make sure `final.pkl` (the trained ML model) is in the project root directory.

## 💻 Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the web interface**
   
   The app will automatically open in your default browser at `http://localhost:8501`

3. **Make predictions**
   - Enter years of experience (0-50)
   - Set job rate (1-10, where 1=Entry level, 10=Executive level)
   - Toggle advanced options for charts and analysis
   - Click "Predict Salary" to get results

## 📊 Application Interface

### Landing Page
<img width="1909" height="992" alt="Landing Page" src="https://github.com/user-attachments/assets/9514cb57-73eb-4068-b6f6-84123aa642a6" />

### Prediction Results
<img width="1919" height="1002" alt="Prediction Results" src="https://github.com/user-attachments/assets/b9bfb3e9-d9e3-49a2-b829-f015fbbff850" />

## 🏗️ Project Structure

```
MyPay-Predictor/
│
├── app.py              # Main Streamlit application
├── final.pkl           # Trained ML model (pickle file)
├── Employees.xlsx      # Training data (Excel file)
├── README.md           # Project documentation
└── .git/               # Git repository
```

## 🔧 How It Works

1. **Input Processing**: User provides years of experience and job rate
2. **Model Prediction**: Pre-trained ML model (stored in `final.pkl`) predicts salary in USD
3. **Currency Conversion**: Real-time exchange rates from API convert USD to INR
4. **Visualization**: Interactive charts show salary trends and market comparisons
5. **Export**: Results can be downloaded as CSV with timestamp

## 📦 Dependencies

- **streamlit**: Web application framework
- **numpy**: Numerical computing
- **pandas**: Data manipulation and analysis
- **plotly**: Interactive visualizations (plotly.graph_objects, plotly.express)
- **joblib**: Model serialization/deserialization
- **requests**: HTTP library for exchange rate API calls
- **datetime**: Timestamp generation

## 🌐 Exchange Rate API

The application uses the [Exchange Rate API](https://api.exchangerate-api.com/) for real-time USD to INR conversion. Exchange rates are cached for 1 hour to optimize performance.

## 📈 Features Breakdown

### Sidebar
- App features overview
- About section
- Real-time exchange rate display

### Main Interface
- **Input Parameters**: Experience and job rate input fields
- **Quick Stats**: Summary of current inputs
- **Prediction Results**: Displays predicted salary in USD, INR, and monthly INR
- **Salary Comparison Chart**: Shows salary progression across experience levels
- **Market Analysis**: Bar chart comparing salaries across different job rates
- **Export Results**: CSV download with all prediction details

## 🎨 UI Design

- Modern gradient color scheme (purple/blue palette)
- Responsive layout with columns
- Custom CSS styling for enhanced visual appeal
- Emoji icons for better user experience
- Interactive charts with Plotly

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

Your Name - [GitHub Profile](https://github.com/yourusername)

## 🐛 Known Issues

- Exchange rate API may fallback to default rate (83.0) if service is unavailable
- Model predictions are based on training data and may not reflect all market conditions

## 🔮 Future Enhancements

- [ ] Add more input parameters (location, industry, education)
- [ ] Support for multiple currencies
- [ ] Historical prediction tracking
- [ ] Model retraining interface
- [ ] Comparison with market benchmarks
- [ ] User authentication and saved predictions

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.

---

**Note**: This application is for educational and estimation purposes only. Actual salaries may vary based on numerous factors including location, company, industry, and individual qualifications.
