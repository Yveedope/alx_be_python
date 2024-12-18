#Ask user to choose weather
weather = input("What's the weather like today? (sunny/rainy/cold):").lower()

# Provide clothing recommendations based on the weather
if weather == "sunny":
    print("wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have a recommendation for this weather.")
