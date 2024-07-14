import requests
import csv

def write_to_csv(filename, data):
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                writer.writerow(row)
        print(f"Data has been successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example data
data = [
    ['Episode', 'Status']
]

# Example usage:

def is_webpage_online(url):
    try:
        response = requests.get(url, timeout=10)  # Set a timeout to avoid long waits
        # Check if the status code is in the range of 200-299
        return 200 <= response.status_code < 300
    except requests.RequestException as e:
        # If any exception occurs, the webpage is considered offline
        print(f"An error occurred: {e}")
        return False

# Example usage
for i in range(1,1111):
    url = 'https://onepiece.fandom.com/wiki/Episode_'+str(i)
    print("Currently working on episode",i)
    if is_webpage_online(url):
        data.append([i,"Success"])
    else:
        data.append([i,"Failure"])

print("\n\n completed status check starting to write\n\n")

filename = "pagestatus.csv"
write_to_csv(filename, data)
