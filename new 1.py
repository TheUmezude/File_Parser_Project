import requests
import json

url = "https://api.hatchways.io/assessment/blog/posts"
query_item = "?tag="
dictionary_list = []
tags = []
new_list = []
resultant_dictionary = {}
sorted_dict = {}


ask_tag_no = int(input("How many tags do you wish to search for? "))

for items in range(0, ask_tag_no):
    add_on = input("Enter the tag you need: ")
    complete_url = url + query_item + add_on
    result = requests.get(complete_url)
    dictionary_list.append(json.loads(result.text))
    
for item1 in range(0, len(dictionary_list)):
    for item2 in range(0, len(dictionary_list[item1]["posts"])):
        if dictionary_list[item1]["posts"][item2] not in new_list:
            new_list.append(dictionary_list[item1]["posts"][item2])


resultant_dictionary["posts"] = new_list
print(resultant_dictionary)