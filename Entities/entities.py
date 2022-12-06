import boto3
import json

client = boto3.client('comprehend')

input_text = """Hello Zhang Wei, I am John. Your AnyCompany Financial Services, LLC credit card account 1111-0000-1111-0008 has a minimum payment of $24.53 that is due by July 31st. Based on your autopay settings, we will withdraw your payment on the due date from your bank account number XXXXXX1111 with the routing number XXXXX0000. 
Customer feedback for Sunshine Spa, 123 Main St, Anywhere. Send comments to Alice at sunspa@mail.com. 
I enjoyed visiting the spa. It was very comfortable but it was also very expensive. The amenities were ok but the service made the spa a great experience."""


response = client.detect_entities(
    Text = input_text,
    LanguageCode = 'en'
)

json_string_formated_response = json.dumps(response, indent=2)

print(json_string_formated_response)