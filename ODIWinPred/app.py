import streamlit as st
import pickle
import pandas as pd

teams = [
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'West Indies',
    'Afghanistan',
    'Pakistan',
    'Sri Lanka'
]

cities = ['Mirpur', 'Abu Dhabi', 'Chittagong', 'Port Elizabeth',
       'Chester-le-Street', 'Guyana', 'Perth', 'Colombo', 'Christchurch',
       'London', 'Hobart', 'Centurion', 'Nelson', 'Melbourne',
       'Johannesburg', 'Kolkata', 'Auckland', 'Trinidad', 'Sydney',
       'Cardiff', 'Ranchi', 'Visakhapatnam', 'Barbados', 'Pallekele',
       'Rangiri', 'Antigua', 'Nagpur', 'Wellington', 'Dunedin',
       'Adelaide', 'Rajkot', 'Chandigarh', 'Gwalior', 'Chennai',
       'Ahmedabad', 'Indore', 'Leeds', 'Southampton', 'St Kitts',
       'Karachi', 'Durban', 'Potchefstroom', 'Dubai', 'Lahore',
       'Birmingham', 'Mount Maunganui', 'Cuttack', 'Cape Town',
       'Nottingham', 'Hamilton', 'Bristol', 'Brisbane', 'Harare',
       'Jaipur', 'Manchester', 'Napier', 'East London', 'Pune',
       'Hambantota', 'Lucknow', 'Guwahati', 'Delhi', 'Sharjah',
       'St Lucia', 'Khulna', 'Mumbai', 'Kuala Lumpur', 'Multan',
       'Belfast', 'Bulawayo', 'Jamaica', 'Fatullah', 'Dominica',
       'Dharmasala', 'St Vincent', 'Dharamsala', 'Dublin', 'Canberra',
       'Kanpur', 'Hyderabad', 'Bridgetown', 'Taunton', 'Bloemfontein',
       'Benoni', 'Bengaluru', 'Grenada', 'Vadodara', 'Port of Spain',
       'Paarl', 'Margao', 'Kimberley', 'Queenstown', 'Thiruvananthapuram',
       'Faisalabad', 'Dhaka', 'Bangalore', 'Kochi', 'Rawalpindi',
       'Peshawar', 'Sylhet', 'Kandy', 'Faridabad', "St George's",
       'Canterbury', 'Gros Islet', 'Darwin', 'Bogra', 'Jamshedpur',
       'Whangarei']
st.title('ODI Cricket Winning Predction')

pipe = pickle.load(open('ODIWinpipe.pkl','rb'))

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Seleect the batting team',teams)

with col1:
    bowling_team = st.selectbox('Seleect the bowling team',teams)               #streamlit run app.py

selected_city = st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    over = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')

if st.button('Predict Probablity'):
    runs_left = target - score
    balls_left = 300 - (over*6)
    wickets = 10 - wickets
    crr = score/over
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")