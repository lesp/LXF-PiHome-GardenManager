import pifacerelayplus, time, pyowm

key = ('API KEY')

def pump(time):
	pfr = pifacerelayplus.PiFaceRelayPlus(pifacerelayplus.RELAY)
	pfr.relays[6].toggle()
	time.sleep(time)
	pfr.relays[6].toggle()	

def forecast(x,y):
        owm = pyowm.OWM(key)
        fc = owm.daily_forecast(x,y)
        f = fc.get_forecast()
        for weather in f:
                rain_forecast = str(weather.get_status())
        if rain_forecast != "rain":
                print('Rain is not forecast')
                pump(300)
                time.sleep(86400)
        else:
                print('Rain is forecast')
                time.sleep(86400)
    
while True:
        forecast('Blackpool,uk',1)
        
