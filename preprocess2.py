import json

business_path = "yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json"
business_restaurants_path = "Processed/business_restaurants.json"
data = []

with open(business_restaurants_path) as data_file:
    data=json.load(data_file)

print(data[1000])
