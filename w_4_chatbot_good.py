import spacy
import requests

nlp = spacy.load("en_core_web_md")

api_key = "7f344331d0b2323597bb5c0818ed1cce"

def get_weather(city_name):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)

    response = requests.get(api_url)
    response_dict = response.json()
    #print(response_dict)
    weather = response_dict["weather"][0]["description"]

    if response.status_code == 200:
        return weather
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

#test_1
#Add those two lines and run just to test the code (output was "mist")		
#weather1 = get_weather("Brisbane")
#print(weather1)		

def chatbot(statement):
    weather = nlp("Current weather in a city")
    nlp_doc = nlp(statement)
    min_similarity = 0.70
    
    if weather.similarity(nlp_doc) >= min_similarity:
        pass
        #similarity = weather.similarity(statement)
        #return similarity
        
#test_2
#Add those two lines and run just to test the "similarity"code 	
#similarity1 = chatbot("What is the weather in Seoul")
#print(similarity1)       
        
        for ent in nlp_doc.ents:
            if ent.label_ == "GPE": # GeoPolitical Entity
                city = ent.text
                break
#                return city
            else:
                return "You need to tell me a city to check."      

#test_3
#Check city name extraction from "statement"
#city1 = chatbot("What is the weather in Kiev")
#print(city1)  	 

            
        city_weather = get_weather(city)
        if city_weather is not None:
            return "In " + city + ", the current weather is: " + city_weather
            
        else:
            return "Something went wrong."
#        else:
#            return "Sorry I don't understand that. Please rephrase your statement."              
#        pass

#Test_4 chatbot 
#response1 = 
response1 = chatbot("What is the weather in New York?")
print(response1)       
        




