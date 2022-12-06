import boto3
import json

client = boto3.client('comprehend')

# Text for comprehend to analyze
input_text = """Hello Zhang Wei, I am John. Your AnyCompany Financial Services, LLC credit card account 1111-0000-1111-0008 has a minimum payment of $24.53 that is due by July 31st. Based on your autopay settings, we will withdraw your payment on the due date from your bank account number XXXXXX1111 with the routing number XXXXX0000. 
Customer feedback for Sunshine Spa, 123 Main St, Anywhere. Send comments to Alice at sunspa@mail.com. 
I enjoyed visiting the spa. It was very comfortable but it was also very expensive. The amenities were ok but the service made the spa a great experience."""

# Call the DetectPiiEntities (https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectPiiEntities.html) API on the input text
response = client.detect_pii_entities(
    Text = input_text,
    LanguageCode = 'en'
)

# Formate the response as a JSON string
json_string_formated_response = json.dumps(response, indent=2)

# Print the formated response
print(json_string_formated_response)