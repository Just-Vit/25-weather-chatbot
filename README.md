# 25-weather-chatbot

>>>Add the final function to make the whole project working

Now that you have the city, you can call the get_weather() function:


    city_weather = get_weather(city)
    if city_weather is not None:
        return "In " + city + ", the current weather is: " + city_weather
    else:
        return "Something went wrong."
    else:
        return "Sorry I don't understand that. Please rephrase your statement."
    
    
Recall that if an error is returned by the OpenWeather API, you print the error code to the terminal, and the get_weather() function returns None. In this code, you first check whether the get_weather() function returns None. If it doesn’t, then you return the weather of the city, but if it does, then you return a string saying something went wrong. The final else block is to handle the case where the user’s statement’s similarity value does not reach the threshold value. In such a case, you ask the user to rephrase their statement.

Having completed all of that, you now have a chatbot capable of telling a user conversationally what the weather is in a city. The difference between this bot and rule-based chatbots is that the user does not have to enter the same statement every time. Instead, they can phrase their request in different ways and even make typos, but the chatbot would still be able to understand them due to spaCy’s NLP features.

Let’s test the bot. Call the chatbot() function and pass in a statement asking what the weather is in a city, for example:
  
 
    response = chatbot("Is it going to rain in New York today?")
    print(response)

Save and close the file, then run the script in your terminal:


    python3 w_4_chatbot_good.py

You will receive output similar to the following:

    Output
    In New York, the current weather is: clear sky

