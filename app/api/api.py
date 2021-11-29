from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("<YOUR_API_TOKEN>")

# Prepare the actor input
run_input = {
    "startUrls": [{ "url": "https://www.transfermarkt.com/lionel-messi/profil/spieler/28003" }],
    "proxyConfig": { "useApifyProxy": True },
    "crawlDepth": 1,
    "pageDepth": 1,
}

# Run the actor and wait for it to finish
run = client.actor("petr_cermak/transfermarkt").call(run_input=run_input)

# Fetch and print actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)