import openai
import requests
import xml.etree.ElementTree as ET

from prompts import wolfram_alpha_parser_sys_prompt, wolfram_alpha_parser_init_prompt
from config import WOLFRAM_APP_ID


class WolframAlphaAPI:
    def __init__(self):
        self.app_id = WOLFRAM_APP_ID
        self.full_length_url = 'http://api.wolframalpha.com/v2/query'
        self.llm_url = 'https://www.wolframalpha.com/api/v1/llm-api'

    def _send_request(self, url: str, query: str) -> str:
        params = {'appid': self.app_id, 'input': query}
        response = requests.get(url, params=params)
        return response.text

    def _parse_full_length_response(self, xml_response: str):
        raw_answers = []

        root = ET.fromstring(xml_response)
        result_pod = root.find("./pod[@id='Result']")
        result_subpods = result_pod.findall('subpod')

        for subpod in result_subpods:
            plaintext_tag = subpod.find('plaintext')
            plaintext = plaintext_tag.text
            raw_answers.append(plaintext)

        return raw_answers

    def full_length_result_query(self, query: str):
        xml_response = self._send_request(self.full_length_url, query)
        # print(xml_response)
        try:
            res = self._parse_full_length_response(xml_response)
            return res
        except:
            # Let's use OpenAi to parse the response
            messages = [
                {
                    'role': "system",
                    'content': wolfram_alpha_parser_sys_prompt
                },
                {
                    'role': "user",
                    'content': wolfram_alpha_parser_init_prompt.format(Query=query, WolframApiOutput=xml_response)
                }

            ]
            completion = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                temperature=0,
                max_tokens=2048,
            )
            res = completion.choices[0].message["content"]
            return res

        return "NO_ANSWER_FOUND"

    def llm_query(self, query: str):
        return self._send_request(self.llm_url, query)
