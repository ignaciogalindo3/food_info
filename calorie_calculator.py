
import requests


def totalCalories():

    # query = '1lb brisket and fries'
    # api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
    # response = requests.get(api_url, headers={'X-Api-Key': 'J2OcrIPN3tUZmTcBRoNwBw==RjghtIYCHPsiQXxK'})
    # api_data = response.json()

    # if response.status_code == requests.codes.ok:
    #     print(response.text)

    # else:
    #     print("Error:", response.status_code, response.text)


    interaction = True


    calorie_count = 0
    protein_count = 0

    while interaction:
        food_query = input(str("List a food: "))
        api_url = f'https://api.api-ninjas.com/v1/nutrition?query={food_query}'
        response = requests.get(api_url, headers={'X-Api-Key': 'J2OcrIPN3tUZmTcBRoNwBw==RjghtIYCHPsiQXxK'})
        if response.status_code == requests.codes.ok:
            # print(response.text)
            pass

        else:
            print("Error:", response.status_code, response.text)
            

        api_data = response.json()
        
        for food_dict in api_data:
            calorie_count += float(food_dict["calories"])
            # print(food_dict)
            protein_count += float(food_dict["protein_g"])
        question = input(str("Do you want to add another food? "))  #answer yes or no
        if question == "yes".lower():
            continue
        elif question == "no".lower():
            return f"You have consumed {calorie_count} calories and {protein_count} grams of protein today"
            
        else:
            while True:
                sus_answer = input(str("Enter yes or no: "))
                if sus_answer == "yes".lower():
                    break
                elif sus_answer == "no".lower():
                    return f"You have consumed {calorie_count} calories and {protein_count} grams of protein today"
                else:
                    continue



print(totalCalories())
                        




