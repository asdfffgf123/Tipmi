import requests

API_KEY = "IDE_IRD_BE_A_SAJAJAT_API_KULCSOD"  # vagy 44d9cf4feabb487580337050320289c6
headers = {
    "X-Auth-Token": API_KEY
}

competitions = ["PL", "PD", "SA", "BL1", "FL1", "CL", "NB1"]

for comp in competitions:
    url = f"https://api.football-data.org/v4/competitions/{comp}/matches"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(f"\n==== {comp} Matches ====\n")
        print(data)
    else:
        print(f"Error {comp}: {response.status_code}")
