import json

business_path = "yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json"
business_restaurants_path = "Processed/business_restaurants.json"
data = []

with open(business_path) as data_file:
    data=[json.loads(line) for line in data_file]

#with open(business_restaurants_path) as data_file:
#       output_data=[json.loads(line) for line in data_file]

#count = 0
output_data = []

for business in data:
    print(business)
    business_data = {}
    
    for category in business["categories"]:
        if category == "Restaurants":
            business_data["business_id"] = business["business_id"]
            business_data["name"] = business["name"]
            business_data["city"] = business["city"]
            business_data["state"] = business["state"]
            business_data["stars"] = business["stars"]
            business_data["review_count"] = business["review_count"]
            business_data["attributes"] = business["attributes"]
            output_data.append(business_data)
    #output_data.write("\n")
    #count = count+1 
    #if count==6:
    #   break
with open(business_restaurants_path, "w") as output:
    json.dump(output_data, output)
