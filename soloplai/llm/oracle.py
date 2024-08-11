from importlib import resources as rsrc
from sys import stderr

import yaml
from openai import OpenAI

from . import config


class Oracle:
    """An 'oracle' in solo-RPG terms is a randomized mechanism to make a determination about the game world. This is
    the singleton object for the Oracle. It will depend on some externally running LLM service.
    """

    __instance: "Oracle|None" = None
    _client: OpenAI
    _base_url: str
    _api_key: str

    def __new__(cls):
        if cls.__instance is None:
            new = super(Oracle, cls).__new__(cls)
            new._load_config()
            new._refresh_client()
            cls.__instance = new
        return cls.__instance

    def _load_config(self):
        conf_path = str(rsrc.files(config) / "config.yaml")
        with open(conf_path) as FILE:  # pylint: disable=unspecified-encoding,invalid-name
            conf = yaml.safe_load(FILE)
        self._base_url = conf["base_url"]
        self._api_key = conf["api_key"]

    def _refresh_client(self):
        try:
            self._client.close()
        except AttributeError:
            pass
        except Exception as e:
            print(e, file=stderr)
        self._client = OpenAI(base_url=self._base_url, api_key=self._api_key)

    def do_completion(self, sys_prompt: str, usr_prompt: str) -> str:
        completion = self._client.chat.completions.create(
            model="LLaMA_CPP",
            messages=[
                {
                    "role": "system",
                    "content": sys_prompt,
                },
                {
                    "role": "user",
                    "content": usr_prompt,
                },
            ],
        )
        return [(i, c.message.content) for i, c in enumerate(completion.choices)]
