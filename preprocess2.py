import json

business_path = "yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json"
business_restaurants_path = "Processed/business_restaurants.json"
reviews_business_restaurants_path = "Processed/reviews_business_restaurants.json"
review_path = "../yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json"

reviews_data = []
business_ids = {}
business_id = {}
business_restaurants_data = []

#Generate dict with all business Ids
with open(business_restaurants_path) as business_restaurants_file:
    business_restaurants_data = json.load(business_restaurants_file)

for business in business_restaurants_data:
    business_id = { business["business_id"]: business["name"]}
    business_ids.update(business_id)

print("Dict generated")

#Generate review file

with open(review_path) as review_file:
    reviews_data=[json.loads(line) for line in review_file]

#with open(reviews_business_restaurants_path, "w") as output:
    #    json.dump([], output)

for review in reviews_data:
    review_data = {}
    if review["business_id"] in business_ids:
        review_data["business_id"] = review["business_id"]
        review_data["stars"] = review["stars"]
        review_data["text"] = review["text"]
        review_data["date"] = review["date"]
        review_data["votes"] = review["votes"]
        reviews_data.append(review_data)

print("Review file generated - ",reviews_data.count)

with open(reviews_business_restaurants_path, "w") as output:
    json.dump(reviews_data, output)            

print("Reviews Dumped")
