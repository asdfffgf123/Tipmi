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
