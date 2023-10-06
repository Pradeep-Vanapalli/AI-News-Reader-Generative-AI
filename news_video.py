import requests
import json

class VideoGenerator:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_video(self, input_text, source_url):
        url = "https://api.d-id.com/talks"

        payload = {
            "script": {
                "type": "text",
                "subtitles": "false",
                "provider": {
                    "type": "microsoft",
                    "voice_id": "en-US-JennyNeural"
                },
                "ssml": "false",
                "input": input_text
            },
            "config": {
                "fluent": "false",
                "pad_audio": "0.0"
            },
            "source_url": source_url
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX2N1c3RvbWVyX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9uYW1lIjoidHJpYWwiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9zdWJzY3JpcHRpb25faWQiOiIiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9iaWxsaW5nX2ludGVydmFsIjoibW9udGgiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9wbGFuX2dyb3VwIjoiZGVpZC10cmlhbCIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX3ByaWNlX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJpY2VfY3JlZGl0cyI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9jcmVkaXRzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vcHJvdmlkZXIiOiJnb29nbGUtb2F1dGgyIiwiaHR0cHM6Ly9kLWlkLmNvbS9pc19uZXciOmZhbHNlLCJodHRwczovL2QtaWQuY29tL2FwaV9rZXlfbW9kaWZpZWRfYXQiOiIyMDIzLTEwLTA2VDE0OjM5OjQzLjMxMVoiLCJodHRwczovL2QtaWQuY29tL29yZ19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vYXBwc192aXNpdGVkIjpbIlN0dWRpbyJdLCJodHRwczovL2QtaWQuY29tL2N4X2xvZ2ljX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jcmVhdGlvbl90aW1lc3RhbXAiOiIyMDIzLTEwLTA2VDE0OjM5OjIyLjQ1M1oiLCJodHRwczovL2QtaWQuY29tL2FwaV9nYXRld2F5X2tleV9pZCI6InJpMzBlZDkxd2giLCJodHRwczovL2QtaWQuY29tL2hhc2hfa2V5IjoibXNNekp0TjVWSl83WHQ2OWZjOGJpIiwiaHR0cHM6Ly9kLWlkLmNvbS9wcmltYXJ5Ijp0cnVlLCJodHRwczovL2QtaWQuY29tL2VtYWlsIjoidnBscDIwMTFiYXRjaEBnbWFpbC5jb20iLCJpc3MiOiJodHRwczovL2F1dGguZC1pZC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTY2NDc5NjY3NzAxODk2Nzg1NzEiLCJhdWQiOlsiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTY2MDMyMDQsImV4cCI6MTY5NjY4OTYwNCwiYXpwIjoiR3pyTkkxT3JlOUZNM0VlRFJmM20zejNUU3cwSmxSWXEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgb2ZmbGluZV9hY2Nlc3MifQ.Pd3Dvkz3WJ6kxXe-Mi4mffT9FvPjTtWH9Rx7zEmzH38vSDl_tc_yAewZFR3vtlcZmdxXHNBV5imsnRiK2Q12DeIOEyniP_jzh5uVMJznZxcj7eBem8slHI0uW2PK7_OUeQ_JR7ni3-qfIWj5CZ-ekhTOU8qo9f9fBdo3F4FNnzW3OssOk4wEHoqo3leDSRwqNmXuOs_FVV77PIDC1L1H1NnQll9aLJC5_jKmqic2Ttv-ZpsdECMaokgdNuq_Lus4bJH0F1gam1RiC0CLlK3kp5BXh5yLFWHmXJhnQBsvB1dfxgTGcYrNH1IINxVQ73ObONQqPrs65j_RM4tTold7hA"
        }

        response = requests.post(url, json=payload, headers=headers)
        _response = json.loads(response.text)
        print("Response: ",_response)
        while _response["status"] != "created":
            response = requests.post(url, json=payload, headers=headers)
            _response = json.loads(response.text)

        talk_id = json.loads(response.text)['id']

        talk_url = f"{url}/{talk_id}"
        print(talk_url)

        headers = {
            "accept": "application/json",
            "authorization": f"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX2N1c3RvbWVyX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJvZHVjdF9uYW1lIjoidHJpYWwiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9zdWJzY3JpcHRpb25faWQiOiIiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9iaWxsaW5nX2ludGVydmFsIjoibW9udGgiLCJodHRwczovL2QtaWQuY29tL3N0cmlwZV9wbGFuX2dyb3VwIjoiZGVpZC10cmlhbCIsImh0dHBzOi8vZC1pZC5jb20vc3RyaXBlX3ByaWNlX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfcHJpY2VfY3JlZGl0cyI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9jcmVkaXRzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jaGF0X3N0cmlwZV9wcmljZV9pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vcHJvdmlkZXIiOiJnb29nbGUtb2F1dGgyIiwiaHR0cHM6Ly9kLWlkLmNvbS9pc19uZXciOmZhbHNlLCJodHRwczovL2QtaWQuY29tL2FwaV9rZXlfbW9kaWZpZWRfYXQiOiIyMDIzLTEwLTA2VDE0OjM5OjQzLjMxMVoiLCJodHRwczovL2QtaWQuY29tL29yZ19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vYXBwc192aXNpdGVkIjpbIlN0dWRpbyJdLCJodHRwczovL2QtaWQuY29tL2N4X2xvZ2ljX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jcmVhdGlvbl90aW1lc3RhbXAiOiIyMDIzLTEwLTA2VDE0OjM5OjIyLjQ1M1oiLCJodHRwczovL2QtaWQuY29tL2FwaV9nYXRld2F5X2tleV9pZCI6InJpMzBlZDkxd2giLCJodHRwczovL2QtaWQuY29tL2hhc2hfa2V5IjoibXNNekp0TjVWSl83WHQ2OWZjOGJpIiwiaHR0cHM6Ly9kLWlkLmNvbS9wcmltYXJ5Ijp0cnVlLCJodHRwczovL2QtaWQuY29tL2VtYWlsIjoidnBscDIwMTFiYXRjaEBnbWFpbC5jb20iLCJpc3MiOiJodHRwczovL2F1dGguZC1pZC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTY2NDc5NjY3NzAxODk2Nzg1NzEiLCJhdWQiOlsiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTY2MDMyMDQsImV4cCI6MTY5NjY4OTYwNCwiYXpwIjoiR3pyTkkxT3JlOUZNM0VlRFJmM20zejNUU3cwSmxSWXEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgb2ZmbGluZV9hY2Nlc3MifQ.Pd3Dvkz3WJ6kxXe-Mi4mffT9FvPjTtWH9Rx7zEmzH38vSDl_tc_yAewZFR3vtlcZmdxXHNBV5imsnRiK2Q12DeIOEyniP_jzh5uVMJznZxcj7eBem8slHI0uW2PK7_OUeQ_JR7ni3-qfIWj5CZ-ekhTOU8qo9f9fBdo3F4FNnzW3OssOk4wEHoqo3leDSRwqNmXuOs_FVV77PIDC1L1H1NnQll9aLJC5_jKmqic2Ttv-ZpsdECMaokgdNuq_Lus4bJH0F1gam1RiC0CLlK3kp5BXh5yLFWHmXJhnQBsvB1dfxgTGcYrNH1IINxVQ73ObONQqPrs65j_RM4tTold7hA"
        }

        response = requests.get(talk_url, headers=headers)
        print(f"Response is: {response}")
        video_response = json.loads(response.text)
        print(f"video Response is: {video_response}")

        while video_response["status"] != "done":
            response = requests.get(talk_url, headers=headers)
            video_response = json.loads(response.text)

        video_url = video_response["result_url"]
        return video_url
