from enum import Enum
from http import HTTPStatus
from typing import Dict

import requests

SLACK_WEB_HOOK_URL = 'https://hooks.slack.com/services/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'


class Color(str, Enum):
    RED = "#DB0000"
    GRAY = "#D3D3D3"


def send_error_case(target_url: str, http_status: HTTPStatus = None):
    payload = {
        "attachments": [
            {
                "mrkdwn_in": ["text"],
                "color": Color.RED.value,
                "title": f"[{target_url}] tests failed",
                "fields": [
                    {
                        "title": "HTTP Status",
                        "value": f"{http_status}",
                        "short": False
                    }
                ]
            }
        ]
    }
    send_to_slack(payload)


def send_shutdown_case(target_url: str):
    payload = {
        "attachments": [
            {
                "mrkdwn_in": ["text"],
                "color": Color.GRAY.value,
                "title": f"[{target_url}] tests shutdown",
                "fields": [
                    {
                        "title": "HTTP Status",
                        "value": "UNKNOWN",
                        "short": False
                    }
                ]
            }
        ]
    }
    send_to_slack(payload)


def send_to_slack(payload: Dict):
    requests.post(url=SLACK_WEB_HOOK_URL, json=payload)
