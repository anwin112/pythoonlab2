from datetime import datetime, timedelta

# Generate sample weather data
def generate_sample_data(start_date, end_date):
    """Generate sample weather data for a given date range."""
    data = []
    current_date = start_date
    while current_date <= end_date:
        # Generate random weather data
        max_temp = round(15 + 20 * (current_date.month / 12), 2)
        min_temp = round(max_temp - 10 + 5 * (current_date.month / 12), 2)
        humidity = round(50 + 30 * (current_date.month / 12), 2)
        data.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'max_temp': max_temp,
            'min_temp': min_temp,
            'humidity': humidity
        })
        current_date += timedelta(days=1)
    return data

# Initialize date range
start_date = datetime(2023, 8, 1)
end_date = datetime(2024, 7, 10)

# Generate sample weather data
weather_data = generate_sample_data(start_date, end_date)

def find_highest_and_lowest_temps(data):
    """Find the highest and lowest temperatures recorded."""
    highest_temp = max(day['max_temp'] for day in data)
    lowest_temp = min(day['min_temp'] for day in data)
    return highest_temp, lowest_temp

def count_hot_days(data, threshold=30):
    """Determine the number of days with temperatures above a given threshold."""
    hot_days = sum(1 for day in data if day['max_temp'] > threshold)
    return hot_days

def compute_average_humidity(data):
    """Compute the average humidity over the specified period."""
    total_humidity = sum(day['humidity'] for day in data)
    average_humidity = total_humidity / len(data)
    return average_humidity

# Analyze the weather data
highest_temp, lowest_temp = find_highest_and_lowest_temps(weather_data)
hot_days = count_hot_days(weather_data)
average_humidity = compute_average_humidity(weather_data)

# Display the results
print(f"Highest Temperature Recorded: {highest_temp}°C")
print(f"Lowest Temperature Recorded: {lowest_temp}°C")
print(f"Number of Days with Temperatures Above 30°C: {hot_days}")
print(f"Average Humidity Over the Period: {average_humidity:.2f}%")
