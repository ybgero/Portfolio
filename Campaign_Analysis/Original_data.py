import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuration
np.random.seed(42)
random.seed(42)
num_campaigns = 58
num_creatives_per_campaign = (4, 8)  # Min/Max
num_placements_per_creative = (3, 6)  # Min/Max
num_days = 90
start_date = datetime(2023, 10, 1)

# Helper functions
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def apply_seasonality(base_value, date):
    # Christmas effect
    if date.month == 12 and date.day in range(15, 31):
        return base_value * (1.5 + 0.5 * (date.day - 15) / 15)
    
    # Black Friday/Cyber Monday
    if date.month == 11 and date.day in range(23, 28):
        return base_value * 3.0
    
    # Valentine's Day
    if date.month == 2 and date.day in range(10, 15):
        return base_value * 2.0
    
    # Weekends
    if date.weekday() >= 5:
        return base_value * 1.2
    
    return base_value

# Generate Campaigns
campaign_types = ['Brand Awareness', 'Lead Gen', 'Product Launch', 'Retargeting', 'Seasonal', 'Competitor']
target_audiences = ['Millennials', 'Gen Z', 'Gen X', 'Boomers', 'Business Owners']
customer_segments = ['Premium', 'Standard', 'New', 'Lapsed', 'VIP']
languages = ['English', 'Spanish', 'French', 'German', 'Multilingual']
locations = ['US', 'UK', 'Canada', 'Australia', 'Global']

campaigns = pd.DataFrame({
    'Campaign_ID': [f'CMP{i:03d}' for i in range(1, num_campaigns+1)],
    'Campaign_Name': [f'Campaign {x}' for x in range(1, num_campaigns+1)],
    'Campaign_Type': np.random.choice(campaign_types, num_campaigns, p=[0.25, 0.3, 0.15, 0.15, 0.1, 0.05]),
    'Target_Audience': np.random.choice(target_audiences, num_campaigns),
    'Customer_Segment': np.random.choice(customer_segments, num_campaigns),
    'Language': np.random.choice(languages, num_campaigns, p=[0.6, 0.15, 0.1, 0.1, 0.05]),
    'Location': np.random.choice(locations, num_campaigns, p=[0.5, 0.2, 0.15, 0.1, 0.05]),
    'Start_Date': [random_date(start_date, start_date + timedelta(days=30)) for _ in range(num_campaigns)],
    'Budget_Allocated': [round(random.uniform(5000, 50000), 2) for _ in range(num_campaigns)],
    'Campaign_Goal': np.random.choice(['Awareness', 'Conversions', 'Revenue', 'Engagement'], num_campaigns)
})

# Set End Date (30-90 days after start)
campaigns['End_Date'] = campaigns['Start_Date'].apply(
    lambda x: x + timedelta(days=random.randint(30, 90))
)

# Generate Creatives
creative_counter = 1
creatives_data = []

ad_formats = ['Video', 'Image', 'Carousel', 'Story']
device_types = ['Mobile', 'Desktop', 'Tablet', 'All']
creative_themes = ['Summer', 'Winter', 'Family', 'Adventure', 'Luxury', 'Discount']

for _, campaign in campaigns.iterrows():
    num_creatives = random.randint(num_creatives_per_campaign[0], num_creatives_per_campaign[1])
    for _ in range(num_creatives):
        creatives_data.append({
            'Creative_ID': f'CRT{creative_counter:04d}',
            'Campaign_ID': campaign['Campaign_ID'],
            'Creative_Name': f"Creative {creative_counter} - {campaign['Campaign_Name']}",
            'Ad_Format': np.random.choice(ad_formats, p=[0.4, 0.3, 0.2, 0.1]),
            'Device_Type': np.random.choice(device_types, p=[0.6, 0.3, 0.05, 0.05]),
            'Creative_Language': campaign['Language'],
            'Creative_Theme': np.random.choice(creative_themes),
            'Production_Cost': round(random.uniform(200, 5000), 2)
        })
        creative_counter += 1

creatives = pd.DataFrame(creatives_data)

# Generate Placements
placement_counter = 1
placements_data = []

channels = ['Social', 'Search', 'Display', 'Email', 'Native']
source_platforms = {
    'Social': ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'TikTok'],
    'Search': ['Google', 'Bing', 'Yahoo'],
    'Display': ['Google Display', 'Programmatic', 'Direct Publishers'],
    'Email': ['Newsletter', 'Drip Campaign', 'Promotional'],
    'Native': ['Taboola', 'Outbrain', 'Revcontent']
}
mediums = ['CPC', 'CPM', 'CPA', 'CPV']
placement_priorities = ['Primary', 'Secondary', 'Testing']

