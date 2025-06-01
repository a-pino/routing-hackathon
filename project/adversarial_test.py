import json
import logging
from tqdm.notebook import tqdm
from typing import List

import openai
from openai.types.chat import (
    chat_completion,
    chat_completion_message,
)

from martian_apart_hack_sdk import exceptions, judge_specs, martian_client, utils
from martian_apart_hack_sdk.models import judge_evaluation, llm_models, router_constraints

# Load the config and make a client.
config = utils.load_config()
client = martian_client.MartianClient(
    api_url=config.api_url,
    api_key=config.api_key,
)

# One quick thing we can do with the client is confirm we have credits.
credit_balance = client.organization.get_credit_balance()
print(credit_balance)


openai_client = openai.OpenAI(
    api_key=config.api_key,
    base_url=config.api_url + "/openai/v2"
)

