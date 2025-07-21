     background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
    }
    .prediction-result {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 1.5rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data(ttl=3600)  
def get_exchange_rate():
    try:
        # Using a free API for exchange rates
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        if response.status_code == 200:
            data = response.json()
            return data['rates']['INR']
        else:
            return 83.0  
    except:
        return 83.0  


@st.cache_resource
def load_model():
    try:
        model = joblib.load("final.pkl")
        return model
    except FileNotFoundError:
        st.error("Model file 'final.pkl' not found. Please ensure the model file is in the correct directory.")
        return None
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None


st.markdown('<h1 class="main-header">💵 MyPay Predictor 💵</h1>', unsafe_allow_html=True)


with st.sidebar:
    st.header("📊 App Features")
    st.markdown("""
    - **Real-time Predictions**: Get instant salary estimates
    - **Currency Conversion**: Results in both USD and INR
    - **Visualizations**: Interactive charts and graphs
    - **Comparison Tool**: Compare multiple scenarios
    - **Export Results**: Download predictions as CSV
    """)
    
    st.header("ℹ️ About")
    st.info("This app uses machine learning to predict salaries based on years of experience and job rate.")
    
    
    exchange_rate = get_exchange_rate()
    st.metric("Current USD to INR", f"₹{exchange_rate:.2f}")


col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📝 Input Parameters")
    
    
    with st.form("prediction_form"):
        col_input1, col_input2 = st.columns(2)
        
        with col_input1:
            years = st.number_input(
                "Years of Experience 👨‍💼", 
                value=1, 
                step=1, 
                min_value=0, 
                max_value=50,
                help="Enter the number of years of professional experience"
            )
            
        with col_input2:
            jobrate = st.number_input(
                "Job Rate (1-10) ⭐", 
                value=3.5, 
                step=0.1, 
                min_value=0.0, 
                max_value=10.0,
                help="Rate the job complexity/level (1=Entry level, 10=Executive level)"
            )
        
        
        st.markdown("### 🎯 Advanced Options")
        
        col_adv1, col_adv2 = st.columns(2)
        with col_adv1:
            show_comparison = st.checkbox("Show Salary Comparison Chart", value=True)
        with col_adv2:
            show_market_analysis = st.checkbox("Show Market Analysis", value=True)
        
        predict_button = st.form_submit_button("🔮 Predict Salary", use_container_width=True)

with col2:
    st.markdown("### 📊 Quick Stats")
    
    
    st.markdown(f"""
    <div class="metric-card">
        <h4>Input Summary</h4>
        <p>Experience: {years} years</p>
        <p>Job Rate: {jobrate}/10</p>
        <p>Date: {datetime.now().strftime('%Y-%m-%d')}</p>
    </div>
    """, unsafe_allow_html=True)


if predict_button:
    model = load_model()
    
    if model is not None:
        try:
            
            X = np.array([[years, jobrate]])
            prediction_usd = model.predict(X)[0]
            prediction_inr = prediction_usd * exchange_rate
            
            
            st.balloons()
            
            st.markdown("### 🎉 Prediction Results")
            
            
            col_result1, col_result2, col_result3 = st.columns(3)
            
            with col_result1:
                st.metric(
                    "Predicted Salary (USD)", 
                    f"${prediction_usd:,.2f}",
                    delta=f"${prediction_usd*0.1:,.2f} potential growth"
                )
            
            with col_result2:
                st.metric(
                    "Predicted Salary (INR)", 
                    f"₹{prediction_inr:,.2f}",
                    delta=f"₹{prediction_inr*0.1:,.2f} potential growth"
                )
            
            with col_result3:
                monthly_inr = prediction_inr / 12
                st.metric(
                    "Monthly Salary (INR)", 
                    f"₹{monthly_inr:,.2f}",
                    delta="Per month"
                )
            
           
            
            
            if show_comparison:
                st.markdown("### 📊 Salary Comparison Chart")
                
                
                experience_range = list(range(max(0, years-5), min(years+6, 21)))
                salaries_usd = []
                salaries_inr = []
                
                for exp in experience_range:
                    pred_usd = model.predict(np.array([[exp, jobrate]]))[0]
                    pred_inr = pred_usd * exchange_rate
                    salaries_usd.append(pred_usd)
                    salaries_inr.append(pred_inr)
                
                
                fig = go.Figure()
                
                fig.add_trace(go.Scatter(
                    x=experience_range,
                    y=salaries_inr,
                    mode='lines+markers',
                    name='Predicted Salary (INR)',
                    line=dict(color='#1f77b4', width=3),
                    marker=dict(size=8)
                ))
                
                
                fig.add_trace(go.Scatter(
                    x=[years],
                    y=[prediction_inr],
                    mode='markers',
                    name='Your Prediction',
                    marker=dict(size=15, color='red', symbol='star')
                ))
                
                fig.update_layout(
                    title="Salary vs Experience (Current Job Rate)",
                    xaxis_title="Years of Experience",
                    yaxis_title="Salary (INR)",
                    hovermode='x unified',
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
            
           
            if show_market_analysis:
                st.markdown("### 🏢 Market Analysis")
                
                
                job_rates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                market_salaries = []
                
                for rate in job_rates:
                    market_pred = model.predict(np.array([[years, rate]]))[0] * exchange_rate
                    market_salaries.append(market_pred)
                
                fig_market = px.bar(
                    x=job_rates,
                    y=market_salaries,
                    title=f"Salary by Job Rate (Experience: {years} years)",
                    labels={'x': 'Job Rate', 'y': 'Salary (INR)'},
                    color=market_salaries,
                    color_continuous_scale='Viridis'
                )
                
               
                fig_market.add_vline(x=jobrate, line_dash="dash", line_color="red", 
                                   annotation_text="Your Job Rate")
                
                st.plotly_chart(fig_market, use_container_width=True)
            
            
            st.markdown("### 💾 Export Results")
            
            export_data = {
                'Years_of_Experience': [years],
                'Job_Rate': [jobrate],
                'Predicted_Salary_USD': [prediction_usd],
                'Predicted_Salary_INR': [prediction_inr],
                'Monthly_Salary_INR': [monthly_inr],
                'Exchange_Rate': [exchange_rate],
                'Prediction_Date': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
            }
            
            df_export = pd.DataFrame(export_data)
            csv = df_export.to_csv(index=False)
            
            st.download_button(
                label="📥 Download Prediction as CSV",
                data=csv,
                file_name=f"salary_prediction_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
            
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")
    else:
        st.error("Unable to load the prediction model.")
else:
    st.info("👆 Please enter your details above and click 'Predict Salary' to get your salary estimate.")
    
    
    st.markdown("### 📊 Sample Salary Trends")
    
    
    sample_years = list(range(0, 21))
    sample_rates = [3, 5, 7]
    
    fig_sample = go.Figure()
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    for i, rate in enumerate(sample_rates):
        sample_salaries = [(year * 5000 + rate * 10000) * exchange_rate for year in sample_years]
        fig_sample.add_trace(go.Scatter(
            x=sample_years,
            y=sample_salaries,
            mode='lines',
            name=f'Job Rate {rate}',
            line=dict(color=colors[i], width=2)
        ))
    
    fig_sample.update_layout(
        title="Sample Salary Trends by Experience and Job Rate",
        xaxis_title="Years of Experience",
        yaxis_title="Salary (INR)",
        height=400
    )
    
    st.plotly_chart(fig_sample, use_container_width=True)


st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    
    
</div>
""".format(datetime.now().strftime('%Y-%m-%d')), unsafe_allow_html=True)