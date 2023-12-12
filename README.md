# PONB3
Algorithm 3 for PONB university project

## Testing

### Configuration

```bash
# Install Flask
pip install flask

# Run program
python <program>.py
```

```bash
# Define the URL and JSON payload
$url = "http://localhost:5000/calculate_weight"

# Fill payload with sample data
$payload = @{
    weight_on_earth = 75
    planet = "MARS"
}

# Convert the payload to JSON
$jsonPayload = $payload | ConvertTo-Json

# Make the POST request
$response = Invoke-RestMethod -Uri $url -Method Post -Body $jsonPayload -Headers @{ "Content-Type" = "application/json" }

# Display the response
$response
```
## Sample output

```bash
weight_on_planet
----------------
        26,36388
```