for _, creative in creatives.iterrows():
    num_placements = random.randint(num_placements_per_creative[0], num_placements_per_creative[1])
    channel = np.random.choice(channels, p=[0.4, 0.3, 0.15, 0.1, 0.05])
    for _ in range(num_placements):
        placements_data.append({
            'Placement_ID': f'PLM{placement_counter:05d}',
            'Creative_ID': creative['Creative_ID'],
            'Placement_Name': f"{channel} Placement - {creative['Creative_Name']}",
            'Channel': channel,
            'Source_Platform': np.random.choice(source_platforms[channel]),
            'Medium': np.random.choice(mediums, p=[0.5, 0.3, 0.15, 0.05]),
            'Placement_Priority': np.random.choice(placement_priorities, p=[0.6, 0.3, 0.1]),
            'Target_CPA': round(random.uniform(5, 50), 2)
        })
        placement_counter += 1

placements = pd.DataFrame(placements_data)

# Generate Performance Data (daily for each placement)
performance_data = []
current_date = start_date

for _ in range(num_days):
    for _, placement in placements.iterrows():
        # Base metrics
        base_impressions = random.randint(1000, 50000)
        base_ctr = random.uniform(0.01, 0.05)
        base_conversion_rate = random.uniform(0.01, 0.10)
        base_engagement = random.uniform(0.5, 5.0)
        
        # Apply seasonality
        impressions = apply_seasonality(base_impressions, current_date)
        ctr = apply_seasonality(base_ctr, current_date)
        
        clicks = int(impressions * ctr)
        conversions = int(clicks * base_conversion_rate)
        engagement_score = apply_seasonality(base_engagement, current_date)
        time_on_page = random.uniform(10, 180) if conversions > 0 else random.uniform(2, 15)
        bounce_rate = random.uniform(0.3, 0.8)
        revenue = round(conversions * random.uniform(10, 100), 2)
        cost = round(clicks * random.uniform(0.2, 2.5), 2)
        
        performance_data.append({
            'Date': current_date,
            'Placement_ID': placement['Placement_ID'],
            'Clicks': clicks,
            'Impressions': int(impressions),
            'Conversions': conversions,
            'Engagement_Score': round(engagement_score, 2),
            'Time_On_Page': round(time_on_page, 1),
            'Bounce_Rate': round(bounce_rate, 2),
            'Revenue_Generated': revenue,
            'Cost_Spent': cost
        })
    
    current_date += timedelta(days=1)

performance = pd.DataFrame(performance_data)

# Add 3 intentional outliers
performance.loc[1234, 'Revenue_Generated'] = 15000  # High revenue outlier
performance.loc[4567, 'CTR'] = 0.75  # Unusually high CTR
performance.loc[2890, 'Conversions'] = -5  # Data entry error

# Calculate CTR after creating outliers
performance['CTR'] = performance['Clicks'] / performance['Impressions']

# Merge all data
full_data = pd.merge(
    pd.merge(
        pd.merge(
            performance,
            placements,
            on='Placement_ID'
        ),
        creatives,
        on='Creative_ID'
    ),
    campaigns,
    on='Campaign_ID'
)

# Reorder columns
columns_order = [
    'Campaign_ID', 'Campaign_Name', 'Campaign_Type', 'Target_Audience', 'Customer_Segment',
    'Language', 'Location', 'Start_Date', 'End_Date', 'Budget_Allocated', 'Campaign_Goal',
    'Creative_ID', 'Creative_Name', 'Ad_Format', 'Device_Type', 'Creative_Language', 
    'Creative_Theme', 'Production_Cost', 'Placement_ID', 'Placement_Name', 'Channel',
    'Source_Platform', 'Medium', 'Placement_Priority', 'Target_CPA', 'Date', 'Clicks',
    'Impressions', 'CTR', 'Conversions', 'Engagement_Score', 'Time_On_Page', 'Bounce_Rate',
    'Revenue_Generated', 'Cost_Spent'
]

full_data = full_data[columns_order]

# Save to CSV
full_data.to_csv('marketing_campaigns_full.csv', index=False)

print(f"Dataset generated with {len(full_data)} rows")
print("Columns:", full_data.columns.tolist())