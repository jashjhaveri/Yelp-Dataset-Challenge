import json

reviews_business_restaurants_path = "Processed/reviews_business_restaurants.json"
reviews_business_count = "Processed/reviews_business_count.json"

reviews_business_data = []
with open (reviews_business_restaurants_path) as reviews_business_file:
    reviews_business_data = json.load(reviews_business_file)
print("File loaded")

reviews_per_business = {}
review_business = {}

for review in reviews_business_data:
    if review["business_id"] in reviews_per_business:
        business_id = review["business_id"]
        reviews_per_business[business_id] = reviews_per_business[business_id] + 1
    else:
        review_business = { review["business_id"] : 1}
        reviews_per_business.update(review_business)
print("Reviews count generated")

with open(reviews_business_count, "w") as output:
    json.dump(reviews_per_business, output, indent=4)


print("List of revisions per business generated")
