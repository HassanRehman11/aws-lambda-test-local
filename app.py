import boto3
import requests



def handler(event, context):
    task = event.get("task",None)
    zodiac_list=["aries", "Taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]
    day_list = ["yesterday","today","tomorrow"]
    task_list = ["list_zodiac","get_horoscope"]
    if((task!=None) and (task in task_list)):
        if(task=="list_zodiac"):
            return({"zodiac":zodiac_list})
        
        elif(task=="get_horoscope"):
            sign = event.get("sign",None)
            day = event.get("day",None)
            if(sign!=None and day!=None):
                if((sign not in zodiac_list) and (day not in day_list)):
                   return({"message":"Wrong sign or day passed"})
                params = (
                ('sign', sign),
                ('day', day),
                )

                r = requests.post('https://aztro.sameerkumar.website/', params=params)
                return r.json()
            else:
                return({"message":"Send sign and day as parameter"})
    else:
        return({"message":"Send task as parameter"})

