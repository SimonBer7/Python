
import pickle
import datetime

#zakladni format info
info = { 'pocet_spusteni': 0, 'posledni_spusteni': None }

try:
    with open("info.dat", "rb") as file:
        info = pickle.load(file)
except FileNotFoundError:
    info = {'pocet_spusteni': 0, 'posledni_spusteni': None}

#po kazdem spusteni provest
info['pocet_spusteni'] += 1
info['posledni_spusteni'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

with open("info.dat", "wb") as file:
    pickle.dump(info, file)

with open("info.dat", "rb") as file:
    loaded_info = pickle.load(file)

print("Počet spuštění:", loaded_info['pocet_spusteni'])
print("Poslední spuštění:", loaded_info['posledni_spusteni'])
